import os
import subprocess

# Verifica si el usuario tiene permisos de superusuario
if os.geteuid() != 0:
    print("Este script debe ejecutarse como superusuario (root).")
    exit(1)
else:
    # Actualiza el sistema
    os.system("sudo apt update")

    # Descarga e instala Pi-hole
    os.system("sudo curl -sSL https://raw.githubusercontent.com/OpenLock20/SL-MASTER-PRODUCT/master/automated%20install/basic-install.sh | bash")
    #cambiar contra
    new_password = "safelock"
    os.system(f'echo "{new_password}\n{new_password}" | sudo pihole -a -p')

    # Cambiar al directorio /var/www/html y realizar operaciones
    os.system("sudo rm -r /var/www/html/admin/")
    os.system("sudo git clone --depth 1 https://github.com/OpenLock20/SL-INTERFACE-PRODUCT /var/www/html/admin")

    # Instala Yersinia
    os.system("sudo apt install -y yersinia")

    print("Pi-hole y Yersinia se han instalado correctamente.")



print("Configuración de Pi-hole y safelock completada, y el repositorio git ha sido clonado.")

#Configura la tarea cron para ejecutar el script cada minuto en el crontab de root
cronjob = '* * * * * python3 /var/www/html/admin/scripts/pi-hole/php/CORREO/crontab_correo.py\n* * * * * python3 /var/www/html/admin/new_crontab.py\n'
with open('/tmp/cronjob', 'w') as cronfile:
    cronfile.write(cronjob)
subprocess.call(['sudo', 'crontab', '/tmp/cronjob'])
print("Tareas configuradas.")



#Instalacion TeamViewer

os.system("gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-ac-timeout 0")


user = os.getlogin()

os.system(f"sudo python3 /home/{user}/Safelock_Automatico/Opciones/TeamViewer.py")

os.system("ip address")
