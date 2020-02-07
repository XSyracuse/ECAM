from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import json
import socket
class flightcontrol:
    def __init__(self):
        self.fc = {
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
        self.network()
        
    def network(self):
        host = "0.0.0.0"
        port  = 5005

        
        self.sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

            
        self.sock.bind((host,port))


    def get(self):
        self.fc['leftflap'] = self.fc['leftflap'] + 1
        self.fc['rightflap'] = self.fc['rightflap'] + 1
        return self.fc
    
        
class SimpleEcho(WebSocket):

    f = flightcontrol()
   
        
    def handleMessage(self):
        
        fc = self.f.get()
        d = json.dumps(fc)
        
        e = unicode(d)
        
        # fc  message back to client
        self.sendMessage(e)

    def handleConnected(self):
        
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')

server = SimpleWebSocketServer('', 8000, SimpleEcho)
server.serveforever()

