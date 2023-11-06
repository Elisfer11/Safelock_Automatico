import os

os.system("sudo cp /home/odroid/SafeLock_Automatico/Opciones/Automatizacion_completa.py /home/odroid/SafeLock_Automatico/Opciones/Automatizacion_pi-hole.sh /home/odroid/")

os.system("sudo python3 /home/odroid/Automatizacion_completa.py")

os.system("sudo rm /home/odroid/Automatizacion_completa.py /home/odroid/Automatizacion_pi-hole.sh")
