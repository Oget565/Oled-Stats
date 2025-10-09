import psutil
import socket
import time

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]

        if ip == "127.0.0.1":
            return "N/A"

    except Exception:
        ip = "N/A"
    finally:
        s.close()
    return ip

def get_temp():
    try:
        temps = psutil.sensors_temperatures()
        
        if 'coretemp' in temps:
            for entry in temps['coretemp']:
                if 'Package id 0' in entry.label:
                    return round(entry.current, 1)
        
        for name, entries in temps.items():
            if entries:
                return round(entries[0].current, 1)
        
        return None
    except Exception as e:
        print(f"Error reading temperature: {e}")
        return None

def main():
    while True:
        cpu = psutil.cpu_percent()
        ram_per = psutil.virtual_memory().percent
        disk = psutil.disk_usage("/").percent
        temp = get_temp()
        ip = get_ip()
        
        print(f"Cpu: {cpu}%, Ram: {ram_per}%, Disk {disk}%, IP: {ip}, Temp: {temp}C")
        time.sleep(1)

main()    