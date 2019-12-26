import time
import board
import pulseio
import digitalio

switch = digitalio.DigitalInOut(board.SLIDE_SWITCH)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

#if switch.value is True: # switch is slid to the left

# Enable the speaker
speaker_enable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker_enable.direction = digitalio.Direction.OUTPUT
speaker_enable.value = True
 
# For the M0 boards:
piezo = pulseio.PWMOut(board.SPEAKER, duty_cycle=0, frequency=440, variable_frequency=True)
 
while True:
    while switch.value:
        for f in (262, 294, 330, 349, 392, 440, 494, 523):
            piezo.frequency = f
            piezo.duty_cycle = 65536 // 2  # On 50%
            time.sleep(0.25)  # On for 1/4 second
            piezo.duty_cycle = 0  # Off
            time.sleep(0.05)  # Pause between notes
        time.sleep(0.5)