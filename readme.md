# AHS Broward Hackathon: 11/17/23 5pm - 11/18/23 8:30am
### Winning Team: Victor Jafet, Daniel Heit, Michael Wang
### This repository contains all the code from our winning hackathon project.

## Below is a short description of what each file is:
- final.py: the final Python (laptop side) code exactly as it was run during the scoring, which is the combined version of the two other Python files:
    - cameraOnly.py: the standalone camera code that is entirely Michael's doing. Michael spent the whole time working on this. 
    - movementOnly.py: the standalone movement code that is entirely my doing. I spent the last 2 hours or so working on this file to code the movements for each possible permutation.
- serialcommsatt/serialcommsatt.ino: the final Arduino C (mBot side) code exactly as it was run during the scoring (serialcommsatt stands for "Serial Communications Attempt" because the file was originally meant to be used just for testing serial communication). This file recieved communications from the computer through serial signals, which could be sent over the provided bluetooth dongle. It would then execute a certain action based on the signal, so overall, the computer would control the order of actions while all the mBot did was recieve signals and perform corresponding actions.

## Requirements and loading/running code 
- Make sure you have the Arduino IDE software properly installed.
- You should have an mBot that is assembled correctly and properly connected to the host computer through a bluetooth dongle for code pushing and serial communications
- Of course, you need the same arm design that we had on our robot which includes the servo being connected the same way, but since this is impossible to replicate without another 3 pages of explanation, the movement alone should function fine even if you're missing an arm (just remove everything having to do with a servo).
1. Load the .ino file into the Arduino IDE and connect to your mBot under the "Arduino Uno" board (the port was COM3 for us)
2. Verify and upload the code to the bot. From the toolbar at the top of the Arduino IDE select Tools -> Serial Monitor
3. Open the Python laptop side code and split screen it with your Arduino IDE window (this is important since the only way we could get Python to do serial writes was through using pyautogui to input values in the serial input box in the Arduino IDE)
4. Replace the mouse coordinates in "pyautogui.click()" with the coordinates of the input box of the serial monitor so that it is selected once the program is started
5. Run the Python program, and in the terminal input the order in which the robot is to contact the bars (1 being the lowest/closest bar, 2 being the medium/2nd closest bar, and 3 being the highest/furthest bar). (Ex. inputting "123" would go low medium high)
6. Press enter one last time to begin the program and watch it happen.
7. After the movement portion of the program is complete, ensure that your webcam (which you should also ensure is correct selected in the code) is facing the track from behind where the robot began. Give it 15 seconds to run, and once it detects green/pink at the same time, it will print an output of what it thinks is the correct order is.

### In the future, I might add more details about the design, scoring, etc so that this project is fully replicable. Hopefully this at least provides some insight to the strategies I used to make the robot successfully communicate with my laptop and move correctly.
#### If they ever happen to see this, I would like to state my appreciation for Mrs. Behar, Mrs. Demosthenes, Mr. Salafia, and especially Mr. Rivero for their support throughout the hackathon. They gave me encouraging words throughout the night and have helped me challenge myself in CS/Engineering in general. Much more still lies ahead. Thank you all very much!
#### And of course, Michael, Daniel, thanks for being part of the dream team. I'm finally gonna go pass out now.