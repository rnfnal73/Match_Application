import pickle
import threading

class ftp():
    def __init__(self):
        pass

    # ['img_send', 내 id, 이미지 size, 사진인덱스]
    def img_recv(self,data_list,ftp_client_list):
        mutex = threading.Lock()
        mutex.acquire()
        ftp_client_socket = ftp_client_list[data_list[1]]
        mutex.release()
        size = data_list[2]
        recvd = 0
        fwrite = open('./id_' + data_list[1]+'/me'+str(data_list[3])+'.jpg','wb')

        while size > recvd:
            data = ftp_client_socket.recv(4096)
            tmp = len(data)
            recvd = recvd+ tmp
            fwrite.write(data)
            print(tmp)

        fwrite.close()

        ftp_client_socket.close()
        mutex.acquire()
        del(ftp_client_list[data_list[1]])
        mutex.release()

        # ['img_send',True or False, 내 id, 이미지 size, 사진인덱스]
        data_list.insert(1, True)

    # ['img_recv',내 id, 사진 가져갈 id, 사진index]
    def img_send(self,data_list,ftp_client_list,clntsock):
        mutex = threading.Lock()
        mutex.acquire()
        ftp_client_socket = ftp_client_list[data_list[1]]
        mutex.release()
        print('보낼게요')
        fread = open('./id_' + data_list[2]+'/me'+str(data_list[3])+'.jpg','rb')
        data = fread.read()
        fread.close()
        # ['img_recv',file_size,내 id, 상대id,사진index]
        data_list.insert(1, len(data))
        clntsock.send(pickle.dumps(data_list))
        ftp_client_socket.send(data)

        ftp_client_socket.close()
        mutex.acquire()
        del (ftp_client_list[data_list[2]])
        mutex.release()


    def ftp_send_talk(self,data_list, ftp_client_list, clntsock):
        mutex = threading.Lock()
        mutex.acquire()
        ftp_client_socket = ftp_client_list[data_list[1]]
        mutex.release()

        fread = open('./id_' + data_list[1]+'/match/id_'+data_list[2]+'.txt','rb')
        data = fread.read()
        fread.close()
        print(len(data))
        self.ftp_send(data,ftp_client_socket)
        #ftp_client_socket.send(pickle.dumps(data))

        ftp_client_socket.close()
        mutex.acquire()
        del (ftp_client_list[data_list[1]])
        mutex.release()

    def ftp_send(self,fread,ftp_client_socket):
        self.sending = ''
        if len(fread) > 1000:
            print(len(fread))
            self.sending = fread[0:1000]
            fread = fread[1000:len(fread)]
            ftp_client_socket.send(self.sending)
            self.ftp_send(fread,ftp_client_socket)
        else:

            ftp_client_socket.send(fread)


