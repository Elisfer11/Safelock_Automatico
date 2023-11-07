#!/bin/bash
xdotool key Control+Alt+t
sleep 4
xdotool type "sudo curl -sSL https://raw.githubusercontent.com/pi-hole/pi-hole/master/automated%20install/basic-install.sh | bash"
xdotool key Return
sleep 1 
#xdotool type "odroid"
#xdotool key Return
sleep 180
xdotool key Return
sleep 1
xdotool key Return
sleep 1
xdotool key Left
sleep 1
xdotool key Return
sleep 1
xdotool key Return
sleep 1
xdotool key Return
sleep 1
xdotool key Return
sleep 1
xdotool key Return
sleep 1
xdotool key Return
sleep 1
xdotool key Return
sleep 1
xdotool key Return
sleep 300
xdotool key Return
sleep 5
xdotool type "exit"
xdotool key Return

