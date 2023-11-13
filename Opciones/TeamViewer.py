import os

user = os.getlogin()

os.system(f"sudo cp /home/safelock/Safelock_Automatico/Opciones/teamviewer-host_15.47.3_arm64.deb /home/{user}")

os.system("sudo apt-get install -y ./teamviewer-host_15.47.3_arm64.deb")

os.system (f"sudo rm /home/{user}/teamviewer-host_15.47.3_arm64.deb")
