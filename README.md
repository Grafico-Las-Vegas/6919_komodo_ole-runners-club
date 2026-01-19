#  Komodo Ole Runners Club Project


## User Front End
- Two red buttons with LED backlight to activate the cold air bursts
- Magnetic switch to turn on red LED buttons when door closes, and turn off fans when door opens


## Control Back End
- Engineering GUI to adjust fan burst length, over head white LED brightness, and emergency fan on/off switch
- Raspberry Pi is controllable from any laptop using https://connect.raspberrypi.com/sign-in with BitWarden login username & password  


## Assemble Hardware on Site
1. Plug L5-30P extension cord #1 to #4 into generator
2. Connect Raspberry Pi 5, HDMI display, and white LED to L5-30P plug #1
3. Connect Fan #1 and Fan #2 to L5-30P plug #2
4. Connect AC to DC Invertor #1 and AC to DC Invertor #2 to L5-30P plug #3
5. Connect AC to DC Invertor #2 and AC to DC Invertor #4 to L5-30P plug #4
6. Adjust steel swivel leveling mounts to ensure stability and proper alignment for door opening and closing


## Setup Software on New Raspberry Pi
1. Make sure keyboard is connected to Raspberry Pi
2. Make sure touch display is connected to Raspberry Pi and showing Desktop after booting up
3. Make sure Raspberry Pi is connected to the internet via Ethernet or Wi-Fi
4. Run the SetupOleRunnersClub.sh in Raspberry Pi terminal (Open with Ctrl + Alt + T):
```
cd ~/6919_komodo_ole-runners-club
chmod +x SetupOleRunnersClub.sh
sudo ./SetupOleRunnersClub.sh
```


## Test System Prior to Event
- As user enters wind chamber and closes the door, LED buttons should turn on
- When a user presses either of the two buttons, fans turn on for a set time and LED buttons turn off
- Any time a user leaves wind chamber by opening the door, LED buttons turn off and fans turn off immediately


## FAQ's
1. Why is the Raspberry Pi not controllable from an external laptop?
- Make sure Raspberry Pi and laptop are connected to the internet, and Raspberry Pi Connect software is running.
2. Why is SetupOleRunnersClub.sh not running, and displaying "permission denied: ./SetupApplication.sh" error message?
- Make sure you have the correct permissions to run the script. You can check the permissions by running the command `ls -l SetupOleRunnersClub.sh`. If the permissions are not set correctly, you can change them by running the command `chmod +x SetupOleRunnersClub.sh`.
3. Why are the LED buttons not turning on when the door is closed?
- Make sure the door sensor is properly aligned and close enough to the square magnetic on the door.
