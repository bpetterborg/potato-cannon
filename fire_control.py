# controls a potato cannon with a Raspbery Pi

# set buttonTimeOpen to correct value if running in trigger mode
# this isn't needed in remote mode

# importing stuff
import gpiozero # rpi gpio control
from time import sleep

# variables
relay = LED(17) # set to correct pin
button = Button(2) # set to correct pin
operationModeSelect = Button(3) # set to correct pin. 3 is not the correct pin
buttonTimeOpen = 0.7
cooldown = input('set cooldown time for remote mode: ')

# fire cannon in trigger mode
while operationModeSelect.when_pressed:

    if button.when_released:
       
        print("operationModeSelect is set to remote")
        print("buttonTimeOpen = " + buttonTimeOpen)
        print("firing... \n")
       
        relay.on()
        print('firing for ' + buttonTimeOpen + 's')
        sleep(float(buttonTimeOpen))
        relay.off()

        print('cannon fired \n')

    else:
        relay.off()

# fire cannon in remote mode
while True: 
    
    # set firing parameters
    sleep(0.25)
    timeOpen = input('Set timeOpen (seconds): ')
    firingInput = input('Fire cannon? [Y]es [N]o: ' + '\n' )

    # make it do the thing
    if firingInput == 'y':

        print('operationModeSelect is set to remote')
        print('timeopen set to ' + timeOpen + '\n')
        print('firing... ')

        relay.on()
        print('firing for ' + timeOpen + 's')
        sleep(float(timeOpen))
        relay.off()

        print('Cannon fired.')
        print('sleeping for ' + cooldown + 's')
        sleep(float(cooldown))
        print('It is now safe to reload the cannon \n')
   
    else:
        relay.off()
        print('not firing; firingInput set to False \n')

