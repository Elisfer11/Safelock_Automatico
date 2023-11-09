import os
user= os.getlogin()
os.system(f"sudo cp /home/{user}/SafeLock_Automatico/Opciones/Automatizacion_completa.py /home/{user}/SafeLock_Automatico/Opciones/Automatizacion_pi-hole.sh /home/{user}/SafeLock_Automatico/Opciones/teamviewer-host_15.47.3_arm64.deb /home/{user}/")

os.system(f"sudo python3 /home/{user}/Automatizacion_completa.py")

os.system(f"sudo rm /home/{user}/Automatizacion_completa.py /home/{user}/Automatizacion_pi-hole.sh")
