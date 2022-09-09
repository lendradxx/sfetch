from curses import resetty
import os


def SearchPackage(package_name: str):
    if os.popen(f"which {package_name} 2>/dev/null").readable():
        return os.popen(f"which {package_name} 2>/dev/null").read()


def GetPackageManagerList():
    result = []
    if SearchPackage("pacman"):
        result.append("pacman")
    elif SearchPackage("apt"):
        result.append("apt")
    elif SearchPackage("dnf"):
        result.append("dnf")
    elif SearchPackage("zypper"):
        result.append("zypper")
    elif SearchPackage("apk"):
        result.append("apk")
    elif SearchPackage("pkcon"):
        result.append("packagekit")
    else:
        result.append("null")

    if SearchPackage("flatpak"):
        result.append("flatpak")

    if SearchPackage("snap"):
        result.append("snap")

    return result


def GetTotalPackages(package_managers: list[str]):
    packages: list[str] = []
    result = ""

    for package_manager in package_managers:
        match package_manager:
            case "pacman":
                packages.append(f"{os.popen('pacman -Q | wc -l').read()} (pacman)".replace("\n", ""))
            case "apt":
                packages.append(f"{os.popen('apt list --installed | wc -l').read()} (apt)".replace("\n", ""))
            case "dnf":
                packages.append(f"{os.popen('dnf list --installed | wc -l').read()} (dnf)".replace("\n", ""))
            case "flatpak":
                packages.append(f"{os.popen('flatpak list | wc -l').read()} (flatpak)".replace("\n", ""))
            case "snap":
                packages.append(f"{os.popen('snap list | wc -l').read()} (snap)".replace("\n", ""))
            case "packagekit":
                packages.append(f"{os.popen('pkcon get-packages -p | grep Installed | wc -l').read()} (packagekit)".replace("\n", ""))
            case _:
                packages.append("0 (Unknown)")

    for i in range(len(packages)):
        if i == len(packages) - 1:
            result += f"{packages[i]}"
        else:
            result += f"{packages[i]}, "

    return result
