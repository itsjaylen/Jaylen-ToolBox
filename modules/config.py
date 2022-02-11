from colorama import init

from modules.installer import install_packages
from modules.listeners.optimizing.optimizer import optimize
from .debugging import LogDebugger


class Settings(object):
    """Configurations"""

    def __init__(self):
        self.todo = []
        self.version = "1.1"
        self.appname = "Jaylen Toolbox"
        self.debug = True
        self.color = init(autoreset=True, convert=True)
        self.processes = ["YourPhone.exe", "LockApp.exe", "OriginWebHelperService.exe", "msedgewebview2.exe", "Microsoft.Photos.exe"]


class Commands(object):
    """Commands list"""

    def __init__(self):
        self.command_list = ["help",
                             "clearlogs",
                             "installer",
                             "ChocolateyInstaller",
                             "AutoOptimizer",
                             
                             ]

        self.command_dict = {"help": self.help,
                             "clearlogs": LogDebugger.ClearLogs,
                             "installer": install_packages,
                             "chocolatey": None,
                             "AutoOptimizer": optimize,
                             
                             }

    def help(self):
        sorted_command_list = sorted(self.command_list[1:], key=str.lower)
        print("\n".join(sorted_command_list), sep="\n")


Settings = Settings()
Commands = Commands()
