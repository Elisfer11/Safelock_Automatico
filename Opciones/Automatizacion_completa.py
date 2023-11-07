import os
import subprocess
user = os.getlogin()

# Verifica si el usuario tiene permisos de superusuario
# Actualiza el sistema
os.system("sudo apt update")
    
#Libreria que interactua con el sistema
os.system("sudo apt-get install -y xdotool")

# Descarga e instala Pi-hole

os.system("./Automatizacion_pi-hole.sh")
#cambiar contra
new_password = "safelock"
os.system(f'echo "{new_password}\n{new_password}" | sudo pihole -a -p')

# Cambiar al directorio /var/www/html y realizar operaciones
os.system("sudo rm -r /var/www/html/admin/")
os.system("sudo git clone --depth 1 https://github.com/Elisfer11/prueba_interfaz.git /var/www/html/admin")

# Instala Yersinia
os.system("sudo apt install -y yersinia")


print("Configuración de Pi-hole y safelock completada, y el repositorio git ha sido clonado.")

#Configura la tarea cron para ejecutar el script cada minuto en el crontab de root
cronjob = '* * * * * python3 /var/www/html/admin/automatizacion.py\n0 3 * * * /var/www/html/admin ; git pull\n'
with open('/tmp/cronjob', 'w') as cronfile:
    cronfile.write(cronjob)
subprocess.call(['sudo', 'crontab', '/tmp/cronjob'])
print("Tareas configuradas.")


#Instalacion TeamViewer
os.system("sudo apt install ./teamviewer-host_15.47.3_arm64.deb")
