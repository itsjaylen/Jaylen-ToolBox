from pymitter import EventEmitter

# https://github.com/durai145/MiningSetupUbuntu/blob/cd90f9795da7737200047a6361f7cd0b36fa7e3c/neo/neo-python-master/neo/EventHub.py

events = EventEmitter(wildcard=True)

def dispatch(event):
    events.emit(event)
    
@events.on("process_listen")
def listen():
    pass