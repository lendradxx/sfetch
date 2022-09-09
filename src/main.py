from lib.packagemanager import GetPackageManagerList, GetTotalPackages
from lib.system import GetDistroColor, GetDistroName, GetHostname, GetKernelInfo, GetMemoryInfo, GetOSType, GetParentDistro, GetUserType, GetUsername
from utils.generator import GenerateLine
from colorama import Fore, Style

if __name__ == "__main__":
    ramInfo = GetMemoryInfo()["ram"]
    swapInfo = GetMemoryInfo()["swap"]
    ramUsagePercent = int(ramInfo["used"]) / int(ramInfo["total"]) * 100
    swapUsagePercent = int(swapInfo["used"]) / int(swapInfo["total"]) * 100
    # swapUsagePercent =

    title = f"USER: {GetUsername()}@{GetHostname()} ({GetUserType()})"
    os = f"OS: {GetOSType()} ({GetDistroName()})"
    kernel = f"Kernel: {GetKernelInfo()}"
    packages = f"Packages: {GetTotalPackages(GetPackageManagerList())}"
    ram = f"RAM: {ramInfo['used']} MB / {ramInfo['total']} MB ({ramUsagePercent:.0f}%)"
    swap = f"SWAP: {swapInfo['used']} MB / {swapInfo['total']} MB ({swapUsagePercent:.0f}%)"
    lineLength = max([len(title), len(os), len(kernel), len(ram), len(swap), len(packages)])

    headerLength = f"{GenerateLine('─', int(lineLength/2))}[ I use {GetParentDistro()} btw ]{GenerateLine('─', int(lineLength/2))}"

    # Prompt Result
    print(
        f"{Style.BRIGHT}\33[{GetDistroColor()}m┌{GenerateLine('─', int(lineLength/2))}{Style.RESET_ALL}[ I use {GetParentDistro()}{Style.RESET_ALL} btw ]{Style.BRIGHT}\33[{GetDistroColor()}m{GenerateLine('─', int(lineLength/2))}┐",
        f"{Style.BRIGHT}\33[{GetDistroColor()}m├─ User{Style.RESET_ALL}: {GetUsername()}@{GetHostname()} ({GetUserType()})",
        f"{Style.BRIGHT}\33[{GetDistroColor()}m├─ OS{Style.RESET_ALL}: {GetParentDistro()} {GetOSType()} ({GetDistroName()})",
        f"{Style.BRIGHT}\33[{GetDistroColor()}m├─ Kernel{Style.RESET_ALL}: {GetKernelInfo()}",
        f"{Style.BRIGHT}\33[{GetDistroColor()}m├─ Packages{Style.RESET_ALL}: {GetTotalPackages(GetPackageManagerList())}",
        f"{Style.BRIGHT}\33[{GetDistroColor()}m├─ RAM{Style.RESET_ALL}: {Style.BRIGHT}{Fore.RED}{ramInfo['used']}{Style.RESET_ALL} MB / {Style.BRIGHT}{Fore.GREEN}{ramInfo['total']}{Style.RESET_ALL} MB ({ramUsagePercent:.1f}%)",
        f"{Style.BRIGHT}\33[{GetDistroColor()}m├─ Swap{Style.RESET_ALL}: {Style.BRIGHT}{Fore.RED}{swapInfo['used']}{Style.RESET_ALL} MB / {Style.BRIGHT}{Fore.GREEN}{swapInfo['total']}{Style.RESET_ALL} MB ({swapUsagePercent:.1f}%)",
        f"{Style.BRIGHT}\33[{GetDistroColor()}m└{GenerateLine('─', len(headerLength))}┘",
        sep="\n",
    )
