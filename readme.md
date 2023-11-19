# AHS Broward Hackathon: 11/17/23 5pm - 11/18/23 8:30am
### Winning Team: Victor Jafet, Daniel Heit, Michael Wang
### This is the code from our winning hackathon project.
## Below is a short description of what each file is:
- final.py: the final Python (laptop side) code exactly as it was run during the scoring, which is the combined version of the two other python files:
    - cameraOnly.py: the standalone camera code that is entirely Michael's doing. Michael spent the whole time working on this. 
    - movementOnly.py: the standalone movement code that is entirely my doing. I spent the last 2 hours or so working on this file to code the movements for each possible permutation.
- serialcommsatt/serialcommsatt.ino: the final Arduino C (mBot side) code exactly as it was run during the scoring (serialcommsatt stands for "Serial Communications Attempt" because the file was originally meant to be used just for testing serial communication). This file recieved communications from the computer through serial signals, which could be sent over the provided bluetooth dongle. It would then execute a certain action based on the signal, so overall, the computer would control the order of actions while all the mBot did was recieve signals and perform corresponding actions.
