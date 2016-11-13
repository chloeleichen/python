from pyfirmata import Arduino, util
import time

board = Arduino('/dev/cu.usbmodem1411')
digital_9 = board.get_pin('d:9:i')




while True:
    it = util.Iterator(board)
    it.start()
    value = digital_9.read()
    print(value)
    time.sleep(1)
