import logging

from colorama import Fore

from modules.config import Commands

logging.basicConfig(format="%(asctime)s : %(name)s : %(funcName)s : %(module)s : %(message)s : %(threadName)s",
                    level=logging.DEBUG, filename="./data/logs/menu_logs.log")


def command_handler():
    while True:
        try:
            cmd = input("Type the command you want to run: ")

            if cmd not in Commands.command_list:
                logging.error(f"Command '{cmd}' not found")
                print(f"{Fore.RED}Command '{cmd}' not found")

            if cmd in Commands.command_list:
                try:
                    Commands.command_dict[cmd]()
                    logging.info(f"Command '{cmd}' found called successfully")
                except KeyError:
                    logging.error(f"Command: {cmd} not implemented.")
                    print("{Fore.RED}Error raised check logs for info")

        except Exception as e:
            logging.error(e)
            print("Error raised check logs for info")
            continue
