import os
import subprocess
import time

#Update del sistema
os.system("sudo apt-get update")

#Instalar Pi-hole
os.system("sudo curl -sSL https://raw.githubusercontent.com/OpenLock20/SL-MASTER-PRODUCT/master/automated%20install/basic-install.sh | bash")
new_password = "safelock"
os.system(f'echo "{new_password}\n{new_password}" | sudo pihole -a -p')


time.sleep(5)
os.system("sudo rm -r /var/www/html/admin/")
os.system("sudo git clone --depth 1 https://github.com/OpenLock20/SL-INTERFACE-PRODUCT /var/www/html/admin")

#Instala Yersinia
os.system("sudo apt install -y yersinia")

#Instala dependencias para el envio de correos
os.system("sudo apt-get install -y python3-pip")

os.system("pip3 install requests")

#Permisos para los archivos
archivos = [
    "/var/www/html/admin/scripts/pi-hole/php/CORREO/configuracion_correo.txt",
    "/var/www/html/admin/scripts/pi-hole/php/CORREO/correo_almacenado.txt",
	"/var/www/html/admin/estadisticas/stats/consultas_bloqueadas.txt",
	"/var/www/html/admin/estadisticas/stats/dominios_en_listas.txt",
	"/var/www/html/admin/estadisticas/stats/porcentaje_bloqueo.txt",
	"/var/www/html/admin/estadisticas/stats/consultas_totales.txt",
	"/var/www/html/admin/pull.sh"

]

for archivo in archivos:
    os.chmod(archivo, 0o777)
    print(f"Permisos cambiados a 777 para {archivo}.")


#Actualiza Crontabs
cronjob = '* * * * * python3 /var/www/html/admin/crontab_conf.py\n'
with open('/tmp/cronjob', 'w') as cronfile:
    cronfile.write(cronjob)
subprocess.call(['sudo', 'crontab', '/tmp/cronjob'])
print("Crontabs Creados.")


#Cambia nombre del equipo a safelock
host_name = "safelock"
with open('/etc/hostname', 'w') as host_file:
    host_file.write(host_name)



#instalacion del Chromium-Browser
os.system("sudo apt install -y chromium-browser")




#Instalacion TeamViewer
user = os.getlogin()

os.system(f"sudo python3 /home/{user}/Safelock_Automatico/TeamViewer/TeamViewer.py")

#Se cambia de Wayland a Xorg
remove_wayland = f"WaylandEnable=false"
with open('/etc/gdm3/custom.conf', 'a') as host_file:
    host_file.write(remove_wayland)




#time.sleep(30)

#os.system("systemctl restart gdm")

print ("*********************************************************")
print ("El SafeLock ya está listo")
print ("Para que toda la configuración tenga efecto se deberá reiniciar el SafeLock")

