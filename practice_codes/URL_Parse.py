import socket
import time
import threading

from queue import Queue

qurl="www.facebook.com"
url = input('Enter the url site to check: ')
print("IP:",socket.gethostbyname(url))
result=socket.gethostbyname(url)

socket.setdefaulttimeout(0.25)
print_lock = threading.Lock()

target = result
t_IP = socket.gethostbyname(target)
print('Starting scan on host: ', t_IP)


def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((t_IP, port))
        with print_lock:
            print(port, 'is open')
        con.close()
    except:
        pass


def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()


q = Queue()
startTime = time.time()

for x in range(100):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in range(1, 60000):
    q.put(worker)

q.join()
print('Time taken:', time.time() - startTime)