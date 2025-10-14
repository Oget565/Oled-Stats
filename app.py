from luma.core.interface.serial import i2c, spi, pcf8574
from luma.core.interface.parallel import bitbang_6800
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1309, ssd1325, ssd1331, sh1106, sh1107, ws0010
import psutil
import socket
import time

serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)

#DISPLAY SIZE IS 128*64

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
    
#IN DEVELOPMENT!!!!
def display_oled(c, r, d, t, i):
    with canvas(device) as draw:
        draw.text((0,0), f"CPU: {c}%", fill="white")
        draw.text((0,10), f"RAM: {r}%", fill="white")
        draw.text((0,20), f"DISK: {d}%", fill="white")
        draw.text((0,30), f"TEMP: {t}%", fill="white")
        draw.text((0,40), f"IP: {i}", fill="white")


def main():
    while True:
        cpu = psutil.cpu_percent()
        ram_per = psutil.virtual_memory().percent
        disk = psutil.disk_usage("/").percent
        temp = get_temp()
        ip = get_ip()
        
        print(f"Cpu: {cpu}%, Ram: {ram_per}%, Disk {disk}%, IP: {ip}, Temp: {temp}C")
        display_oled(cpu, ram_per, disk, temp, ip)
        time.sleep(1)


main()    