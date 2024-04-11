from flask import Flask, render_template
import platform
import psutil
import socket

app = Flask(__name__)

@app.route('/')
def index():
    # Get hardware details
    processor = platform.processor()
    architecture = platform.architecture()[0]
    machine = platform.machine()
    cores = psutil.cpu_count(logical=False)
    threads = psutil.cpu_count(logical=True)
    total_memory = round(psutil.virtual_memory().total / (1024 ** 3), 2)
    available_memory = round(psutil.virtual_memory().available / (1024 ** 3), 2)
    network_interfaces = psutil.net_if_addrs()

    # Get software details
    python_version = platform.python_version()
    hostname = socket.gethostname()
    system = platform.system()
    release = platform.release()

    return render_template('index.html', processor=processor, architecture=architecture, machine=machine,
                           cores=cores, threads=threads, total_memory=total_memory, available_memory=available_memory,
                           network_interfaces=network_interfaces, python_version=python_version, hostname=hostname,
                           system=system, release=release)

if __name__ == '__main__':
    app.run(debug=True)
