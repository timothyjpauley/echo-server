import socket
import sys
import traceback
'''
Tim Pauley
Python 230 HW2 Updated
Date 04/18/2019

I went through the demo's and fixed /filled in the correct code
'''

def server(log_buffer=sys.stderr):
    # set an address for our server
    address = ('127.0.0.1', 10000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # log that we are building a server
    print("making a server on {0}:{1}".format(*address), file=log_buffer)

    # TODO: bind your new sock 'sock' to the address above and begin to listen
    #       for incoming connections
    sock.bind(address)
    try:
        sock.listen(1)
        while True:
            print('waiting for a connection', file=log_buffer)
            conn, addr = sock.accept()
            try:
                print('connection - {0}:{1}'.format(*addr), file=log_buffer)
                while True:
                    data = conn.recv(16)
                    print('received "{0}"'.format(data.decode('utf8')))
                    
                    print('sent "{0}"'.format(data.decode('utf8')))
                    
                    if data != b'':
                        print("Sending data back to the client")
                        conn.sendall(data)
                    else:
                        print("No more data from ", addr)
                        break
            except Exception as e:
                traceback.print_exc()
                sys.exit(1)
            finally:
                conn.close()
                print(
                    'echo complete, client connection closed', file=log_buffer
                )

    except KeyboardInterrupt:
        print('quitting echo server', file=log_buffer)
        raise


if __name__ == '__main__':
    server()
    sys.exit(0)