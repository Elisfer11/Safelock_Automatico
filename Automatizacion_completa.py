import os
user= os.getlogin()
os.system(f"sudo cp /home/{user}/SafeLock_Automatico/Opciones/Automatizacion_completa.py /home/{user}/SafeLock_Automatico/Opciones/Automatizacion_pi-hole.sh /home/{user}/")

os.system(f"sudo python3 /home/{user}/Automatizacion_completa.py")

os.system(f"sudo rm /home/{user}/Automatizacion_completa.py /home/{user}/Automatizacion_pi-hole.sh")
