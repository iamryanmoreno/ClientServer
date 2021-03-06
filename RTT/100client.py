import socket
import sys
import time
import datetime

now = datetime.datetime.now()

print str(now)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
#---------------------------------------------------------CONNECTION SETUP PHASE <Protocol Phase> WS <Measurement Type> WS <No. of Probes> WS <MESSAGE SIZE> WS <Server Delay>
print 's  rtt  2 100 1'
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
    # Send data
    message = '1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111'
    t1 = time.time()
#---------------------------------------------------------MEASUREMENT PHASE <Protocol Phase> WS <Probe Seq. No.> WS <Payload>
    print 'm  2  1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111'
    print >>sys.stderr, 'sending "%s"' % message
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = sock.recv(100)
        amount_received += len(data)
        print >>sys.stderr, 'received "%s"' % data
    t2 = time.time()
    print 'RTT is', t2 - t1, 'seconds'
	
	#formula of throughput RWIN (TCP Receive Window)/RTT [bytes/s]
	
finally:
#---------------------------------------------------------CONNECTION TERMINATION PHASE <Protocol Phase> WS
    print 't  .'
    print >>sys.stderr, 'closing socket'
    sock.close()
