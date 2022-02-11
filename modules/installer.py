import os
from .utils import Events

# BETA PROB NOT WORKING IDK


APPLICATIONS = {"Discord": None, "Chrome": None, "Visual Studio Code": None,
                "Visual Studio": None, "Sharex": None, "Files": None, "Process Hacker 2": None, }
GAME_LAUNCHERS = {"Rockstar": None, "Steam": None, "Blizzard": None}
SOFTWARE_PACKAGES = {"Nvidia GeForce Experience": None, "Java": None,}


def install_packages(Chocolatey=False):
    if Chocolatey == True:
        Events.elevate()
        for Package in APPLICATIONS:
            os.system(f"choco install {Package} -y")
        
