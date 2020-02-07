import socket
import struct
import xhsi_id
import xhsi_data

class xhsiRx(object):
    obs = []
    
    def setobs(self,x):
        print 'set'
        self.obs = [x]

    def invoke(self):
        #print  'invoke'
        if len(self.obs) > 0:
          self.obs[0]()
        
    def network(self):
        host = "0.0.0.0"
        port  = 49018

        
        self.sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

            
        self.sock.bind((host,port))

    def forever1(self):
      
        while True:
            data,addr = self.sock.recvfrom(8192)
            
            #print data
            self.unpack1(data)
            
    def forever(self):
       with open('xhsi.bin','wb') as f:
           while True:
               data,addr = self.sock.recvfrom(8192)
               f.write(data)
               #print data
    
    def unpack1(self,data):
        #print data
        #read header
        h = str(data[0:4])
        #print h
        header = struct.unpack('>cccc',h)
        #print 'header'
        #print header
        length = struct.unpack('>i',str(data[4:8]))
        #print length[0]
        j = 8
        if h[0:3]=='FMC':
            length = (0,)
            
        for i in xrange(length[0]):
            id = str(data[j:j+4])
            j=j+4
            v =  str(data[j:j+4])
            j=j+4
            idd = struct.unpack('>i',id)
            vv = struct.unpack('>f',v)
            #print idd[0], vv[0]
            if h=='ADCD':
                xhsi_id.setflightcontrol(idd[0],vv[0])

        self.invoke()
        '''
                if idd[0]==xhsi_id.SIM_COCKPIT2_CONTROLS_FLAP_RATIO:
                    print 'flap ratio %f' % vv[0]
                    xhsi_data.fc['leftflap'] = vv[0]*40
                    xhsi_data.fc['rightflap'] = vv[0]*40
        '''
                
    def unpack(self):
        with open('xhsi.bin','rb') as f:
            #read header
            h = f.read(4)
            #print h
            header = struct.unpack('>cccc',h)
            print 'header'
            print header
            length = struct.unpack('>i',f.read(4))
            #print length[0]
            for i in xrange(length[0]):
                id = f.read(4)
                v = f.read(4)
                idd = struct.unpack('>i',id)
                vv = struct.unpack('>f',v)
                print idd[0], vv[0]
                if header=={'A','D','C','D'}:
                    if idd[0]==xhsi_id.SIM_COCKPIT2_CONTROLS_FLAP_RATIO:
                        print 'flap ratio %f' % vv[0]
                


#xp = xhsiRx()

#xp.network()

#xp.forever()
#xp.unpack()
       
