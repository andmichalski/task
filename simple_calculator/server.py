import socket

class MyCalc:

    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    def calc_server(self):
        self.s.bind('', 8888)
        self.s.listen(5)

        while True:
            c, addr = self.s.accept()
            print "Connected with client"
            c.send("Thank for connection")
            message = c.recv(1024)
            if len(message) > 0:
                print(message)
            c.close()

    def calc_client(self):
        self.c.connect(('localhost', 8888))
        message = input("Write something: ")
        self.c.send(message)