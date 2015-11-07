from threading import Thread, Event
import time

def countdown(n, started_evt): 
    print('countdown starting') 
    started_evt.wait()
    while n > 0:
        print('T-minus', n) 
        n -= 1 
        time.sleep(1)

started_evt = Event()

print('Launching countdown')
t = Thread(target=countdown, args=(5,started_evt)) 
t.start()        

print " waiting"
time.sleep(5)
print "end wait"
started_evt.set() 
print('countdown is running')

