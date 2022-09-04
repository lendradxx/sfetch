#!/usr/bin/env bash

# Variable
LOG_TITLE="LOG"

# Helper function
function log() {
    title=$LOG_TITLE
    message="$1"

    echo -e "[$title]: $message"
}

if [ ! -f "state.conf" ]; then
    log "State file cannot be found, you must remove it manually!"
    exit 1
else
    source ./state.conf
fi

function UpdateState() {
    echo "INSTALLED_STATE=false" >state.conf
}

case $INSTALLED_STATE in
"user")
    log "Removing sfetch..."
    rm $HOME/.local/bin/sfetch
    UpdateState
    ;;
"root")
    log "Removing sfetch..."
    sudo rm /usr/local/bin/sfetch
    UpdateState
    ;;
"false")
    log "sfetch isn't installed yet!"
    ;;
esac
