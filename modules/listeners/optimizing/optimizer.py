import psutil
from elevate import elevate



def optimize():
    processes = []
    processes_pid = []
    amount = 0
    
    for proc in psutil.process_iter():
        try:
            processName = proc.name()
            processID = proc.pid
            amount += 1
            
            
            processes.append(str(processName))
            processes_pid.append(str(processID))
            
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
        
    elevate(show_console=True)
    print(amount)
    print(processes[6])
    print(processes_pid[6])