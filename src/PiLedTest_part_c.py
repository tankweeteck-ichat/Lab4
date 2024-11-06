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
        on_off = not on_off
        if switchPosition==1:
            time.sleep(0.1)  # This sets the 5 Hz blinking.
        else:
            time.sleep(0.05)  # This sets the 10 Hz blinking.
        control_LED(on_off)



# Main entry point
if __name__ == "__main__":
    main()

