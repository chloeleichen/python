from pyfirmata import Arduino, util
import time

board = Arduino('/dev/cu.usbmodem1411')
echo_pin = board.get_pin('d:7:i')
trig_pin = board.get_pin('d:8:o')




while True:
    it = util.Iterator(board)
    it.start()
    trig_pin.write(False)
    time.sleep(1)
    trig_pin.write(True)
    time.sleep(1)
    
    value = digital_9.read()
    print(value)
