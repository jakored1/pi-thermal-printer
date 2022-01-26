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
(some of the photos I used here belong to the websites/companies that host the above tutorials, I do not claim to own them)

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
- Rechargeable battery to power the Raspberry Pi: https://www.adafruit.com/product/1566
- Battery pack to power the thermal printer: https://www.adafruit.com/product/248
- Thermal Printer starter pack: https://www.adafruit.com/product/600
- Buttons (these are good cause they are pre-wired): https://www.amazon.com/Twidec-Normal-Momentary-Pre-soldered-PBS-110-XBK/dp/B07RPS2ZY3/ref=sr_1_4?keywords=momentary+pushbutton&qid=1584144566&rnid=2941120011&s=industrial&sr=1-4
- Raspberry Pi (can probably use any model, in this project I used a model 2 I got in 2016): https://www.raspberrypi.com/products/raspberry-pi-4-model-b/
- Jumper cables: https://www.amazon.com/REXQualis-120pcs-Breadboard-Arduino-Raspberry/dp/B072L1XMJR/ref=sr_1_2_sspa?keywords=female+male+jumper+wire&qid=1643220257&s=electronics&sprefix=female+male+jumper+%2Celectronics%2C542&sr=1-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzTkpaODlEQjhHTkhNJmVuY3J5cHRlZElkPUEwMDU0NjA5WkhFREFQV0IzTVNIJmVuY3J5cHRlZEFkSWQ9QTA2NTYzMDQyNUtER0JJWVhRNldCJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==
- **optional* - more thermal paper cause one is probably not enough: https://www.adafruit.com/product/599
  
**note - first two supplies can be ignored, but then it won't be portable and will require 2 electricity outlets, one to power the printer, and one to power the Raspberry Pi*  
  
Once we have our the supplies we can start our project!
  
  
## Step 1: Connecting the printer
After we setup our Raspberry Pi and connected it to a computer,  
we need to connect the thermal printer to it and make sure it can print.  
To connect the thermal printer to the Pi I recommend the first few minutes of this video:  
https://youtu.be/r6KvQShmRJg?t=475  

After we have the printer connected, we need to configure some stuff on the Pi.  
First we need to figure out the **BAUD rate** of the thermal printer,  
it should be written on the **test page** that came with the printer  
<img src="https://cdn-learn.adafruit.com/assets/assets/000/031/836/large1024/raspberry_pi_components_test-baud.jpg?1461025182" alt="drawing" width="300"/>  
(for the tutorial, we'll use a 19200 baud rate)
  
