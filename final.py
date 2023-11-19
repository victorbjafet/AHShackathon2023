
import pyautogui
from time import sleep

def write(char):
    pyautogui.write(char)
    pyautogui.press('enter')

order = input("order of the things (1 lowest, 2 mid, 3 high): ")
input()
pyautogui.click(1562,1111)

write('4')
sleep(1.5)

foot = 1.5

if order == "123":
    # print("the order is", returnVal[3], returnVal[2], returnVal[1])
    write('r')
    sleep(1.5)
    write('3')
    sleep(1.5)
    write('4')
    sleep(1.5)
    write('w')
    sleep(foot)
    write('q')
    sleep(1.5)
    write('0')
    sleep(5)
    write('2')
    sleep(1.5)
    write('5')
    sleep(1.5)
    write('4')
    sleep(1.5)
    write('w')
    sleep(foot)
    write('q')
    sleep(1.5)
    write('0')
    sleep(5)
    write('2')
    sleep(1.5)
    write('5')
    sleep(1.5)
    write('w')
    sleep(foot)
    write('q')
    sleep(1.5)
elif order == "132":
    # print("the order is", returnVal[3], returnVal[1], returnVal[2])
    write('r')
    sleep(1.5)
    write('3')
    sleep(1.5)
    write('4')
    sleep(1.5)
    write('w')
    sleep(foot*2)
    write('q')
    sleep(1.5)
    write('0')
    sleep(5)
    write('2')
    sleep(1.5)
    write('5')
    sleep(1.5)
    write('4')
    sleep(1.5)
    write('s')
    sleep(foot)
    write('q')
    sleep(1.5)
    write('0')
    sleep(5)
    write('2')
    sleep(1.5)
    write('5')
    sleep(1.5)
    write('w')
    sleep(foot*2)
    write('q')
    sleep(1.5)
elif order == "213":
    # print("the order is", returnVal[2], returnVal[3], returnVal[1])
    write('r')
    sleep(1.5)
    write('w')
    sleep(foot)
    write('q')
    sleep(1.5)
    write('0')
    sleep(5)
    write('2')
    sleep(1.5)
    write('5')
    sleep(1.5)
    write('4')
    sleep(1.5)
    write('s')
    sleep(foot+0.3)
    write('q')
    sleep(1.5)
    write('3')
    sleep(1.5)
    write('4')
    sleep(1.5)
    write('w')
    sleep(foot*2)
    write('q')
    sleep(1.5)
    write('0')
    sleep(5)
    write('2')
    sleep(1.5)
    write('5')
    sleep(1.5)
    write('4')
    sleep(1.5)
    write('w')
    sleep(foot)
    write('q')
    sleep(1.5)

elif order == "231":
    # print("the order is", returnVal[2], returnVal[1], returnVal[3])
    write('r')
    sleep(1.5)
    write('w')
    sleep(foot)
    write('q')
    sleep(1.5)
    write('0')
    sleep(5)
    write('2')
    sleep(1.5)
    write('5')
    sleep(1.5)
    write('4')
    sleep(1.5)
    write('w')
    sleep(foot)
    write('q')
    sleep(1.5)
    write('0')
    sleep(5)
    write('2')
    sleep(1.5)
    write('5')
    sleep(1.5)
    write('4')
    sleep(1.5)
    write('s')
    sleep((foot*2)+0.3)
    write('q')
    sleep(1.5)
    write('3')
    sleep(1.5)
    write('4')
    sleep(1.5)


elif order == "312":
    # print("the order is", returnVal[1], returnVal[3], returnVal[2])
    write('r')
    sleep(1.5)
    write('w')
    sleep(foot*2)
    write('q')
    sleep(1.5)
    write('0')
    sleep(5)
    write('2')
    sleep(1.5)
    write('5')
    sleep(1.5)
    write('4')
    sleep(1.5)
    write('s')
    sleep((foot*2)+0.3)
    write('q')
    sleep(1.5)
    write('3')
    sleep(1.5)
    write('4')
    sleep(1.5)
    write('w')
    sleep(foot)
    write('q')
    sleep(1.5)
    write('0')
    sleep(5)
    write('2')
    sleep(1.5)
    write('5')
    sleep(1.5)
    write('4')
    sleep(1.5)

    


elif order == "321":
    # print("the order is", returnVal[1], returnVal[2], returnVal[3])
    write('r')
    sleep(1.5)
    write('w')
    sleep(foot*2)
    write('q')
    sleep(1.5)
    write('0')
    sleep(5)
    write('2')
    sleep(1.5)
    write('5')
    sleep(1.5)
    write('4')
    sleep(1.5)
    write('s')
    sleep(foot)
    write('q')
    sleep(1.5)
    write('0')
    sleep(5)
    write('2')
    sleep(1.5)
    write('5')
    sleep(1.5)
    write('4')
    sleep(1.5)
    write('s')
    sleep(foot+0.3)
    write('q')
    sleep(1.5)
    write('3')
    sleep(1.5)
    write('4')
    sleep(1.5)
    
    




# importing required libraries
import cv2  # OpenCV library 
import time # time library
from threading import Thread # library for multi-threading
import numpy as np

# defining a helper class for implementing multi-threading 
class WebcamStream :
    # initialization method 
    def __init__(self, stream_id=0):
        self.stream_id = stream_id # default is 0 for main camera 
        
        # opening video capture stream 
        self.vcap  = cv2.VideoCapture(1)
        if self.vcap.isOpened() is False :
            print("[Exiting]: Error accessing webcam stream.")
            exit(0)
        fps_input_stream = int(self.vcap.get(5)) # hardware fps
        print("FPS of input stream: {}".format(fps_input_stream))
            
        # reading a single frame from vcap stream for initializing 
        self.grabbed , self.frame = self.vcap.read()
        if self.grabbed is False :
            print('[Exiting] No more frames to read')
            exit(0)
        # self.stopped is initialized to False 
        self.stopped = True
        # thread instantiation  
        self.t = Thread(target=self.update, args=())
        self.t.daemon = True # daemon threads run in background 
        
    # method to start thread 
    def start(self):
        self.stopped = False
        self.t.start()
    # method passed to thread to read next available frame  
    def update(self):
        while True :
            if self.stopped is True :
                break
            self.grabbed , self.frame = self.vcap.read()
            if self.grabbed is False :
                print('[Exiting] No more frames to read')
                self.stopped = True
                break 
        self.vcap.release()
    # method to return latest read frame 
    def read(self):
        return self.frame
    # method to stop reading frames 
    def stop(self):
        self.stopped = True

someVal = False
start = time.time()
# initializing and starting multi-threaded webcam input stream 
webcam_stream = WebcamStream(stream_id=0) # 0 id for main camera
webcam_stream.start()
# processing frames in input stream
num_frames_processed = 0 
start = time.time()
while True :
    if webcam_stream.stopped is True :
        break
    else :
        y3 = []
        height = {}
        # Reading the video from the 
        # webcam in image frames 
        base = webcam_stream.read() 
        #base = cv2.convertScaleAbs(base, alpha=3)


        # lab = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2LAB)
        # # store the a-channel
        # a_channel = lab[:,:,1]
        # # Automate threshold using Otsu method
        # th = cv2.threshold(a_channel,127,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]
        # # Mask the result with the original image
        # imageFrame = cv2.bitwise_and(imageFrame, imageFrame, mask = th)

        # hsv = cv2.cvtColor(base, cv2.COLOR_BGR2HSV)
        # ## mask of green (36,0,0) ~ (70, 255,255)
        # mask1 = cv2.inRange(hsv, (36, 0, 0), (70, 255,255))
        # ## mask o yellow (15,0,0) ~ (36, 255, 255)
        # mask2 = cv2.inRange(hsv, (15,0,0), (36, 255, 255))
        # ## final mask and masked
        # mask = cv2.bitwise_or(mask1, mask2)
        # imageFrame = cv2.bitwise_and(base,base, mask=mask)
    
        # # Convert the imageFrame in  
        # # BGR(RGB color space) to  
        # # HSV(hue-saturation-value) 
        # # color space 
        # hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV) 
    
        # # Set range for red color and  
        # # define mask 
        # red_lower = np.array([136, 87, 111], np.uint8) 
        # red_upper = np.array([180, 255, 255], np.uint8) 
        # red_mask = cv2.inRange(hsvFrame, red_lower, red_upper) 
    
        # # Set range for green color and  
        # # define mask 
        # green_lower = np.array([25, 52, 72], np.uint8) 
        # green_upper = np.array([102, 255, 255], np.uint8) 
        # green_mask = cv2.inRange(hsvFrame, green_lower, green_upper) 
    
        # # Set range for blue color and 
        # # define mask 
        # blue_lower = np.array([94, 80, 2], np.uint8) 
        # blue_upper = np.array([120, 255, 255], np.uint8) 
        # blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper) 
        
        # # Morphological Transform, Dilation 
        # # for each color and bitwise_and operator 
        # # between imageFrame and mask determines 
        # # to detect only that particular color           
    
        # # Creating contour to track green color 
        # contours, hierarchy = cv2.findContours(green_mask, 
        #                                     cv2.RETR_TREE, 
        #                                     cv2.CHAIN_APPROX_SIMPLE) 
        
        # for pic, contour in enumerate(contours): 
        #     area = cv2.contourArea(contour) 
        #     if(area > 500): 
        #         x, y1, w, h = cv2.boundingRect(contour) 
        #         if y1 > x*2:
        #             # base = cv2.rectangle(base, (x, y1),  
        #             #                         (x + w, y1 + h), 
        #             #                         (0, 255, 0), 2) 
                    
        #             # cv2.putText(base, "Yellow Colour", (x, y1), 
        #             #             cv2.FONT_HERSHEY_SIMPLEX,  
        #             #             1.0, (255, 255, 0)) 
                    
        #             y3.append(y1)
        #             height['yellow'] = y1
        
        baseFrame = webcam_stream.read() 
        #baseFrame = cv2.convertScaleAbs(baseFrame, alpha=3)
    
        lab = cv2.cvtColor(baseFrame, cv2.COLOR_BGR2LAB)
        # store the a-channel
        a_channel = lab[:,:,1]
        # Automate threshold using Otsu method
        th = cv2.threshold(a_channel,127,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]
        # Mask the result with the original image
        baseFrame = cv2.bitwise_and(baseFrame, baseFrame, mask = th)

        # Convert the baseFrame in  
        # BGR(RGB color space) to  
        # HSV(hue-saturation-value) 
        # color space 
        hsvFrame = cv2.cvtColor(baseFrame, cv2.COLOR_BGR2HSV) 
    
        # Set range for red color and  
        # define mask 
        red_lower = np.array([136, 87, 111], np.uint8) 
        red_upper = np.array([180, 255, 255], np.uint8) 
        red_mask = cv2.inRange(hsvFrame, red_lower, red_upper) 
    
        # Set range for green color and  
        # define mask 
        green_lower = np.array([25, 52, 72], np.uint8) 
        green_upper = np.array([102, 255, 255], np.uint8) 
        green_mask = cv2.inRange(hsvFrame, green_lower, green_upper) 
    
        # Set range for blue color and 
        # define mask 
        blue_lower = np.array([94, 80, 2], np.uint8) 
        blue_upper = np.array([120, 255, 255], np.uint8) 
        blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper) 
        
        # Morphological Transform, Dilation 
        # for each color and bitwise_and operator 
        # between imageFrame and mask determines 
        # to detect only that particular color 
    
    
        # Creating contour to track green color 
        # contours, hierarchy = cv2.findContours(green_mask, 
        #                                     cv2.RETR_TREE, 
        #                                     cv2.CHAIN_APPROX_SIMPLE) 
        
        # real = True
        # for pic, contour in enumerate(contours): 
        #     area = cv2.contourArea(contour) 
        #     if(area > 500):
        #         x, y2, w, h = cv2.boundingRect(contour) 
        #         for n in y3:
        #             if np.abs(n-y2) > 5:
        #                 pass
        #             else: 
        #                 real = False 
        #         if real and y2 > x*2:
        #             base = cv2.rectangle(base, (x, y2),  
        #                                     (x + w, y2 + h), 
        #                                     (0, 255, 0), 2) 
                    
        #             cv2.putText(base, "Green Colour", (x, y2), 
        #                         cv2.FONT_HERSHEY_SIMPLEX,  
        #                         1.0, (0, 255, 0)) 
                    
                    # height['green'] = y2
        # Python code for Multiple Color Detection 

        # Reading the video from the 
        # webcam in image frames 
        imageFrame = webcam_stream.read() 
        #imageFrame = cv2.convertScaleAbs(imageFrame, alpha=3)


        hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV) 

        # Set range for red color and 
        # define mask 
        red_lower = np.array([136, 87, 111], np.uint8) 
        red_upper = np.array([180, 255, 255], np.uint8) 
        red_mask = cv2.inRange(hsvFrame, red_lower, red_upper) 

        # Set range for green color and 
        # define mask 
        green_lower = np.array([25, 52, 72], np.uint8) 
        green_upper = np.array([102, 255, 255], np.uint8) 
        green_mask = cv2.inRange(hsvFrame, green_lower, green_upper) 

        # Set range for blue color and 
        # define mask 
        blue_lower = np.array([60, 80, 2], np.uint8) 
        blue_upper = np.array([150, 255, 255], np.uint8) 
        blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper) 

        kernel = np.ones((5, 5), "uint8") 

        # For red color 
        red_mask = cv2.dilate(red_mask, kernel) 
        res_red = cv2.bitwise_and(imageFrame, imageFrame, 
                                mask = red_mask) 

        # For green color 
        green_mask = cv2.dilate(green_mask, kernel) 
        res_green = cv2.bitwise_and(imageFrame, imageFrame, 
                                    mask = green_mask) 

        # For blue color 
        blue_mask = cv2.dilate(blue_mask, kernel) 
        res_blue = cv2.bitwise_and(imageFrame, imageFrame, 
                                mask = blue_mask) 

        # Creating contour to track red color 
        contours, hierarchy = cv2.findContours(red_mask, 
                                            cv2.RETR_TREE, 
                                            cv2.CHAIN_APPROX_SIMPLE) 

        for pic, contour in enumerate(contours): 
            area = cv2.contourArea(contour) 
            if(area > 300): 
                x, y, w, h = cv2.boundingRect(contour) 
                base = cv2.rectangle(base, (x, y), 
                                        (x + w, y + h), 
                                        (0, 0, 255), 2) 
                
                cv2.putText(base, "Pink Colour", (x, y), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1.0, 
                            (0, 0, 255))	 
                
                height['pink'] = y

        # Creating contour to track blue color 
        contours, hierarchy = cv2.findContours(blue_mask, 
                                            cv2.RETR_TREE, 
                                            cv2.CHAIN_APPROX_SIMPLE) 
        for pic, contour in enumerate(contours): 
            area = cv2.contourArea(contour) 
            if(area > 500): 
                x, y, w, h = cv2.boundingRect(contour) 
                if np.abs(w) > 100 and np.abs(h) < 50:
                    imageFrame = cv2.rectangle(imageFrame, (x, y), 
                                            (x + w, y + h), 
                                            (0, 255, 0), 2) 
                    
                    cv2.putText(imageFrame, "Green Colour", (x, y), 
                                cv2.FONT_HERSHEY_SIMPLEX, 
                                1.0, (0, 255, 0)) 
                    
                    height['green'] = y

        # if 'green' not in height:
        #     height['green'] = 280
        if len(height) == 2:
            if height['green'] < 190 and height['pink'] < 190:
                height['yellow'] = 230
            elif height['green'] > 200 and height['pink'] < 150:
                height['yellow'] = 170
            else:
                height['yellow'] = 130

            if height['yellow'] > 50 and height['green'] > 50:
                if (time.time() - start > 15):
                    someVal = True

            print(dict(sorted(height.items(), key=lambda item: item[1])))

    # adding a delay for simulating video processing time 
    num_frames_processed += 1
    # displaying frame 
    cv2.imshow('frame' , imageFrame)
    key = cv2.waitKey(1)
    if key == ord('q') or someVal:
        returnVal = []
        for n in (dict(sorted(height.items(), key=lambda item: item[1]))):
            returnVal.append(n)
        break
end = time.time()
webcam_stream.stop() # stop the webcam stream

print(returnVal)
#top to bottom


if order == "123":
    print("the order is", returnVal[2], returnVal[1], returnVal[0])

elif order == "132":
    print("the order is", returnVal[2], returnVal[0], returnVal[1])

elif order == "213":
    print("the order is", returnVal[1], returnVal[2], returnVal[0])

elif order == "231":
    print("the order is", returnVal[1], returnVal[0], returnVal[2])


elif order == "312":
    print("the order is", returnVal[0], returnVal[2], returnVal[1])
    

elif order == "321":
    print("the order is", returnVal[0], returnVal[1], returnVal[2])