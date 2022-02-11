import os
import glob
import logging

class LogDebugger(object):
    def ClearLogs(self):
        LOG_PATH = f"{os.getcwd()}/data/logs"
        for log in glob.glob(f"{LOG_PATH}*.log"):
            print(log)
            with open(log), "r+" as f:
                try:
                    f.truncate(0)
                    print(f"Successfully cleared {log}")
                except Exception as e:
                    logging.DEBUG(e)
                    print(f"Failed to clear log {log} check logs for more info")
        
        
        
LogDebugger = LogDebugger()