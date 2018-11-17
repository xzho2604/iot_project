import socket
from data_clean import *
from imageShow import *
from predict_single import *

def main():
    # 创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind(("",8888))
    tcp_socket.listen(128)

    #write to the file when received data
    new_file = open("record.txt","wb")
 
    client_socket,client_addr = tcp_socket.accept()
    while True:
        data = client_socket.recv(4096)
        print(data)
        if data:
            #if there is data write t othe file
            new_file.write(data)
        else:
            print("transmission complete")
            break;

    client_socket.close()
    new_file.close()

if __name__ == "__main__":

    main()
    #now we have record.txt
    v=data_clean("record.txt",write_file=False)[0]
    print("Base Reading:", v[0:4])
    (x,y,err) = predict(v)
    plot_show(x,y,v[5],v[6])


