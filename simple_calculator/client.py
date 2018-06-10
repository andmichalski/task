import socket

class MyClient:

    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def get_input(self):
        print("Please write simple calculation with symbols: +, -, *, /")
        calculation = input("Write here: ")
        return calculation


    def send_equation(self, calculation):
        self.s.sendto(calculation.encode('utf-8'), ("127.0.0.1", 5005))
        calculation = self.s.recv(1024)
        print("Got: ", calculation.decode('utf-8'))

def main():
    server = MyClient()
    calculation = server.get_input()
    server.send_equation(calculation)
if __name__ == "__main__":
    main()