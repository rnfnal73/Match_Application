import pickle
import threading
import pymysql

#resource_path('./id_' + self.editline_id.text() + '/match/match_candidate_list.txt')

class chat():
    def __init__(self):
        pass

    # 클라이언트로부터 recv를 받게되면 상대가 online인지 확인하고
    # online이면 , offline이면
    def process_chat_recv(self, chat_socket, on_chat_list, info):
        db = pymysql.connect(host='database-1.cpkdmxea5j3f.ap-northeast-2.rds.amazonaws.com', user='admin', password='12345678', db='project_db', charset='utf8')
        curs = db.cursor()

        mutex = threading.Lock()
        mutex.acquire()
        sql = "update profile set on_chat=1 where id='" + info[0] + "'"
        print(sql)
        curs.execute(sql)
        db.commit()
        mutex.release()

        while True:
            try:
                recvd = chat_socket.recv(4096)
                data = pickle.loads(recvd)

                mutex.acquire()
                print(data)
                print(info[1])
                #상대가 대화를 종료했을때

                #클라이언트로부터 종료 요청이오면 on_chat_list에서 삭제하고,on_chat=0 으로 수정, 스레드 종료
                if data[0]=='chat_end':
                    sql = "update profile set on_chat=0 where id='" + info[0] + "'"
                    curs.execute(sql)
                    db.commit()
                    on_chat_list[info[0]][0].close()
                    del(on_chat_list[info[0]])
                    print('chat end')
                    mutex.release()
                    break

                db.commit()
                sql = "select on_chat from profile where id='" + info[1] + "'"
                curs.execute(sql)
                result = curs.fetchall()


                print(result)
                if result:
                    fwrite = open('./id_' + info[0] + '/match/id_' + info[1] + '.txt', 'a')
                    fwrite.write('me: ' + data[0] + '\n')
                    fwrite.close()

                    fwrite = open('./id_' + info[1] + '/match/id_' + info[0] + '.txt', 'a')
                    fwrite.write(info[0] + ': ' + data[0] + '\n')
                    fwrite.close()

                    # 상대가 on_chat일때, 상대 client로 전송
                    if result[0][0] == 1 and info[0] == on_chat_list[info[1]][1]:
                        print('상대에게전송')
                        try:
                            otherside_sock = on_chat_list[info[1]][0]  # 상대 chat_client_socket
                            otherside_sock.send(pickle.dumps(data))
                            print('상대에게전송_done')
                            mutex.release()
                        except:
                            print('lock!')
                            fwrite = open('./id_' + info[0] + '/match/id_' + info[1] + '.txt', 'a')
                            fwrite.write('me: ' + data[0] + '\n')
                            fwrite.close()
                            print('mid')
                            fwrite = open('./id_' + info[1] + '/match/id_' + info[0] + '.txt', 'a')
                            fwrite.write(info[0] + ': ' + data[0] + '\n')
                            fwrite.close()
                            mutex.release()
                            print('상대의 접속이 종료됨')

                    # 상대가 off_chat일때, new_talk = 1로
                    else:
                        sql = "update id_" + info[1] + " set new_talk=1 where id='" + info[0] + "'"
                        print(sql)
                        curs.execute(sql)
                        db.commit()
                        mutex.release()

            except:
                print('매치 채팅 스레드 비정상 종료')
                sql = "update profile set on_chat=0 where id='" + info[0] + "'"
                curs.execute(sql)
                db.commit()
                on_chat_list[info[0]][0].close()
                del (on_chat_list[info[0]])
                break


        print(f'id {info[0]}의 채팅 스레드가 종료됨')

    # anonymous_chat_client_sock, the_other_sock, 상대 아이디,내아이디
    def anonymous_chat_recv(self, my_sock, the_other_sock, id_other,my_id, anonymous_on_chat_list ,anonymous_chat_list):
        _send = []
        _send.append('start')
        _send.append(id_other)
        my_sock.send(pickle.dumps(_send))

        while True:
            try:
                print(f'anonymous chatting {id_other}로 부터 시작')
                data = pickle.loads(my_sock.recv(4096))
                print(data)

                #상대가 대화를 종료했을때
                #내 소켓으로부터 온 'chat_end'요청으로 스레드만 종료해줌
                if data[0]=='chat_end':
                    my_sock.close()
                    break

                #클라이언트로부터 종료 요청이오면 상대 소켓으로 'end' 보내고, 스레드 종료
                elif data[0]=='end':
                    str = []
                    str2 = []
                    str.append('end')
                    str2.append('no connection')
                    the_other_sock.send(pickle.dumps(str2))
                    my_sock.send(pickle.dumps(str))
                    my_sock.close()
                    break

                else:
                    print('상대에게전송')  # 상대 chat_client_socket
                    the_other_sock.send(pickle.dumps(data))
                    print(data)
                    print('상대에게전송_done')
            except:
                mutex = threading.Lock()
                mutex.acquire()
                idx = -1
                for item in anonymous_chat_list:
                    if item[0] == my_id:
                        idx = anonymous_chat_list.index(item)
                if idx != -1:
                    list = anonymous_chat_list.pop(idx)
                    list[1].close()
                    mutex.release()
                    break
                anonymous_on_chat_list[my_id].close()
                del (anonymous_on_chat_list[my_id])
                mutex.release()
                break
        print('익명 채팅 스레드 비정상 종료')