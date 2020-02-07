from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import json
import socket
import ecampumper
import xhsi_data

class flightcontrol(object):
    """
    fc = {
          'leftflap' : 0,
          'rightflap' : 0,
          'left_ail' : 0,
          'right_ail' : 0,
          'left_elev' : 0,
          'right_elev' : 0,
          'rudder' : -2,
          'ailtrim' : -4,
          'stabtrim' : 3,
          'ruddertrim' : 10,
          'spoilersAll' : 0
          }
    """
    epumper = ecampumper.ecampumper()
    def __init__(self):
        #self.epumper = ecampumper.ecampumper()
        pass
    
    def setobs(self,x):
        self.epumper.setobserver(x)
        
    def getparam(self):
        #xhsi_data.fc['leftflap'] = xhsi_data.fc['leftflap'] + 1
        #xhsi_data.fc['rightflap'] = xhsi_data.fc['rightflap'] + 1
        return xhsi_data.fc
    
        
class Ecam(WebSocket):
    f = flightcontrol()
    def handle(self):
        #print 'handle'
        
        #fc = flightcontrol.getparam(self)
        fc = self.f.getparam()
        
        d = json.dumps(fc)
        
        e = unicode(d)
        
        # fc  message back to client
        self.sendMessage(e)

    def handleMessage(self):
        
        #fc = flightcontrol.getparam(self)
        fc = self.f.getparam()
        d = json.dumps(fc)
        
        e = unicode(d)
        
        # fc  message back to client
        self.sendMessage(e)

    def handleConnected(self):
        
        print(self.address, 'connected')

        self.sendMessage(unicode('Hello'))

        self.f.setobs(self.handle)
        
    def handleClose(self):
        print(self.address, 'closed')

def func():
    print 'func'
    
if __name__ == "__main__":
    #ff = flightcontrol()
    server = SimpleWebSocketServer('', 8000, Ecam)
    server.serveforever()

