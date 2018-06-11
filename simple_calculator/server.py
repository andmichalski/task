import socket


class MyServer:

    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def calculate(self, data):
        if "+" in data:
            nlist = [int(a) for a in data.split("+")]
            return sum(nlist)
        elif "-" in data:
            nlist = [int(a) for a in data.split("-")]
            return nlist[0] - nlist[1]
        elif "*" in data:
            nlist = [int(a) for a in data.split("*")]
            return nlist[0] * nlist[1]
        elif "/" in data:
            nlist = [int(a) for a in data.split("/")]
            return nlist[0] / nlist[1]
        elif data == "exit":
            self.s.close()
            exit(0)
        else:
            return "Can not do calculations"

    def calc_server(self):
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind(("127.0.0.1", 5005))

        while True:
            data, addr = self.s.recvfrom(1024)
            received_data = data.decode('utf-8')
            if data:
                data_to_send = self.calculate(received_data)
                self.s.sendto(str(data_to_send).encode('utf-8'), addr)


def main():
    server = MyServer()
    server.calc_server()


if __name__ == "__main__":
    main()
