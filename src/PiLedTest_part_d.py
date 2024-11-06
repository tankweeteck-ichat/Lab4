import hal.hal_input_switch as SWITCH
import hal.hal_led as LED
import time

def control_LED(turn_on):
    if turn_on is True:
        LED.set_output(24, 1)
    else:
        LED.set_output(24, 0)

def main():
    on_off = True
    counter=0
    LED.init()
    SWITCH.init()

    while(True):
        switchPosition = SWITCH.read_slide_switch()
        on_off = not on_off
        if switchPosition==1:
            time.sleep(0.1)  # This sets the 5 Hz blinking.
            counter=0  # Reset the 5 sec counter
        else:
            time.sleep(0.05)  # This sets the 10 Hz blinking.
            counter +=1   # Increment the 5 sec counter.
            if counter>=100:   # 100*0.05 sec = 5 sec
                on_off = False    # Turn off the LED.
        control_LED(on_off)



# Main entry point
if __name__ == "__main__":
    main()

