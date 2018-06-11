import socket


class MyClient:

    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def get_input(self):
        print("Please write simple calculation with symbols: +, -, *, /")
        calculation = input("Write here: ")
        return calculation

    def send_calculation(self, calculation):
        self.s.sendto(calculation.encode('utf-8'), ("127.0.0.1", 5005))
        if calculation == "exit":
            self.s.close()
            exit(0)
        calculation, addr = self.s.recvfrom(1024)
        print("Got: ", calculation.decode('utf-8'))


def main():
    client = MyClient()
    while True:
        calculation = client.get_input()
        client.send_calculation(calculation)


if __name__ == "__main__":
    main()
