from socket import *
#具体功能
class FtpClient:
    def __inti__(self,fd):
        self.fd = fd
    def do_list(self):
        self.fd.send(b'L')
        #等待回复
        data = self.fd.recv(128).decode()
        if data == "Ok":
            while True:
                data = self.fd.recv(128)
                if data == b'##':
                    break
                print(data.decode())

        else:
           print(data)
def request(fd):
    ftp = FtpClient()
    while True:
        print("\n===========命令选项===============")
        print("************list****************")
        print("************get_file****************")
        print("************put_file****************")
        print("************quit****************")
        print("*=================================")

        cmd = input("输入命令:")
        if cmd == 'list':
            ftp.do_list(fd)
        elif cmd == 'get_file':
            fd.recv(1024)
        elif cmd == 'put_file':
            fd.send()
        else:

#网络链接
def main ():
    #服务器地址
    ADDR = ("127.0.0.1",9999)
    fd = socket()
    try:
        fd.connect(ADDR)
    except Exception as e :
        print("链接服务器失败")
    else:
        print("""****************
             Date          File          Image
        ************************""")
        cls = input("请输入文件种类")
        if cls not in  ['Date','File','Image']:
            print("Sorry input Error!!")
            return
        else:
            fd.send(cls.encode())

if __name__ == "__main__":
    main()