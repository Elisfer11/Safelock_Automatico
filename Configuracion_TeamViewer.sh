#!/bin/bash
xdotool key Control+Alt+t
sleep 4
xdotool type "teamviewer"
xdotool key Return
sleep 10
xdotool key Tab
sleep 1
xdotool key Tab
sleep 1
xdotool key Return
sleep 1
xdotool key Tab
sleep 1
xdotool key Return
sleep 1
xdotool key Tab
sleep 1
xdotool key Down
sleep 1
xdotool key Tab
sleep 1
xdotool key Tab
sleep 1
xdotool key Down
sleep 1
xdotool key Down
sleep 1
xdotool key Tab
sleep 1
xdotool key Tab
sleep 1
xdotool key Tab
sleep 1
xdotool key Tab
sleep 
xdotool key Tab
sleep 1
xdotool key Return
sleep 1
xdotool key Tab
sleep 1
xdotool key Down
sleep 1
xdotool key Down
sleep 1
xdotool key Tab
sleep 1
xdotool key Tab
sleep 1
xdotool key Tab
sleep 1
xdotool key Tab
sleep 1
xdotool key Tab
sleep 1
xdotool key Tab
sleep 1
xdotool type "SafeLock1."
sleep 1
xdotool key Tab
sleep 1
xdotool type "SafeLock1."
sleep 1
repeticiones_tab=23

# Realiza un bucle para presionar la tecla Tab 23 veces
for ((i=0; i<$repeticiones_tab; i++))
do
  sleep 1
  xdotool key Tab
done

sleep 1
xdotool key Return 
sleep 1
xdotool key Alt+F4


