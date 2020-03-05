import socket
import os
from PyQt5.QtCore import QThread
from PyQt5 import QtCore
import copy
import pickle
from PIL import Image
import threading

# [ 'img_send', id , file_size , pic_number ]

class client(QThread,QtCore.QObject):
    recv_msg_signal = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.host = '127.0.0.1' #socket.gethostname()
        #self.host_ip = socket.gethostbyname(self.host)
        self.port = 5555
        self.ftp_port = 6666
        self.chat_port = 7777
        self.instruction = ' '
        self.msg_list = []
        self.number_of_widgets = 0
        self.my_id = ''
        self.my_dir = './'
        self.my_path = './'
        #self.login_success = False
        self.msg_list_server = []
        self.instruction_server = ' '
        self.anonymous_chat_buffer = ''
        self.id_other = ''

        print('connecting to %s' % self.host)
        self.server_addr = (self.host, self.port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.connect(self.server_addr)

        self.chat_server_addr = (self.host, self.chat_port)
        self.chat_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.chat_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #chat_initiate할때까지 기다려야함
        self.chat_buffer = ''

        self.ftp_server_addr = (self.host, self.ftp_port)
        self.ftp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ftp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.chat_recv_thread_stop = 1

        self.anonymous_chat_port = 4444
        self.anonymous_chat_server_addr = (self.host, self.anonymous_chat_port)
        self.anonymous_chat_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.anonymous_chat_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


    def match_chat_send(self,data):
        # 전송하려는 글자 수가 1000이 넘어가면 나눠서 보냄
        # 전체 문자열에서 1000글자를 잘라내서 보내고, 나머지 문자열에 대해 재귀실행
        self.sending = data[0]
        if len(self.sending) >1000:
            tmp = self.sending[0:1000]
            self.sending = self.sending[1000:len(self.sending)]
            self.chat_sock.send(pickle.dumps([tmp]))
            print(f'나눠서보냄 {tmp}')
            print(len(self.sending))
            self.match_chat_send([self.sending])
        else:
            self.chat_sock.send(pickle.dumps(data))
            print(data)
            print('그냥 보냄')


    def match_chat_recv(self):
        self.chat_buffer = self.chat_sock.recv(4096)


    # ['img_send',내 id, 이미지 size, 사진인덱스]
    def client_ftp_send(self,filepath):
        mutex =threading.Lock()
        mutex.acquire()
        self.ftp_sock.connect(self.ftp_server_addr)
        self.ftp_sock.send(pickle.dumps(self.msg_list[1]))
        print(self.msg_list[1])
        print('아이디보냄')
        mutex.release()

        f = open(filepath, 'rb')
        data = f.read()
        f.close()

        self.client_send()

        self.ftp_sock.send(data)
        # ['img_send',True or False, 내 id, 이미지 size, 사진인덱스]
        self.client_recv()

        self.ftp_sock.close()
        self.ftp_server_addr = (self.host, self.ftp_port)
        self.ftp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ftp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def ftp_recv_talk(self,filesize,id_other):
        self.msg_list.append('ftp_recv_talk')
        self.msg_list.append(self.my_id)
        self.msg_list.append(id_other)

        mutex = threading.Lock()
        mutex.acquire()
        self.ftp_sock.connect(self.ftp_server_addr)
        self.ftp_sock.send(pickle.dumps(self.my_id))
        mutex.release()

        self.client_send()
        recvd = 0
        while filesize > recvd:
            data = self.ftp_sock.recv(1024)
            recvd = recvd + len(data)
            print(len(data))
            fwrite = open('./tmp/tmp_chat.txt','ab')
            print(data)
            fwrite.write(data)
            fwrite.close()

        fread = open('./tmp/tmp_chat.txt','r')
        data_read = fread.read()
        fread.close()
        fwrite = open('./tmp/tmp_chat.txt', 'w')
        fwrite.write('')
        fwrite.close()
        self.ftp_sock.close()
        self.ftp_server_addr = (self.host, self.ftp_port)
        self.ftp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ftp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return data_read

    # ['img_recv',내id,상대id,사진index]
    def client_ftp_recv(self):
        pic_index = self.msg_list[3]
        mutex = threading.Lock()
        mutex.acquire()
        self.ftp_sock.connect(self.ftp_server_addr)
        self.ftp_sock.send(pickle.dumps(self.my_id))
        mutex.release()

        self.client_send()
        print('받을게요')
        # ['img_recv',file_size,내 id, 상대id,사진index]
        self.client_recv()
        # size = pickle.loads(self.ftp_sock.recv(1024))
        size = self.msg_list_server[1]
        recvd = 0
        print(size)
        fwrite = open('./id_'+self.msg_list_server[2]+'/match/id_'+self.msg_list_server[3]+'/me'+ str(pic_index) + '.jpg', 'wb')
        while size > recvd:
            print(recvd)
            # print(2)
            data = self.ftp_sock.recv(4096)
            # print(3)
            tmp = len(data)
            recvd = recvd + tmp
            fwrite.write(data)
            # print(tmp)
        fwrite.close()
        # ['img_recv',True or False,내id, 상대id,사진index]
        # self.client_recv()
        self.ftp_sock.close()
        self.ftp_server_addr = (self.host, self.ftp_port)
        self.ftp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ftp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # ['img_recv',내id,상대id,사진index]
    def client_ftp_recv_tmp(self):
        pic_index = self.msg_list[3]
        mutex = threading.Lock()
        mutex.acquire()
        self.ftp_sock.connect(self.ftp_server_addr)
        self.ftp_sock.send(pickle.dumps(self.my_id))
        mutex.release()

        self.client_send()
        print('받을게요')
        # ['img_recv',file_size,내 id, 상대id,사진index]
        self.client_recv()
        #size = pickle.loads(self.ftp_sock.recv(1024))
        size = self.msg_list_server[1]
        recvd=0
        print(size)
        fwrite = open('./tmp/tmp'+str(pic_index)+'.jpg', 'wb')
        while size > recvd:
            print(recvd)

            data = self.ftp_sock.recv(4096)

            tmp = len(data)
            recvd = recvd + tmp
            fwrite.write(data)

        fwrite.close()
        # ['img_recv',True or False,내id, 상대id,사진index]
        #self.client_recv()
        self.ftp_sock.close()
        self.ftp_server_addr = (self.host, self.ftp_port)
        self.ftp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ftp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def client_send(self):
        print("sending {0}".format(self.msg_list))
        #print(pickle.dumps(self.msg_list))
        self.sock.send(pickle.dumps(self.msg_list))  # send(bytes) returns the number of bytes sent
        self.instruction = ' '
        self.msg_list = []
        # self.client_recv()

    def client_recv(self):
        data = self.sock.recv(2048)
        data = pickle.loads(data)
        self.msg_list_server = copy.deepcopy(data)
        print(f'recv {data}')

    def img_send(self, file_path):
        f = open(file_path, 'rb')
        data = f.read()
        self.sock.send(pickle.dumps(len(data)))
        print(len(data))
        self.sock.send(data)
        f.close()
        print('보냄')

    def img_recv(self, file_bytes, file_name):
        pass

    def mkdir(self):
        dir_path = './id_' + self.msg_list_server[2]
        try:
            if not (os.path.isdir(dir_path)):
                os.makedirs(os.path.join(dir_path))
        except OSError:
            print('failed to mkdir' + self.msg_list_server[2])
            return
        try:
            if not (os.path.isdir(dir_path+'/match')):
                os.makedirs(os.path.join(dir_path+'/match'))

        except OSError:
            print('failed to mkdir' + self.msg_list_server[2]+'/match')
            return

    def img_resize(self,file_path):
        source_image = file_path
        target_image = './tmp/resized.jpg'
        image = Image.open(source_image)
        image = image.convert('RGB')
        image.save(target_image)
        # resize 할 이미지 사이즈
        resize_image = image.resize((330, 300))
        # 저장할 파일 Type : JPEG, PNG 등
        # 저장할 때 Quality 수준 : 보통 95 사용
        resize_image.save(target_image, mode='jpg', quality=95)

    def img_size(self,filepath):
        f = open(filepath,'rb')
        size = len(f.read())
        f.close()
        return size

    def client_chat_initiate(self,id_yours):
        self.chat_sock.connect(self.chat_server_addr)
        self.chat_sock.send(pickle.dumps([self.my_id,id_yours]))
        print(id_yours)

    #채팅서버로 부터 recv대기하는 스레드
    #recv가 발생하면 signal을 chat_uii에 보내서 값을 로컬에 저장하고 화면에 출력해주도록 함
    def run(self):
        while self.chat_recv_thread_stop:
            try:
                self.match_chat_recv()
                self.recv_msg_signal.emit()
            except:
                pass
        self.chat_recv_thread_stop = 1
        self.chat_server_addr = (self.host, self.chat_port)
        self.chat_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.chat_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print('채팅 리시브 스레드 종료')

