# Raspberry Pi Thermal Printer
### _Fun Photo/Text Thermal Printer Present_

##### Reason:
This project was made for a friend as a birthday gift.  
When starting the project the goal was to create a box with 5 buttons and a thermal printer popping out.  
When pressing one of the five buttons a photo or a text message will be printed from the printer accordingly.  
The project will also be able to work without any electricity outlet, so the box can be carried around freely!  
##### Background:
I came into this project with no background in electronics and such, I only know some software.  
So I beleive this project isn't too challenging and can be accomplished relatively easily following this tutorial  
##### Credits:
To create this project I followed these tutorials:  
https://www.hackster.io/glowascii/using-a-thermal-printer-with-raspberry-pi-d74619  
https://learn.adafruit.com/networked-thermal-printer-using-cups-and-raspberry-pi/connect-and-configure-printer  
In this readme I'll explain how I combined the mentioned tutorials, the errors I ran into, how I solved them, hopefully allowing you to re-create this at home 😄  

#### Image of the final product:
###### Top:
<img src="https://github.com/jakored1/pi-thermal-printer/blob/main/photos-for-readme/TopViewPic.jpeg?raw=true" alt="drawing" width="300"/>

###### Back:
<img src="https://github.com/jakored1/pi-thermal-printer/blob/main/photos-for-readme/BackPic.jpeg?raw=true" alt="drawing" width="300"/>

###### Inside:
<img src="https://github.com/jakored1/pi-thermal-printer/blob/main/photos-for-readme/InteriorPic.jpeg?raw=true" alt="drawing" width="300"/>

###### Example Print:
<img src="https://github.com/jakored1/pi-thermal-printer/blob/main/photos-for-readme/ImagePic.jpeg?raw=true" alt="drawing" width="300"/>

### Supplies:
- [Rechargeable battery](https://www.adafruit.com/product/1566) to power the Raspberry Pi
- [Battery pack](https://www.adafruit.com/product/248) to power the thermal printer
- [Thermal Printer starter pack](https://www.adafruit.com/product/600)
- [Buttons](https://www.amazon.com/Twidec-Normal-Momentary-Pre-soldered-PBS-110-XBK/dp/B07RPS2ZY3/ref=sr_1_4?keywords=momentary+pushbutton&qid=1584144566&rnid=2941120011&s=industrial&sr=1-4) (these are good cause they are pre-wired)
- [Raspberry Pi](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/) (can probably use any model, in this project I used a model 2 I got in 2016)
- [Jumper cables](https://www.amazon.com/REXQualis-120pcs-Breadboard-Arduino-Raspberry/dp/B072L1XMJR/ref=sr_1_2_sspa?keywords=female+male+jumper+wire&qid=1643220257&s=electronics&sprefix=female+male+jumper+%2Celectronics%2C542&sr=1-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzTkpaODlEQjhHTkhNJmVuY3J5cHRlZElkPUEwMDU0NjA5WkhFREFQV0IzTVNIJmVuY3J5cHRlZEFkSWQ9QTA2NTYzMDQyNUtER0JJWVhRNldCJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==)
- **optional* - more [thermal paper](https://www.adafruit.com/product/599) cause one is probably not enough
  
**note - first two supplies can be ignored, but then it won't be portable and will require 2 electricity outlets, one to power the printer, and one to power the Raspberry Pi*  
  
Once we have our supplies we can start our project!
  
  
## Step 1: Setting up the printer
After we setup our Raspberry Pi and connected it to a computer,  
we need to connect the thermal printer to it and make sure it can print.  
To connect the thermal printer to the Pi I recommend the first few minutes of [this video](https://youtu.be/r6KvQShmRJg?t=475)
  
After we have the printer connected, we need to configure some stuff on the Pi,  
To do this correctly follow [this tutorial](https://learn.adafruit.com/networked-thermal-printer-using-cups-and-raspberry-pi/connect-and-configure-printer).  
If you **run into an error** like this:  
'CUPS Server Error: Success'  
<img src="https://i.redd.it/mm9jqkkg75611.jpg" alt="drawing" width="300"/>  
Then try to **install a different Raspbian image on your Raspberry Pi:**  
https://downloads.raspberrypi.org/raspbian/images/  
I ran into this error and none of the solutions online worked for me,  
so eventually I tried with another image and it worked!  
(I used [this image](https://downloads.raspberrypi.org/raspbian/images/raspbian-2019-04-09/2019-04-08-raspbian-stretch.zip))  
  
Once you finished the above tutorial and the printer prints properly we can move on to connecting the buttons.  
If printing the image comes out with gibberish don't worry about it,  
that happend to me but through the code (later on) photos were printing just fine  
  
## Step 2: Connecting the buttons  
To connect the buttons lets take a look at the [Raspberry Pi GPIO pinout](https://pinout.xyz/)  
We need to connect one of the buttons wires to a GPIO Pin (any of them) and the other wire to a Ground Pin (any of them).  
Do this for all the buttons you want to use, and remmember the number of the GPIO Pin you connected the button to as we'll need it later on  
  
Use the Jumper Cables we purchased to connect everything  
  
To test the buttons create a python file containing this code:  
```python
#!/bin/python 
import RPi.GPIO as GPIO  
GPIO.setmode(GPIO.BCM)  
GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_UP) # Replace 17 with the GPIO Pin you connected the button to  
  
def button1(channel):
    print("Button pressed")
  
def main():  
    # Execute functions when buttons are pressed
    GPIO.add_event_detect(17, GPIO.FALLING, callback = button1, bouncetime = 2000)
    # Waiting
    while 1:
        time.sleep(1)
if __name__ == "__main__":
    main()
```  
It should print when you press the button,  
If not, make sure both of the buttons wires are properly connected to the Pi  
  
## Step 3: Code!  
After we setup all the buttons and printer, lets write our code.  
The code.py file I placed in this project is fit for my needs so I will explain how to use it.  
If you're using less buttons then edit the code accordingly 😀  

First, create the following directory  
```sh
mkdir /home/pi/Desktop/final/
```  
Then create 5 more directories each named a number from 1 to 5 inside the 'final' directory  
```sh
mkdir /home/pi/Desktop/final/1
mkdir /home/pi/Desktop/final/2
mkdir /home/pi/Desktop/final/3
mkdir /home/pi/Desktop/final/4
mkdir /home/pi/Desktop/final/5
```  
After that, copy the code.py file into the 'final' directory.  
It should look something like this:  
+-- /home/pi/Desktop/final/  
+--+-- 1/  
+--+-- 2/  
+--+-- 3/  
+--+-- 4/  
+--+-- 5/  
+--+-- code.py  
Next!  
Fill the folders 1 to 5 with .jpeg and/or .txt files!  
Before we can run the script we need to install the required python packages  
```sh
python3 -m pip install pillow
python3 -m pip install thermal-printer
```  
(I forgot the exact name of the 'thermal-printer' package, it might be 'thermalprinter' instead)  
  
After all folders have at least one file in them (jpeg or txt), and we installed our packages,  
Run the script!  
```sh
python3 /home/pi/Desktop/final/code.py
```  
  
If everything went smoothly, when you press a button it should print one of the contents from the folder correspinding to the buttons number.  
Be patient! printing photos takes the printer some time, if you press another button while it's still printing the image will come out bad  
  
Finally,  
To make this into a portable box as shown in the above photos you will have to create a service that runs the code.py script when the Raspberry Pi starts up, buy a box, and pack it however you want!  
  
Enjoy!
