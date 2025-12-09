#  Komodo Ole Runners Club Project

<<<<<<< HEAD
## User Front End
- Two red buttons with LED backlight to activate the cold air bursts
- Magnetic switch to turn on red LED buttons when door closes, and turn off fans when door opens
=======
## Hardware
- Raspberry Pi 5 
- GPIO Header
- 8 Channel Relay Module
- Button with LED
- Terrabloom EC Fan https://youtu.be/kluuL5dU2_Q?si=Ofyb_LtWS_kj8pzH
>>>>>>> 18faf57694f26441e46b4e905e85a3536f207c90

## Control Back End
- Engineering GUI to adjust fan burst length, over head white LED brightness, and emergency fan on/off switch
- Raspberry Pi is controllable from any laptop using https://connect.raspberrypi.com/sign-in with BitWarden login username & password  

## Assemble Hardware
1. Plug L5-30P extension cord #1 to #4 into generator
2. Connect Raspberry Pi 5, HDMI display, and white LED to L5-30P plug #1
3. Connect Fan #1 and Fan #2 to L5-30P plug #2
4. Connect AC to DC Invertor #1 and AC to DC Invertor #2 to L5-30P plug #3
5. Connect AC to DC Invertor #2 and AC to DC Invertor #4 to L5-30P plug #4

## Setup Raspberry Pi Software
1. Make sure keyboard is connected to Raspberry Pi
2. Make sure HDMI display is connected to Raspberry Pi
3. Run the SetupOleRunnersClub.sh in Raspberry Pi terminal (Open with Ctrl + Alt + T):
```
cd ~
sudo ./SetupOleRunnersClub.sh
```

## Test System
- As user enters wind chamber and closes door, LED buttons turn on
- When user presses either of two buttons, fans turn on for set time and LED buttons turn off
- Any time user leaves wind chamber and opens door, LED buttons turn off and fans turn off immediately


# FAQ's
1. How do I update the application?
2. Why is SetupOleRunnersClub.sh not running?
```
chmod +x install_komodo.sh
./SetupOleRunnersClub.sh
```
