from db import database
import socket
import threading
import pickle
import os
import pymysql
import ftp_server
import chat_server



#resource_path('./id_' + self.editline_id.text() + '/match/match_candidate_list.txt')

class thread_server():
    def __init__(self):
        self.host = '127.0.0.1'
        self.host_ip = socket.gethostbyname(self.host)
        self.port = 5555
        self.server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server_socket.bind((self.host,self.port))
        self.server_socket.listen()
        self.client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        self.client_list={} # thread_object : client_socket

        self.mutex = threading.Lock()
        self.my_dir = os.getcwd()
        self.msg_list = []
        self.instruction=' '
        self.number_of_clients = 0

        self.host_ip = socket.gethostbyname(self.host)
        self.port = 7777
        self.chat_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.chat_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.chat_socket.bind((self.host, self.port))
        self.chat_socket.listen()

        self.on_chat_list = {} # 내 id : [chat_socket,대화하려는 상대id]

        self.chat_accept_thread = threading.Thread(target=self.accept_chat_client)
        self.chat_accept_thread.start()

        #self.count_thread = threading.Thread(target=self.count_clients, name=None)
        #self.count_thread.start()


        self.ftp_port = 6666
        self.ftp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ftp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.ftp_socket.bind((self.host, self.ftp_port))
        self.ftp_socket.listen()

        self.ftp_client_list = {} # 내 id : ftp_socket

        self.ftp_accept_thread = threading.Thread(target=self.accept_ftp_client)
        self.ftp_accept_thread.start()


        self.anonymous_chat_port = 4444
        self.anonymous_chat_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.anonymous_chat_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.anonymous_chat_socket.bind((self.host, self.anonymous_chat_port))
        self.anonymous_chat_socket.listen()

        self.anonymous_chat_1_m = []  # [내 id , anonymous_chat_socket]
        self.anonymous_chat_2_m = []  # [내 id , anonymous_chat_socket]
        self.anonymous_chat_3_m = []  # [내 id , anonymous_chat_socket]
        self.anonymous_chat_4_m = []  # [내 id , anonymous_chat_socket]

        self.anonymous_chat_1_f = []  # [내 id , anonymous_chat_socket]
        self.anonymous_chat_2_f = []  # [내 id , anonymous_chat_socket]
        self.anonymous_chat_3_f = []  # [내 id , anonymous_chat_socket]
        self.anonymous_chat_4_f = []  # [내 id , anonymous_chat_socket]

        self.anonymous_on_chat_list = {} # 내 id : chat_socket

        self.anonymous_accept_thread = threading.Thread(target=self.accept_anonymous_chat_client)
        self.anonymous_accept_thread.start()

        self.server_db = database()


    def accept_client(self):
        print('waiting for client')
        (self.client_socket, addr) = self.server_socket.accept()
        my_thread=threading.Thread(target=self.server_process, name=None, args=(self.client_socket,))

        self.mutex.acquire()
        self.client_list[my_thread] = [self.client_socket]
        self.mutex.release()

        my_thread.start()

    def accept_ftp_client(self):
        while True:
            print('ftp accept 시작!!!')
            (ftp_socket, addr) = self.ftp_socket.accept()
            self.mutex.acquire()
            id = pickle.loads(ftp_socket.recv(1024))
            self.ftp_client_list[id] = ftp_socket
            print(self.ftp_client_list)
            self.mutex.release()
            print('ftp연결 성공')

    def accept_chat_client(self):
        while True:
            print('chat connect를 시작')
            (chat_client_socket, addr) = self.chat_socket.accept()
            print('chat connect 완료')
            chat_obj = chat_server.chat()
            print('accept success')
            data = chat_client_socket.recv(4096)
            #info = [내id, 상대id]
            info = pickle.loads(data)
            my_thread = threading.Thread(target=chat_obj.process_chat_recv , name=None, args=(chat_client_socket,self.on_chat_list,info))

            self.mutex.acquire()
            self.on_chat_list[info[0]] = [chat_client_socket,info[1]]
            self.mutex.release()

            my_thread.start()
            print(self.on_chat_list[info[0]])
            print('나는 종료되면 안돼요')

    def accept_anonymous_chat_client(self):
        db = pymysql.connect(host='database-1.cpkdmxea5j3f.ap-northeast-2.rds.amazonaws.com', user='admin', password='12345678', db='project_db', charset='utf8')
        curs = db.cursor()
        mutex = threading.Lock()
        while True:
            #같은 선택지에 투표한 사람들과 매치되도록, (카운트 3초 후 매치되도록?)
            print('anonymous chat connect를 시작')
            (anonymous_chat_client_sock, addr) = self.anonymous_chat_socket.accept()
            print('anonymous chat connect 완료')
            anonymous_chat_obj = chat_server.chat()
            print('anonymous chat accept success')
            my_id = pickle.loads(anonymous_chat_client_sock.recv(1024))

            db.commit()
            sql = "select vote,gender from profile where id='"+my_id+"'"
            curs.execute(sql)
            result = curs.fetchall()[0]

            # vote 번호의 딕셔너리가 비어있지 않고, 나랑 다른 성별의 사람이 존재할 경우 start 신호를 두 소켓에 전달해주고, 스레드를 생성해줌
            # 해당되지 않으면 딕셔너리에 자신을 추가하고 accept대기
            if result[0] == 1:
                # 1번에 투표한 남성의 경우 anonymous_chat_1_f이 비어있으면 anonymous_chat_1_m에 자신을 추가하고 기다리고, 비어있지 않으면 스레드를 생성하고 통신시작
                if result[1] == '남성':

                    mutex.acquire()
                    # anonymous_chat_1_f이 비어있지 않을경우
                    if self.anonymous_chat_1_f:
                        # 리스트에 저장된 구조는 [ id, 소켓 ] 형태
                        # 상대 소켓도 넣어주는 이유는 좋아요 눌렀을떄 프로필이랑 사진 보내주려고
                        the_other_info = self.anonymous_chat_1_f.pop(0)

                        self.anonymous_on_chat_list[my_id] = anonymous_chat_client_sock
                        self.anonymous_on_chat_list[the_other_info[0]] = the_other_info[1]

                        # 내 소켓으로부터 recv 대기하는 스레드
                        anonymous_chat_accpet_thread_me = threading.Thread(target=anonymous_chat_obj.anonymous_chat_recv,args=(anonymous_chat_client_sock, the_other_info[1], the_other_info[0],my_id, self.anonymous_on_chat_list,self.anonymous_chat_1_m))
                        anonymous_chat_accpet_thread_me.start()

                        # 상대 소켓으로부터 recv 대기하는 스레드
                        anonymous_chat_accpet_thread_other = threading.Thread(target=anonymous_chat_obj.anonymous_chat_recv,args=(the_other_info[1], anonymous_chat_client_sock, my_id, the_other_info[0], self.anonymous_on_chat_list,self.anonymous_chat_1_f ))
                        anonymous_chat_accpet_thread_other.start()
                    #비어있을 경우
                    else:
                        self.anonymous_chat_1_m.append([my_id,anonymous_chat_client_sock])
                    mutex.release()
                        
                #남성이 아닌 여성의 경우
                else:
                    mutex.acquire()
                    if self.anonymous_chat_1_m:
                        # 리스트에 저장된 구조는 [ id, 소켓 ] 형태
                        # 상대 소켓도 넣어주는 이유는 좋아요 눌렀을떄 프로필이랑 사진 보내주려고
                        the_other_info = self.anonymous_chat_1_m.pop(0)

                        self.anonymous_on_chat_list[my_id] = anonymous_chat_client_sock
                        self.anonymous_on_chat_list[the_other_info[0]] = the_other_info[1]

                        # 내 소켓으로부터 recv 대기하는 스레드
                        anonymous_chat_accpet_thread_me = threading.Thread(target=anonymous_chat_obj.anonymous_chat_recv, args=(
                        anonymous_chat_client_sock, the_other_info[1], the_other_info[0],my_id, self.anonymous_on_chat_list,self.anonymous_chat_1_f))
                        anonymous_chat_accpet_thread_me.start()

                        # 상대 소켓으로부터 recv 대기하는 스레드
                        anonymous_chat_accpet_thread_other = threading.Thread(target=anonymous_chat_obj.anonymous_chat_recv,
                                                                           args=(
                                                                           the_other_info[1], anonymous_chat_client_sock,
                                                                           my_id,the_other_info[0], self.anonymous_on_chat_list,self.anonymous_chat_1_m))
                        anonymous_chat_accpet_thread_other.start()
                    # 비어있을 경우
                    else:
                        self.anonymous_chat_1_f.append([my_id, anonymous_chat_client_sock])
                    mutex.release()
            elif result[0] ==2:
                # 1번에 투표한 남성의 경우 anonymous_chat_1_f이 비어있으면 anonymous_chat_1_m에 자신을 추가하고 기다리고, 비어있지 않으면 스레드를 생성하고 통신시작
                if result[1] == '남성':
                    mutex.acquire()
                    # anonymous_chat_2_f이 비어있지 않을경우
                    if self.anonymous_chat_2_f:
                        # 리스트에 저장된 구조는 [ id, 소켓 ] 형태
                        # 상대 소켓도 넣어주는 이유는 좋아요 눌렀을떄 프로필이랑 사진 보내주려고
                        the_other_info = self.anonymous_chat_2_f.pop(0)

                        self.anonymous_on_chat_list[my_id] = anonymous_chat_client_sock
                        self.anonymous_on_chat_list[the_other_info[0]] = the_other_info[1]

                        # 내 소켓으로부터 recv 대기하는 스레드
                        anonymous_chat_accpet_thread_me = threading.Thread(target=anonymous_chat_obj.anonymous_chat_recv, args=(
                        anonymous_chat_client_sock, the_other_info[1], the_other_info[0],my_id, self.anonymous_on_chat_list,self.anonymous_chat_2_m))
                        anonymous_chat_accpet_thread_me.start()

                        # 상대 소켓으로부터 recv 대기하는 스레드
                        anonymous_chat_accpet_thread_other = threading.Thread(target=anonymous_chat_obj.anonymous_chat_recv,
                                                                           args=(
                                                                           the_other_info[1], anonymous_chat_client_sock,
                                                                           my_id,the_other_info[0], self.anonymous_on_chat_list,self.anonymous_chat_2_f))
                        anonymous_chat_accpet_thread_other.start()
                    # 비어있을 경우
                    else:
                        self.anonymous_chat_2_m.append([my_id, anonymous_chat_client_sock])
                    mutex.release()
                # 남성이 아닌 여성의 경우
                else:
                    mutex.acquire()
                    if self.anonymous_chat_2_m:
                        # 리스트에 저장된 구조는 [ id, 소켓 ] 형태
                        # 상대 소켓도 넣어주는 이유는 좋아요 눌렀을떄 프로필이랑 사진 보내주려고
                        the_other_info = self.anonymous_chat_2_m.pop(0)

                        self.anonymous_on_chat_list[my_id] = anonymous_chat_client_sock
                        self.anonymous_on_chat_list[the_other_info[0]] = the_other_info[1]

                        # 내 소켓으로부터 recv 대기하는 스레드
                        anonymous_chat_accpet_thread_me = threading.Thread(target=anonymous_chat_obj.anonymous_chat_recv, args=(
                            anonymous_chat_client_sock, the_other_info[1], the_other_info[0],my_id, self.anonymous_on_chat_list,self.anonymous_chat_2_f))
                        anonymous_chat_accpet_thread_me.start()

                        # 상대 소켓으로부터 recv 대기하는 스레드
                        anonymous_chat_accpet_thread_other = threading.Thread(target=anonymous_chat_obj.anonymous_chat_recv,
                                                                           args=(
                                                                               the_other_info[1],
                                                                               anonymous_chat_client_sock,
                                                                               my_id,the_other_info[0], self.anonymous_on_chat_list,self.anonymous_chat_2_m))
                        anonymous_chat_accpet_thread_other.start()
                    # 비어있을 경우
                    else:
                        self.anonymous_chat_2_f.append([my_id, anonymous_chat_client_sock])
                    mutex.release()
            elif result[0] == 3:
                # 1번에 투표한 남성의 경우 anonymous_chat_1_f이 비어있으면 anonymous_chat_1_m에 자신을 추가하고 기다리고, 비어있지 않으면 스레드를 생성하고 통신시작
                if result[1] == '남성':
                    mutex.acquire()
                    # anonymous_chat_3_f이 비어있지 않을경우
                    if self.anonymous_chat_3_f:
                        # 리스트에 저장된 구조는 [ id, 소켓 ] 형태
                        # 상대 소켓도 넣어주는 이유는 좋아요 눌렀을떄 프로필이랑 사진 보내주려고
                        the_other_info = self.anonymous_chat_3_f.pop(0)

                        self.anonymous_on_chat_list[my_id] = anonymous_chat_client_sock
                        self.anonymous_on_chat_list[the_other_info[0]] = the_other_info[1]

                        # 내 소켓으로부터 recv 대기하는 스레드
                        anonymous_chat_accpet_thread_me = threading.Thread(target=anonymous_chat_obj.anonymous_chat_recv, args=(
                        anonymous_chat_client_sock, the_other_info[1], the_other_info[0],my_id, self.anonymous_on_chat_list,self.anonymous_chat_3_m))
                        anonymous_chat_accpet_thread_me.start()

                        # 상대 소켓으로부터 recv 대기하는 스레드
                        anonymous_chat_accpet_thread_other = threading.Thread(target=anonymous_chat_obj.anonymous_chat_recv,
                                                                           args=(
                                                                           the_other_info[1], anonymous_chat_client_sock,
                                                                           my_id,the_other_info[0], self.anonymous_on_chat_list,self.anonymous_chat_3_f))
                        anonymous_chat_accpet_thread_other.start()
                    # 비어있을 경우
                    else:
                        self.anonymous_chat_3_m.append([my_id, anonymous_chat_client_sock])
                    mutex.release()
                # 남성이 아닌 여성의 경우
                else:
                    mutex.acquire()
                    if self.anonymous_chat_3_m:
                        # 리스트에 저장된 구조는 [ id, 소켓 ] 형태
                        # 상대 소켓도 넣어주는 이유는 좋아요 눌렀을떄 프로필이랑 사진 보내주려고
                        the_other_info = self.anonymous_chat_3_m.pop(0)

                        self.anonymous_on_chat_list[my_id] = anonymous_chat_client_sock
                        self.anonymous_on_chat_list[the_other_info[0]] = the_other_info[1]

                        # 내 소켓으로부터 recv 대기하는 스레드
                        anonymous_chat_accpet_thread_me = threading.Thread(target=anonymous_chat_obj.anonymous_chat_recv, args=(
                            anonymous_chat_client_sock, the_other_info[1], the_other_info[0],my_id, self.anonymous_on_chat_list,self.anonymous_chat_3_f))
                        anonymous_chat_accpet_thread_me.start()

                        # 상대 소켓으로부터 recv 대기하는 스레드
                        anonymous_chat_accpet_thread_other = threading.Thread(target=anonymous_chat_obj.anonymous_chat_recv,
                                                                           args=(
                                                                               the_other_info[1],
                                                                               anonymous_chat_client_sock,
                                                                               my_id,the_other_info[0], self.anonymous_on_chat_list,self.anonymous_chat_3_m))
                        anonymous_chat_accpet_thread_other.start()
                    # 비어있을 경우
                    else:
                        self.anonymous_chat_3_f.append([my_id, anonymous_chat_client_sock])
                    mutex.release()
            elif result[0] == 4:
                # 1번에 투표한 남성의 경우 anonymous_chat_1_f이 비어있으면 anonymous_chat_1_m에 자신을 추가하고 기다리고, 비어있지 않으면 스레드를 생성하고 통신시작
                if result[1] == '남성':
                    mutex.acquire()
                    # anonymous_chat_4_f이 비어있지 않을경우
                    if self.anonymous_chat_4_f:
                        # 리스트에 저장된 구조는 [ id, 소켓 ] 형태
                        # 상대 소켓도 넣어주는 이유는 좋아요 눌렀을떄 프로필이랑 사진 보내주려고
                        the_other_info = self.anonymous_chat_4_f.pop(0)

                        self.anonymous_on_chat_list[my_id] = anonymous_chat_client_sock
                        self.anonymous_on_chat_list[the_other_info[0]] = the_other_info[1]

                        # 내 소켓으로부터 recv 대기하는 스레드
                        anonymous_chat_accpet_thread_me = threading.Thread(target=anonymous_chat_obj.anonymous_chat_recv, args=(
                        anonymous_chat_client_sock, the_other_info[1], the_other_info[0],my_id, self.anonymous_on_chat_list,self.anonymous_chat_4_m))
                        anonymous_chat_accpet_thread_me.start()

                        # 상대 소켓으로부터 recv 대기하는 스레드
                        anonymous_chat_accpet_thread_other = threading.Thread(target=anonymous_chat_obj.anonymous_chat_recv,
                                                                           args=(
                                                                           the_other_info[1], anonymous_chat_client_sock,
                                                                           my_id,the_other_info[0], self.anonymous_on_chat_list,self.anonymous_chat_4_f))
                        anonymous_chat_accpet_thread_other.start()
                    # 비어있을 경우
                    else:
                        self.anonymous_chat_4_m.append([my_id, anonymous_chat_client_sock])
                    mutex.release()
                # 남성이 아닌 여성의 경우
                else:
                    mutex.acquire()
                    if self.anonymous_chat_4_m:
                        # 리스트에 저장된 구조는 [ id, 소켓 ] 형태
                        # 상대 소켓도 넣어주는 이유는 좋아요 눌렀을떄 프로필이랑 사진 보내주려고
                        the_other_info = self.anonymous_chat_4_m.pop(0)

                        self.anonymous_on_chat_list[my_id] = anonymous_chat_client_sock
                        self.anonymous_on_chat_list[the_other_info[0]] = the_other_info[1]

                        # 내 소켓으로부터 recv 대기하는 스레드
                        anonymous_chat_accpet_thread_me = threading.Thread(target=anonymous_chat_obj.anonymous_chat_recv, args=(
                            anonymous_chat_client_sock, the_other_info[1], the_other_info[0],my_id, self.anonymous_on_chat_list,self.anonymous_chat_4_f))
                        anonymous_chat_accpet_thread_me.start()

                        # 상대 소켓으로부터 recv 대기하는 스레드
                        anonymous_chat_accpet_thread_other = threading.Thread(target=anonymous_chat_obj.anonymous_chat_recv,
                                                                           args=(
                                                                               the_other_info[1],
                                                                               anonymous_chat_client_sock,
                                                                               my_id,the_other_info[0], self.anonymous_on_chat_list,self.anonymous_chat_4_m))
                        anonymous_chat_accpet_thread_other.start()
                    # 비어있을 경우
                    else:
                        self.anonymous_chat_4_f.append([my_id, anonymous_chat_client_sock])
                    mutex.release()
            print('나는 종료되면 안돼요')


    def server_recv(self,clntsock):  # instruction receive
        try:
            print('waiting to recv message from client')
            data_recv=clntsock.recv(2048)
            data=pickle.loads(data_recv)
            print(data)

            if data[0] == 'close_thread':
                db = pymysql.connect(host='database-1.cpkdmxea5j3f.ap-northeast-2.rds.amazonaws.com', user='admin', password='12345678', db='project_db', charset='utf8')
                curs = db.cursor()
                curs.execute("update profile set online=0 where id=%s",(data[1],))
                db.commit()
                db.close()
                return False
            elif data[0] == 'exit_login':
                return False
            elif data[0] == 'img_send':
                ftp_obj = ftp_server.ftp()
                ftp_recv_thread = threading.Thread(target=ftp_obj.img_recv,args=(data,self.ftp_client_list,))
                ftp_recv_thread.start()

            elif data[0] == 'img_recv':
                ftp_obj = ftp_server.ftp()
                ftp_recv_thread = threading.Thread(target=ftp_obj.img_send, args=(data, self.ftp_client_list,clntsock))
                ftp_recv_thread.start()
                return True

            elif data[0] == 'ftp_recv_talk':
                ftp_obj = ftp_server.ftp()
                ftp_recv_thread = threading.Thread(target=ftp_obj.ftp_send_talk, args=(data, self.ftp_client_list, clntsock))
                ftp_recv_thread.start()
                return True

            elif data[0] == 'remove_list_element':
                print('remove_list_element')
                self.remove_list_element(data)

            self.server_db.get_data(data,self.client_list)
            if data[0]=='count_users':
                data.append(len(self.client_list))
            self.server_send(data,clntsock)
            return True

        except Exception as e:
            print('메인 스레드 비정상 종료')
            return False





    def server_send(self, data_list, clntsock):
        #cur_thread = threading.current_thread()
        #clntsock=self.client_list[cur_thread]
        print(f'sending {data_list}')
        clntsock.send(pickle.dumps(data_list))

    #thread running function
    def server_process(self,clntsock):
        while self.server_recv(clntsock):
            pass
        try:
            my_thread=threading.currentThread()
            self.mutex.acquire()
            self.client_list[my_thread][0].close()
            sql = "update profile set online=0 where id='" + self.client_list[my_thread][1] + "'"
            self.server_db.curs.execute(sql)
            self.server_db.db.commit()
            self.remove_list_element(['remove_list_element',self.client_list[my_thread][1]])
            del (self.client_list[my_thread])
            self.mutex.release()
        except:
            print('성공적')
            del (self.client_list[my_thread])
            self.mutex.release()
        print(self.anonymous_chat_1_f)
        print(self.anonymous_chat_1_m)
        print(self.anonymous_chat_2_f)
        print(self.anonymous_chat_2_m)
        print(self.anonymous_chat_3_f)
        print(self.anonymous_chat_3_m)
        print(self.anonymous_chat_4_f)
        print(self.anonymous_chat_4_m)
        print(self.anonymous_on_chat_list)
        print('thread ends')

    def count_clients(self):
        while True:
            self.mutex.acquire()
            self.number_of_clients = len(self.client_list)
            self.mutex.release()
            #print(self.number_of_clients)

    # ['remove_list_element', 내id]
    def remove_list_element(self, data_list):
        db = pymysql.connect(host='database-1.cpkdmxea5j3f.ap-northeast-2.rds.amazonaws.com', user='admin', password='12345678', db='project_db', charset='utf8')
        curs = db.cursor()
        mutex = threading.Lock()
        db.commit()
        sql = "select vote,gender from profile where id='" + data_list[1] + "'"
        curs.execute(sql)
        result = curs.fetchall()[0]
        mutex.acquire()
        print(self.anonymous_chat_1_m)
        if result[0] == 1:
            if result[1] == '남성':
                idx = -1
                for item in self.anonymous_chat_1_m:
                    if item[0] == data_list[1]:
                        idx = self.anonymous_chat_1_m.index(item)
                if idx != -1:
                    list = self.anonymous_chat_1_m.pop(idx)
                    list[1].close()
                    mutex.release()
                    return
            else:
                idx = -1
                for item in self.anonymous_chat_1_f:
                    if item[0] == data_list[1]:
                        idx = self.anonymous_chat_1_f.index(item)
                if idx != -1:
                    list = self.anonymous_chat_1_f.pop(idx)
                    list[1].close()
                    mutex.release()
                    return

        elif result[0] == 2:
            if result[1] == '남성':
                idx = -1
                for item in self.anonymous_chat_2_m:
                    if item[0] == data_list[1]:
                        idx = self.anonymous_chat_2_m.index(item)
                if idx != -1:
                    list = self.anonymous_chat_2_m.pop(idx)
                    list[1].close()
                    mutex.release()
                    return
            else:
                idx = -1
                for item in self.anonymous_chat_2_f:
                    if item[0] == data_list[1]:
                        idx = self.anonymous_chat_2_f.index(item)
                if idx != -1:
                    list = self.anonymous_chat_2_f.pop(idx)
                    list[1].close()
                    mutex.release()
                    return
        elif result[0] == 3:
            if result[1] == '남성':
                idx = -1
                for item in self.anonymous_chat_3_m:
                    if item[0] == data_list[1]:
                        idx = self.anonymous_chat_3_m.index(item)
                if idx != -1:
                    list = self.anonymous_chat_3_m.pop(idx)
                    list[1].close()
                    mutex.release()
                    return
            else:
                idx = -1
                for item in self.anonymous_chat_3_f:
                    if item[0] == data_list[1]:
                        idx = self.anonymous_chat_3_f.index(item)
                if idx != -1:
                    list = self.anonymous_chat_3_f.pop(idx)
                    list[1].close()
                    mutex.release()
                    return
        elif result[0] == 4:
            if result[1] == '남성':
                idx = -1
                for item in self.anonymous_chat_4_m:
                    if item[0] == data_list[1]:
                        idx = self.anonymous_chat_4_m.index(item)
                if idx != -1:
                    list = self.anonymous_chat_4_m.pop(idx)
                    list[1].close()
                    mutex.release()
                    return
            else:
                idx = -1
                for item in self.anonymous_chat_4_f:
                    if item[0] == data_list[1]:
                        idx = self.anonymous_chat_4_f.index(item)
                if idx != -1:
                    list = self.anonymous_chat_4_f.pop(idx)
                    list[1].close()
                    mutex.release()
                    return
        self.anonymous_on_chat_list[data_list[1]].close()
        del (self.anonymous_on_chat_list[data_list[1]])
        mutex.release()



if __name__=='__main__':
    server=thread_server()
    while True:
        server.accept_client()




