import subprocess
import shlex
import threading

def worker():
	proc = subprocess.Popen(shlex.split('gifview -a cat.gif'))
	proc.communicate()

t = threading.Thread(target = worker)
t.daemon = True
t.start()

t.join()
