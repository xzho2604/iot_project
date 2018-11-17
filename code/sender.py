import socket


#read file and then retunrn the coment of the file in binary
def file_deal(file_name):
    try:
        files = open(file_name, "rb")
        mes = files.read()
    except:
        print("没有该文件")
    else:
        files.close()
        return mes

def main():
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    #the receiver address
    tcp_ip = '127.0.0.1'
    tcp_port = 8888
    tcp_socket.connect((tcp_ip, tcp_port))
    while True:
        # 利用accept获取分套接字以及客户端的地址
        mes = file_deal("record.txt")
        if mes:
            tcp_socket.send(mes.encode())
        #关闭分套接字
        else:
            print("message complete")

        tcp_socket.close()
if __name__ == "__main__":
    main()
