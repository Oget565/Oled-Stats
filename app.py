import psutil

cpu = psutil.cpu_percent()
ram_per = psutil.virtual_memory().percent
disk = psutil.disk_usage("/").percent

def main():
    while True:
        print(f"Cpu: {cpu}, Ram: {ram_per}, Disk {disk}")

main()    