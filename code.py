#!/bin/python3


# Imports
import RPi.GPIO as GPIO
import time
import os
import random
import socket
from PIL import Image
from thermalprinter import ThermalPrinter
from thermalprinter.constants import CodePage


# Global
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(6, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(8, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down = GPIO.PUD_UP)

BASEWIDTH = 384
B1LIST = []
B1CNT = 0
B2LIST = []
B2CNT = 0
B3LIST = []
B3CNT = 0
B4LIST = []
B4CNT = 0
B5LIST = []
B5CNT = 0


def print_image(img_path, p):
    """
    Gets image path, opens image, resizes it so that the width
    is 384px (max amount supported by the printer I used), converts the image to greyscale,
    prints the image
    """
    
    p.out("Photo:")
    p.feed(2)
    # Opening image
    im = Image.open(img_path)
    # Resizing while keeping the same proportions
    wpercent = (BASEWIDTH/float(im.size[0]))
    hsize = int((float(im.size[1])*float(wpercent)))
    im = im.resize((BASEWIDTH, hsize), Image.ANTIALIAS)
    # Converting image to greyscale
    im = im.convert('L')
    
    p.image(im)
    p.feed(4)


def print_text(text_path, p):
    """
    Gets path of a txt file, reads it, and prints it
    """

    # Reading file
    with open(text_path, 'r') as f:
        text = f.read()
    
    p.out(text, justify='L')
    p.feed(4)


def randomize_files(dir_num):
    """
    Gets all files from requested directory under /home/pi/Desktop/final/
    and returns them in a list in a randomized order
    """
    
    dir_path = "/home/pi/Desktop/final/"+str(dir_num)+"/"
    files_list = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
    full_path_list = []
    for x in files_list:
        full_path_list.append(dir_path+x)

    random.shuffle(full_path_list)
    return full_path_list


def button1(p):
    """
    Button 1
    """
    print("Button 1")
    global B1LIST
    global B1CNT
    if B1LIST == []:
        B1LIST = randomize_files('1')

    if B1LIST[B1CNT][-4:] == ".txt":
        print_text(B1LIST[B1CNT], p)
    elif B1LIST[B1CNT][-5:] == ".jpeg":
        print_image(B1LIST[B1CNT], p)
    else:
        p.out("This file is not a .txt or .jpeg file", justify='L')
        p.feed(4)

    B1CNT = B1CNT + 1
    if B1CNT == len(B1LIST):
        B1CNT = 0


def button2(p):
    """
    Button 2
    """
    print("Button 2")
    global B2LIST
    global B2CNT
    if B2LIST == []:
        B2LIST = randomize_files('2')

    if B2LIST[B2CNT][-4:] == ".txt":
        print_text(B2LIST[B2CNT], p)
    elif B2LIST[B2CNT][-5:] == ".jpeg":
        print_image(B2LIST[B2CNT], p)
    else:
        p.out("This file is not a .txt or .jpeg file", justify='L')
        p.feed(4)

    B2CNT = B2CNT + 1
    if B2CNT == len(B2LIST):
        B2CNT = 0


def button3(p):
    """
    Button 3
    """
    print("Button 3")
    global B3LIST
    global B3CNT
    if B3LIST == []:
        B3LIST = randomize_files('3')

    if B3LIST[B3CNT][-4:] == ".txt":
        print_text(B3LIST[B3CNT], p)
    elif B3LIST[B3CNT][-5:] == ".jpeg":
        print_image(B3LIST[B3CNT], p)
    else:
        p.out("This file is not a .txt or .jpeg file", justify='L')
        p.feed(4)

    B3CNT = B3CNT + 1
    if B3CNT == len(B3LIST):
        B3CNT = 0


def button4(p):
    """
    Button 4
    """
    print("Button 4")
    global B4LIST
    global B4CNT
    if B4LIST == []:
        B4LIST = randomize_files('4')

    if B4LIST[B4CNT][-4:] == ".txt":
        print_text(B4LIST[B4CNT], p)
    elif B4LIST[B4CNT][-5:] == ".jpeg":
        print_image(B4LIST[B4CNT], p)
    else:
        p.out("This file is not a .txt or .jpeg file", justify='L')
        p.feed(4)

    B4CNT = B4CNT + 1
    if B4CNT == len(B4LIST):
        B4CNT = 0


def button5(p):
    """
    Button 5
    """
    print("Button 5")
    global B5LIST
    global B5CNT
    if B5LIST == []:
        B5LIST = randomize_files('5')

    if B5LIST[B5CNT][-4:] == ".txt":
        print_text(B5LIST[B5CNT], p)
    elif B5LIST[B5CNT][-5:] == ".jpeg":
        print_image(B5LIST[B5CNT], p)
    else:
        p.out("This file is not a .txt or .jpeg file", justify='L')
        p.feed(4)

    B5CNT = B5CNT + 1
    if B5CNT == len(B5LIST):
        B5CNT = 0


def main():
        
    ip = ''
    # If device is connected to the internet, print the ip address
    # I attempt to get the ip address so that if there is internet connection when the pi
    # turns on I could edit and change the files via ftp without having to connect a keyboard/mouse/screen
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = str(s.getsockname()[0])
        s.close()
    except Exception as e:
        pass

    
    with ThermalPrinter(port='/dev/serial0') as p:

        # Execute functions when buttons are pressed
        GPIO.add_event_detect(17, GPIO.FALLING, callback = lambda x: button1(p), bouncetime = 2000)
        GPIO.add_event_detect(22, GPIO.FALLING, callback = lambda x: button2(p), bouncetime = 2000)
        GPIO.add_event_detect(6, GPIO.FALLING, callback = lambda x: button3(p), bouncetime = 2000)
        GPIO.add_event_detect(8, GPIO.FALLING, callback = lambda x: button4(p), bouncetime = 2000)
        GPIO.add_event_detect(26, GPIO.FALLING, callback = lambda x: button5(p), bouncetime = 2000)
        
        # The pi can take time to startup so I made it print "I'm ready" when it's ready
        p.out("I'm Readyyy", justify='C')
        if ip != '':
            p.out(ip, justify='C')
        p.feed(6)

        # Waiting
        while 1:
            time.sleep(1)


if __name__ == "__main__":
    main()

