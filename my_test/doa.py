from tuning import Tuning
import usb.core
import usb.util
import time
import sys

dev = usb.core.find(idVendor=0x2886, idProduct=0x0018)

if dev:
    Mic_tuning = Tuning(dev)
    while True:
        try:
            #print "\rDIR:", Mic_tuning.direction, ", VAD:", Mic_tuning.is_voice(), "SPEECH:", Mic_tuning.read('SPEECHDETECTED'),
            if Mic_tuning.read('SPEECHDETECTED'): 
                print 's',
            elif Mic_tuning.is_voice():
                print ".",
            sys.stdout.flush()
            time.sleep(0.1)
        except KeyboardInterrupt:
            break

