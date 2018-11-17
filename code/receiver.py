import socket

def main():
    # 创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind(("",8888))
    tcp_socket.listen(128)

    #write to the file when received data
    new_file = open("record.tx","wb")

    while True:
        client_socket,client_addr = tcp_socket.accept()
        data = client_socket.recv(4096)

        if data:
            #if there is data write t othe file
            new_file.write(data)
        else:
            print("transmission complete")
            new_file.close()
            break;

    client_socket.close()
    





if __name__ == "__main__":
    main()
