import socket


class CalculatorServer:

    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def calculate(self, data):

        def split_by_operator(data, oper):
            return [int(d) for d in data.split(oper)]

        if "+" in data:
            nlist = split_by_operator(data, "+")
            return sum(nlist)
        elif "-" in data:
            nlist = split_by_operator(data, "-")
            return nlist[0] - nlist[1]
        elif "*" in data:
            nlist = split_by_operator(data, "*")
            return nlist[0] * nlist[1]
        elif "/" in data:
            nlist = split_by_operator(data, "/")
            try:
                division = nlist[0] / nlist[1]
            except ZeroDivisionError:
                division = "You can not divide by 0"
            return division
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
    server = CalculatorServer()
    server.calc_server()


if __name__ == "__main__":
    main()
