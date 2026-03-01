#  Komodo Ole Runners Club Project

Based off https://www.pipelinegames.com/products/storm-chaser-simulator

TODO: verified power supply current draw is 


## User Front End
- One wireless remote control and two black buttons to activate 1 or 3 second cold air bursts
- 
- Magnetic switch to turn on red LED buttons when door closes, and turn off fans when door opens


## Control Back End
- Engineering GUI to adjust fan burst length and emergency fan on/off switch
- Raspberry Pi is controllable from any laptop using https://connect.raspberrypi.com/sign-in with BitWarden login username & password  

## Notes for Manufacturing Hardware at Shop
1. Air flows out of the sticker side of all 5 fans on all  4 Thermoelectric Cooling Units (202-00003-A). See black arrows in Figure 1 for hot and cold side air flow directions.
2. Drill 3/16 inch hole in the plastic plate in between the cooling units to insert the two pair of thinner upper fan wires downwards (towards the radiators.) 
3. Feed two pair of thicker upper chiller wires downwards (towards the radiators), under the foam padding.
3. See figure 2 for air flow direction of the static ducted fans. The power cord should be above the speed controller port when installed for air to flow upwards.
4. Slide two halves of the cooling unit plates together to allow cooling unit to mount to internal frame.
5. Dont put the Outer Back Foam pieces onto 1st and 2nd Stage Cooling Chambers until 1st and 2nd stage are bolted together.
6. The PL300 FoamBoard Construction Adhesive takes 24 to fully set up. Foam should not be moved until it is fully set.

## Assemble Hardware on Site
1. Plug L5-30P extension cord #1 to #4 into generator
2. Connect Raspberry Pi 5, HDMI display, and white overhead LED to L5-30P plug #1
3. Connect Fan #1 and Fan #2 to L5-30P plug #2
4. Connect AC to DC Invertor #1 and AC to DC Invertor #2 to L5-30P plug #3
5. Connect AC to DC Invertor #2 and AC to DC Invertor #4 to L5-30P plug #4
6. Adjust steel swivel leveling mounts to ensure stability and proper alignment for door opening and closing
7. The black TerraBloom wireless controller with white tape and letter P is the main controller for the system. The 2nd controller is unpaired, but can be used for backup purposes if battery on the main controller is low.

https://erayakpower.com/products/8000w-inverter-generator-whole-home-backup?variant=48276282638541&country=US&currency=USD&gad_campaignid=23378001586&gbraid=0AAAAAoI-_ZIQ9hAid7tx-dPsSlYFyiCvp

https://www.jackery.com/products/jackery-explorer-5000-plus-series?variant=41336307449943

https://www.homedepot.com/p/Westinghouse-18-000-14-500-Watt-Dual-Fuel-Gas-and-Propane-Portable-Generator-with-Remote-Electric-Start-Low-THD-and-50-Amp-Outlet-WGen14500DFc/318062122?g_store=3315&source=shoppingads&locale=en-US&fp=ggl


## Setup Software on New Raspberry Pi
1. Make sure keyboard is connected to Raspberry Pi
2. Make sure touch display is connected to Raspberry Pi and showing Desktop after booting up
3. Make sure Raspberry Pi is connected to the internet via Ethernet or Wi-Fi
  * nmcli device wifi connect "Blaze's iPhone" password "Ironman@42"
4. Run the SetupOleRunnersClub.sh in Raspberry Pi terminal (Open with Ctrl + Alt + T):
```
cd ~/6919_komodo_ole-runners-club
chmod +x SetupOleRunnersClub.sh
sudo ./SetupOleRunnersClub.sh
```

## GUI User Manual
1. Fan Duration (seconds) has three options, and sets how long the air burst will last when ACTION button is pressed.
2. Fan Speed (%) has four options, and sets percentage of maximum speed (288 cubic feet per minute) of fans when they are running.
3. Red Button LED Brightness is a continous slider (0 to 100%), and sets brightness of ACTION button LED.
4. TURN ON FANS: Press this button to turn on fans continuously (Air will start warming up after about 9 seconds of continuous operation).
5. TURN OFF FANS: Press this button to turn off fans immediately (e.g. emergency like person wanting to leave wind chamber)


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
