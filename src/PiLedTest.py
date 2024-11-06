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
    LED.init()
    SWITCH.init()

    while(True):
        switchPosition = SWITCH.read_slide_switch()
        if switchPosition==1:
            on_off = not on_off
        else:
            on_off = False
        control_LED(on_off)
        time.sleep(0.1)     # This sets the 5 Hz blinking.



# Main entry point
if __name__ == "__main__":
    main()

