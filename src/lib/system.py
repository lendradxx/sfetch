import platform


class User:
    """
    Class user include information about user account on the system,\n
    such like username, hostname, account type, group, and many more
    """

    def __init__(self, sep: str = ":") -> None:
        self.sep = sep
        pass

    def Generate(self):
        pass


class Software:
    """
    Class software include information about software on the system,\n
    suck like distro name, kernel version, total installed package, and many more
    """

    def __init__(self) -> None:
        pass

    def Generate(self):
        pass


class Hardware:
    """
    Class hardware include information about hardware on the system,\n
    suck like ram, model/vendor, storage, cpu, gpu and many more
    """

    def __init__(self) -> None:
        pass

    def Generate(self):
        pass
