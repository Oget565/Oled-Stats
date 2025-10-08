import psutil
import socket
import time


def get_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def main():
    while True:
        cpu = psutil.cpu_percent()
        ram_per = psutil.virtual_memory().percent
        disk = psutil.disk_usage("/").percent
        
        print(f"Cpu: {cpu}, Ram: {ram_per}, Disk {disk}, IP: {get_ip()}")
        time.sleep(1)

main()    