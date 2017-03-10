import socket
import sys
import datetime

now = datetime.datetime.now()

print str(now)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
#---------------------------------------------------------CONNECTION SETUP PHASE <Protocol Phase> WS <Measurement Type> WS <No. of Probes> WS <MESSAGE SIZE> WS <Server Delay>
try:
	print 's  rtt  1 1 0'
	sock.bind(server_address)

	# Listen for incoming connections
	sock.listen(1)
except ValueError:
	print '404 ERROR: Invalid Connection Setup Message'
	
while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print '1 OK'
        print >>sys.stderr, 'connection from', client_address
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1)
#---------------------------------------------------------MEASUREMENT PHASE <Protocol Phase> WS <Probe Seq. No.> WS <Payload>
            print 'm  1  1'
            print >>sys.stderr, 'received "%s"' % data
            if data:
				#add delay
                print >>sys.stderr, 'sending data back to the client'
                connection.sendall(data)
            else:
                print >>sys.stderr, 'no more data from', client_address
                break
    except ValueError:
        print '404 ERROR: Invalid Measurement Message'
    finally:
        try:
            # Clean up the connection
            print '1 OK: Closing Connection'
#---------------------------------------------------------CONNECTION TERMINATION PHASE <Protocol Phase> WS
            print 't  .'
            connection.close()
        except ValueError:
            print '404 ERROR: Invalid Connection Termination Message'
