import os
import subprocess

#Update del sistema
os.system("sudo apt-get update")

#Instalar Pi-hole
os.system("sudo curl -sSL https://raw.githubusercontent.com/OpenLock20/SL-MASTER-PRODUCT/master/automated%20install/basic-install.sh | bash")
new_password = "safelock"
os.system(f'echo "{new_password}\n{new_password}" | sudo pihole -a -p')

os.system("sudo rm -r /var/www/html/admin/")
os.system("sudo git clone --depth 1 https://github.com/OpenLock20/SL-INTERFACE-PRODUCT /var/www/html/admin")

#Instala Yersinia
os.system("sudo apt install -y yersinia")

#Instala dependencias para el envio de correos
os.system("sudo apt-get install python3-pip")

os.system("pip3 install requests")


#Configura el crontab
cronjob = '* * * * * python3 /var/www/html/admin/new_crontab.py\n'
with open('/tmp/cronjob', 'w') as cronfile:
    cronfile.write(cronjob)
subprocess.call(['sudo', 'crontab', '/tmp/cronjob'])
print("Tareas configuradas.")



#Quita la suspencion automatica
os.system("gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-ac-timeout 0")


#Instalacion TeamViewer

user = os.getlogin()

os.system(f"sudo python3 /home/{user}/Safelock_Automatico/Opciones/TeamViewer.py")

os.system("ip address")
