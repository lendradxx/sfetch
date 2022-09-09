import os, psutil, platform
from xml.etree.ElementInclude import include


def GetUsername():
    return os.getenv("USER")


def GetHostname():
    return os.popen("hostname").read().replace("\n", "")


def GetKernelInfo():
    return platform.release()


def GetDistroName():
    return platform.freedesktop_os_release()["NAME"]


def GetParentDistro():
    if not platform.freedesktop_os_release()["ID_LIKE"]:
        return

    return platform.freedesktop_os_release()["ID_LIKE"].capitalize()


def GetDistroColor():
    return platform.freedesktop_os_release()["ANSI_COLOR"]


def GetOSType():
    return platform.system()


def GetUserType():
    user_id: str = os.popen("id").read()

    if not user_id.find("wheel"):
        return "Standard"

    return "Admin"


def GetPackagesInfo():
    pass


def GetMemoryInfo():
    RawRAM = os.popen('free -t -m | grep "Mem"').read().split(" ")
    RawRAM = list(filter(None, RawRAM))
    RawSwap = os.popen('free -t -m | grep "Swap"').read().split(" ")
    RawSwap = list(filter(None, RawSwap))

    return {
        "ram": {
            "total": RawRAM[1],
            "used": RawRAM[2],
            "free": RawRAM[3],
            "shared": RawRAM[4],
            "buff": RawRAM[5],
            "available": RawRAM[6],
        },
        "swap": {
            "total": RawSwap[1],
            "used": RawSwap[2],
            "free": RawSwap[3],
        },
    }
