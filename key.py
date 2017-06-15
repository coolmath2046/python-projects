import struct
file = open("/dev/input/mice","rb")
currentX = 0
currentY = 0
def getMouseEvent():
    global currentX,currentY
    buf = file.read(3);
    button = ord(str(buf)[0]);
    bLeft = button & 0x1;
    bMiddle = ( button & 0x4 ) > 0;
    bRight = ( button & 0x2 ) > 0;
    x,y = struct.unpack( "bb", buf[1:] );
    currentX += x
    currentY += y
    print ("L:%d, M: %d, R: %d, x: %d, y: %d\n" % (bLeft,bMiddle,bRight, currentX, currentY) );
while True:
    getMouseEvent()
