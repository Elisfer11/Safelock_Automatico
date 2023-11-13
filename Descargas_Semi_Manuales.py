import os
import subprocess

# Verifica si el usuario tiene permisos de superusuario
if os.geteuid() != 0:
    print("Este script debe ejecutarse como superusuario (root).")
    exit(1)
else:
    # Actualiza el sistema
    os.system("sudo apt update") 

    #Libreria que interactua con el sistema
    os.system("sudo apt-get install -y xdotool")


    # Descarga e instala Pi-hole
    os.system("sudo curl -sSL https://raw.githubusercontent.com/pi-hole/pi-hole/master/automated%20install/basic-install.sh | bash")
    #cambiar contra
    new_password = "safelock"
    os.system(f'echo "{new_password}\n{new_password}" | sudo pihole -a -p')

    # Cambiar al directorio /var/www/html y realizar operaciones
    os.system("sudo rm -r /var/www/html/admin/")
    os.system("sudo git clone --depth 1 https://github.com/Elisfer11/prueba_interfaz.git /var/www/html/admin")

    # Instala Yersinia
    os.system("sudo apt install -y yersinia")

    print("Pi-hole y Yersinia se han instalado correctamente.")



print("Configuración de Pi-hole y safelock completada, y el repositorio git ha sido clonado.")

#Configura la tarea cron para ejecutar el script cada minuto en el crontab de root
cronjob = '* * * * * python3 /var/www/html/admin/automatizacion.py\n0 3 * * * /var/www/html/admin ; git pull\n'
with open('/tmp/cronjob', 'w') as cronfile:
    cronfile.write(cronjob)
subprocess.call(['sudo', 'crontab', '/tmp/cronjob'])
print("Tareas configuradas.")


#Instalacion TeamViewer
user = os.getlogin()

os.system(f"sudo python3 /home/{user}/Safelock_Automatico/Opciones/TeamViewer.py")

os.system("ip address")
