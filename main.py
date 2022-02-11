import modules
import os

from modules.menu import command_handler


folders = ["data", "./data/logs"]

def main():
    try:
        os.system(f"title loaded version {modules.Settings.version}")
        for folder in folders:
            if not os.path.exists(folder):
                os.mkdir(folder)
        command_handler()
    except Exception:
        pass
    
if __name__ == "__main__":
    main()
