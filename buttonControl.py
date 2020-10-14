# controls a potato cannon with a Raspbery Pi

# to-do
# make it so I don't have to ssh into it or use a button for firing


# importing stuff
import gpiozero
from time import sleep

# variables
relay = LED(17)
button = Button(2)
timeOpen = 0.7 # time to open relay for

timeOpen = input('Set timeOpen (seconds): ')
firingInput = input('Fire cannon? [Y]es [N]o: ')


# activate relay for 
while True:
    
    if button.when_released:
        
        print('firing... \n')
        relay.on()
        sleep(timeOpen)
        relay.off()
    
    else:
        relay.off()

while True:
    
    if firingInput == 'y':

        print('firing... \n')
        relay.on()
        sleep(timeOpen)
        relay.off()

