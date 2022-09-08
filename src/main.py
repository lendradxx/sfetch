from lib.system import GetDistroName, GetHostname, GetKernelInfo, GetMemoryInfo, GetOSType, GetUserType, GetUsername
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
    ram = f"RAM: {ramInfo['used']} MB / {ramInfo['total']} MB ({ramUsagePercent:.0f}%)"
    swap = f"SWAP: {swapInfo['used']} MB / {swapInfo['total']} MB ({swapUsagePercent:.0f}%)"
    lineLength = max([len(title), len(os), len(kernel), len(ram), len(swap)])

    headerLength = f"{GenerateLine('─', int(lineLength/2))}[ I use {GetDistroName()} btw ]{GenerateLine('─', int(lineLength/2))}"

    # Prompt Result
    print(
        f"┌{GenerateLine('─', int(lineLength/2))}[ I use {Style.BRIGHT}{Fore.MAGENTA}{GetDistroName()}{Style.RESET_ALL} btw ]{GenerateLine('─', int(lineLength/2))}┐",
        f"├─ {Style.BRIGHT}{Fore.LIGHTWHITE_EX}User{Style.RESET_ALL}: {GetUsername()}@{GetHostname()} ({GetUserType()})",
        f"├─ {Style.BRIGHT}{Fore.LIGHTBLUE_EX}OS{Style.RESET_ALL}: {GetOSType()} ({GetDistroName()})",
        f"├─ {Style.BRIGHT}{Fore.GREEN}Kernel{Style.RESET_ALL}: {GetKernelInfo()}",
        f"├─ {Style.BRIGHT}{Fore.CYAN}RAM{Style.RESET_ALL}: {Style.BRIGHT}{Fore.RED}{ramInfo['used']}{Style.RESET_ALL} MB / {Style.BRIGHT}{Fore.GREEN}{ramInfo['total']}{Style.RESET_ALL} MB ({ramUsagePercent:.1f}%)",
        f"├─ {Style.BRIGHT}{Fore.YELLOW}Swap{Style.RESET_ALL}: {Style.BRIGHT}{Fore.RED}{swapInfo['used']}{Style.RESET_ALL} MB / {Style.BRIGHT}{Fore.GREEN}{swapInfo['total']}{Style.RESET_ALL} MB ({swapUsagePercent:.1f}%)",
        f"└{GenerateLine('─', len(headerLength))}┘",
        sep="\n",
    )
