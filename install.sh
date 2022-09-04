#!/usr/bin/env bash

# Check os-release files...
if [ -f "/etc/os-release" ]; then
    source "/etc/os-release"
fi

# Helper function
function log() {
    title=$LOG_TITLE
    message="$1"

    echo -e "[$title]: $message"
}

function InstalledPackage() {
    if [[ $(which $1 2>/dev/null) ]]; then
        echo "true"
    fi
}

function Input() {
    read -p "$1" result
    echo $result
}

function GetDistroID() {
    if [[ ! $ID_LIKE ]]; then
        echo $ID
    else
        echo $ID_LIKE
    fi
}

function CompilePython() {
    OUTPUT_PATH="dist"

    if [[ $1 ]]; then
        OUTPUT_PATH="$1"
    fi

    pyinstaller -F src/main.py \
        --workpath "$OUTPUT_PATH/build" \
        --distpath "$OUTPUT_PATH/bin" \
        --log-level "WARN" \
        --clean
}

function InstallBinary() {
    case $1 in
    "user")
        if [[ ! -d "$HOME/.local/bin" ]]; then
            mkdir "$HOME/.local/bin"
        fi

        log "Installing binary to user dir..."
        install dist/bin/main $HOME/.local/bin/sfetch
        log "Done"
        ;;
    "root")
        log "Installing binary to root dir..."
        sudo install dist/bin/main /usr/local/bin/sfetch
        log "Done"
        ;;
    esac
}

# Generate current installed state
function GenerateState() {
    echo "INSTALLED_STATE=$1" >state.conf
}

# Variable
LOG_TITLE="LOG"
DISTRO_ID=$(GetDistroID)

# Install Methods
# For Arch Based
function ArchInstall() {
    # Check is pip installed or not
    if ! $(InstalledPackage python3); then
        log "python3 is not installed"
        answer=$(Input "Do you want to install python3? [y/n]: ")
        if [[ $answer == "y" || $answer == "Y" ]]; then
            log "Installing python3..."
            sudo pacman -S python3 --noconfirm
        else
            log "Because python3 isn't going installed, so the installation process will be cancelled"
            exit 1
        fi
    fi

    # Prompt if user want to install in root or user dir
    TARGET="user"
    PromptTarget=$(Input "Do you want install this program on root dir? [y/n]: ")
    if [[ $PromptTarget == "y" || $PromptTarget == "Y" ]]; then
        TARGET="root"
    fi

    log "Check if local environment existed..."

    if [[ ! -d ".env" ]]; then
        python3 -m venv .env
        source .env/bin/activate
        log "Installing dependencies..."
        pip install -r requirements.txt
    else
        source .env/bin/activate
    fi

    CompilePython
    InstallBinary $TARGET
    GenerateState $TARGET
}

# Determine Install Method
case $DISTRO_ID in
"arch")
    ArchInstall
    ;;
*)
    log "Please manually install dependencies, cause we didn't support this distro yet"
    ;;
esac
