import socket
import sys
import datetime
import time

now = datetime.datetime.now()

print str(now)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
#---------------------------------------------------------CONNECTION SETUP PHASE <Protocol Phase> WS <Measurement Type> WS <No. of Probes> WS <MESSAGE SIZE> WS <Server Delay>
print 's  rtt  4 800 4'
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print '800 OK'
        print >>sys.stderr, 'connection from', client_address
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(800)
#---------------------------------------------------------MEASUREMENT PHASE <Protocol Phase> WS <Probe Seq. No.> WS <Payload>
            print 'm  4  11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111'
            print >>sys.stderr, 'received "%s"' % data
            if data:
                time.sleep(4)
                print >>sys.stderr, 'sending data back to the client'
                connection.sendall(data)
            else:
                print >>sys.stderr, 'no more data from', client_address
                break
    finally:
        # Clean up the connection
        print '800 OK: Closing Connection'
#---------------------------------------------------------CONNECTION TERMINATION PHASE <Protocol Phase> WS
        print 't  .'
        connection.close()
