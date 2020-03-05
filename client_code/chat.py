from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QThread
import pickle
import socket
import os

class anonymous_chat_ui(QtWidgets.QDialog):
    start_main_signal = QtCore.pyqtSignal()
    def __init__(self,_client,parent=None):
        super(anonymous_chat_ui, self).__init__(parent)
        self._client = _client

        self.anonymous_chat_recv = anonymous_chat_worker(self._client, self._client.anonymous_chat_sock)
        self.anonymous_chat_recv.start_signal.connect(self.enable_buttons)
        self.anonymous_chat_recv.back_signal.connect(self.ui_close)
        self.anonymous_chat_recv.clear_signal.connect(self.clear_show)
        self.anonymous_chat_recv.append_signal.connect(self.chat_append)
        self.anonymous_chat_recv.abnormal_exit_signal.connect(self.set_back_flag)

        self.back_flag = 1
        #self.anonymous_chat_recv.append_signal.connect(self.chat_append)
        #self._client.recv_msg_signal.connect(self.process_recv_msg)
        self.setupUi()

    def setupUi(self):
        # disable (but not hide) close button
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)

        self.setObjectName("Dialog")
        self.resize(570, 429)
        self.chat_insert = QtWidgets.QTextEdit(self)
        self.chat_insert.setGeometry(QtCore.QRect(0, 360, 361, 71))
        self.chat_insert.setObjectName("chat_insert")
        self.like_button = QtWidgets.QPushButton(self)
        self.like_button.setGeometry(QtCore.QRect(500, 360, 71, 71))
        self.like_button.setObjectName("back_button")
        self.chat_show = QtWidgets.QTextEdit(self)
        self.chat_show.setGeometry(QtCore.QRect(0, 0, 571, 361))
        self.chat_show.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.chat_show.setObjectName("chat_show")
        self.back_button = QtWidgets.QPushButton(self)
        self.back_button.setGeometry(QtCore.QRect(430, 360, 71, 71))
        self.back_button.setObjectName("like_button")
        self.send_button = QtWidgets.QPushButton(self)
        self.send_button.setGeometry(QtCore.QRect(360, 360, 71, 71))
        self.send_button.setObjectName("send_button")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.back_button.clicked.connect(self.back_button_clicked)
        self.send_button.clicked.connect(self.send_button_clicked)
        self.like_button.clicked.connect(self.like_button_clicked)

    def set_back_flag(self):
        self.back_flag = -1

    def abnormal_ui_close(self):
        self._client.number_of_widgets = self._client.number_of_widgets - 1
        self._client.anonymous_chat_sock.close()
        self.close()
        self._client.anonymous_chat_server_addr = (self._client.host, self._client.anonymous_chat_port)
        self._client.anonymous_chat_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._client.anonymous_chat_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.anonymous_chat_recv.anonymous_chat_sock = self._client.anonymous_chat_sock

        self.start_main_signal.emit()

    def ui_close(self):
        self._client.number_of_widgets = self._client.number_of_widgets - 1
        self._client.anonymous_chat_sock.close()
        self.close()
        self._client.anonymous_chat_server_addr = (self._client.host, self._client.anonymous_chat_port)
        self._client.anonymous_chat_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._client.anonymous_chat_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.anonymous_chat_recv.anonymous_chat_sock = self._client.anonymous_chat_sock

        self._client.msg_list.append('remove_list_element')
        self._client.msg_list.append(self._client.my_id)
        #['remove_list_element', 내id]
        self._client.client_send()
        self._client.client_recv()

        self.start_main_signal.emit()


    def clear_show(self):
        #self.chat_show.clear()
        #self.chat_insert.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.chat_show.append('상대가 접속을 종료했습니다')
        self.send_button.setEnabled(False)
        self.like_button.setEnabled(False)
        self.back_flag = 0
        print('well cleared')

    def enable_buttons(self):
        self.chat_show.setText('대화를 시작해보세요')
        self.send_button.setEnabled(True)
        self.like_button.setEnabled(True)
        self.back_flag = 1

    def ui_show(self):
        self.chat_show.setText('대화 상대를 기다리는 중입니다')
        self.send_button.setEnabled(False)
        self.like_button.setEnabled(False)
        self._client.number_of_widgets = self._client.number_of_widgets + 1
        self.back_flag = 0
        self.show()

    def chat_append(self):
        str = self._client.anonymous_chat_buffer
        self.chat_show.append('상대방: ' + str)
        self._client.anonymous_chat_buffer = ''

    def send_button_clicked(self):
        data = self.chat_insert.toPlainText()
        self.chat_send([data])
        self.chat_insert.clear()

    def chat_send(self,data):
        # 전송하려는 글자 수가 1000이 넘어가면 나눠서 보냄
        # 전체 문자열에서 1000글자를 잘라내서 보내고, 나머지 문자열에 대해 재귀실행
        self.sending = data[0]
        if len(self.sending) >1000:
            tmp = self.sending[0:1000]
            self.sending = self.sending[1000:len(self.sending)]
            self._client.anonymous_chat_sock.send(pickle.dumps([tmp]))
            print(f'나눠서보냄 {tmp}')
            print(len(self.sending))
            self.chat_show.append('나: '+tmp)
            self.chat_send([self.sending])
        else:
            self._client.anonymous_chat_sock.send(pickle.dumps([self.sending]))
            self.chat_show.append('나: '+self.sending)
            print(data)
            print('그냥 보냄')

    #상대 아이디 이용해서 상대 프로필이랑 사진 받아서 폴더만들어 저장하고, 매치가능성 리스트에 추가
    #매치가능성 리스트, 매치 리스트에 있는지 없는지 확인한 후 추가해줘야 함
    def like_button_clicked(self):
        fread = open('./id_' + self._client.my_id + '/match/match_candidate_list.txt', 'rb')
        match_list = pickle.loads(fread.read())
        fread.close()

        self.like_button.setEnabled(False)

        #매치 리스트가 비어있지 않을때
        if match_list:
            for item in match_list:
                if item == self._client.id_other:
                    pass
                else:
                    # [ 'get_profile' , 내 id, 프로필을 받아갈 id ]
                    self._client.msg_list.append('get_profile')
                    self._client.msg_list.append(self._client.my_id)
                    self._client.msg_list.append(self._client.id_other)
                    self._client.client_send()
                    # [ 'get_profile' ,True or False, 내 id, 프로필을 받아갈 id ,[ 닉네임, 거주지, 취미, 나이, 성별, 자기소개 ] ]
                    self._client.client_recv()

                    if self._client.msg_list_server[1]:
                        try:
                            if not (
                            os.path.isdir('./id_' + self._client.my_id + '/match/id_' + self._client.id_other)):
                                os.makedirs(os.path.join(
                                    './id_' + self._client.my_id + '/match/id_' + self._client.id_other))
                        except OSError:
                            print('failed to mkdir' + 'id_' + self._client.id_other)
                            return

                        match_list.append(self._client.id_other)
                        fwrite = open('./id_' + self._client.my_id + '/match/match_candidate_list.txt', 'wb')
                        fwrite.write(pickle.dumps(match_list))
                        fwrite.close()

                        f = open('./id_' + self._client.my_id + '/match/id_' + self._client.id_other + '/profile.txt', 'wb')
                        f.write(pickle.dumps(self._client.msg_list_server[4]))
                        f.close()

                        # ['img_recv',내id,상대id,사진index]
                        self._client.msg_list.append('img_recv')
                        self._client.msg_list.append(self._client.my_id)
                        self._client.msg_list.append(self._client.id_other)
                        self._client.msg_list.append(1)
                        self._client.client_ftp_recv()

                        self._client.msg_list.append('img_recv')
                        self._client.msg_list.append(self._client.my_id)
                        self._client.msg_list.append(self._client.id_other)
                        self._client.msg_list.append(2)
                        self._client.client_ftp_recv()

                        self._client.msg_list.append('img_recv')
                        self._client.msg_list.append(self._client.my_id)
                        self._client.msg_list.append(self._client.id_other)
                        self._client.msg_list.append(3)
                        self._client.client_ftp_recv()
        # 매치리스트가 비어있을때
        else:
            # [ 'get_profile' , 내 id, 프로필을 받아갈 id ]
            self._client.msg_list.append('get_profile')
            self._client.msg_list.append(self._client.my_id)
            self._client.msg_list.append(self._client.id_other)
            self._client.client_send()
            # [ 'get_profile' ,True or False, 내 id, 프로필을 받아갈 id ,[ 닉네임, 거주지, 취미, 나이, 성별, 자기소개 ] ]
            self._client.client_recv()

            if self._client.msg_list_server[1]:
                try:
                    if not (
                            os.path.isdir('./id_' + self._client.my_id + '/match/id_' + self._client.id_other)):
                        os.makedirs(os.path.join(
                            './id_' + self._client.my_id + '/match/id_' + self._client.id_other))
                except OSError:
                    print('failed to mkdir' + 'id_' + self._client.id_other)
                    return

                match_list.append(self._client.id_other)
                fwrite = open('./id_' + self._client.my_id + '/match/match_candidate_list.txt', 'wb')
                fwrite.write(pickle.dumps(match_list))
                fwrite.close()

                f = open('./id_' + self._client.my_id + '/match/id_' + self._client.id_other + '/profile.txt', 'wb')
                f.write(pickle.dumps(self._client.msg_list_server[4]))
                f.close()

                # ['img_recv',내id,상대id,사진index]
                self._client.msg_list.append('img_recv')
                self._client.msg_list.append(self._client.my_id)
                self._client.msg_list.append(self._client.id_other)
                self._client.msg_list.append(1)
                self._client.client_ftp_recv()

                self._client.msg_list.append('img_recv')
                self._client.msg_list.append(self._client.my_id)
                self._client.msg_list.append(self._client.id_other)
                self._client.msg_list.append(2)
                self._client.client_ftp_recv()

                self._client.msg_list.append('img_recv')
                self._client.msg_list.append(self._client.my_id)
                self._client.msg_list.append(self._client.id_other)
                self._client.msg_list.append(3)
                self._client.client_ftp_recv()



    def back_button_clicked(self):
        if self.back_flag == 1:
            end_msg = pickle.dumps(['end'])
            self._client.anonymous_chat_sock.send(end_msg)
        elif self.back_flag == 0:
            self.ui_close()

        elif self.back_flag == -1:
            self.abnormal_ui_close()

    def anonymous_chat_initiate(self):
        #['check_vote',내id]
        self._client.msg_list.append('check_vote')
        self._client.msg_list.append(self._client.my_id)
        self._client.client_send()
        #['check_vote',True or False, 내id]
        self._client.client_recv()
        if self._client.msg_list_server[1]:
            self._client.anonymous_chat_sock.connect(self._client.anonymous_chat_server_addr)
            self._client.anonymous_chat_sock.send(pickle.dumps(self._client.my_id))
            print('anonymous chat connected')
            self.ui_show()
            self.anonymous_chat_recv.start()
        else:
            QtWidgets.QMessageBox.about(self, 'no vote', '먼저 투표를 해주세요')
            self.start_main_signal.emit()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "익명 채팅"))
        self.chat_insert.setText(_translate("Dialog", ""))
        self.like_button.setText(_translate("Dialog", "좋아요"))
        self.chat_show.setText(_translate("Dialog", "대화를 시작해보세요"))
        self.back_button.setText(_translate("Dialog", "나가기"))
        self.send_button.setText(_translate("Dialog", "전송"))


class anonymous_chat_worker(QThread, QtCore.QObject):
    start_signal = QtCore.pyqtSignal()
    append_signal = QtCore.pyqtSignal()
    back_signal = QtCore.pyqtSignal()
    clear_signal = QtCore.pyqtSignal()
    abnormal_exit_signal = QtCore.pyqtSignal()
    def __init__(self,_client,sock):
        super().__init__()
        #self.anonymous_obj = anonymous_obj
        self._client = _client
        self.anonymous_chat_sock = sock

    # 채팅서버로 부터 recv대기하는 스레드
    # recv가 발생하면 화면에 출력해주도록 함
    def run(self):
        print('start of recv thread')
        while True:
            try:
                data = pickle.loads(self.anonymous_chat_sock.recv(1024))
                print(data)
                # 랜덤채팅 ui를 띄워줌
                if data[0] == 'start':
                    print('show')
                    #상대 아이디 받기
                    self._client.id_other = data[1]

                    self.start_signal.emit()
                # 채팅 ui를 닫아주고 그 사후처리
                elif data[0] == 'end':
                    self.back_signal.emit()
                    print('랜덤 채팅 리시브 스레드 종료')
                    break
                elif data[0]=='no connection':
                    self._client.anonymous_chat_sock.send(pickle.dumps(['chat_end']))
                    #나가기 버튼만 활성화 하고 채팅할 상대가 없다는 말만 뜨게함
                    self.clear_signal.emit()
                    print('랜덤 채팅 리시브 스레드 종료 그리고 채팅창 비활성화!')
                    break
                # 받은 내용을 ui에 출력해줌
                else:
                    print(data)
                    #self.anonymous_obj.chat_show.append('상대방: ' + data)
                    self._client.anonymous_chat_buffer = data[0]
                    self.append_signal.emit()
            except:
                print('상대가 비정상 종료')
                self.clear_signal.emit()
                self.abnormal_exit_signal.emit()
                break


class match_chat_ui(QtWidgets.QDialog):
    def __init__(self, _client, parent=None):
        super(match_chat_ui, self).__init__(parent)
        self._client=_client
        self._client.recv_msg_signal.connect(self.process_recv_msg)
        self.id_yours = ''
        self.setupUi()

    def setupUi(self):
        # disable (but not hide) close button
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)

        self.setObjectName("Form")
        self.resize(570, 430)
        self.chat_text_edit = QtWidgets.QTextEdit(self)
        self.chat_text_edit.setGeometry(QtCore.QRect(0, 360, 430, 70))
        self.chat_text_edit.setObjectName("chat_text_edit")

        self.send_button = QtWidgets.QPushButton(self)
        self.send_button.setGeometry(QtCore.QRect(430, 360, 70, 70))
        self.send_button.setObjectName("send_button")

        self.back_button = QtWidgets.QPushButton(self)
        self.back_button.setGeometry(QtCore.QRect(500, 360, 70, 70))
        self.back_button.setObjectName("back_button")

        self.chat_text_show = QtWidgets.QTextEdit(self)
        self.chat_text_show.setGeometry(QtCore.QRect(0, 0, 571, 361))
        self.chat_text_show.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.chat_text_show.setObjectName("chat_text_show")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.back_button.clicked.connect(self.back_button_clicked)
        self.send_button.clicked.connect(self.send_button_clicked)

    # 서버로 부터 갱신된 대화내용을 받아서 저장하고 초기화면에 띄워주는 함수
    def initiate_chat(self):
        #['new_talk', 내id, 매치 상대id]
        self._client.msg_list.append('new_talk')
        self._client.msg_list.append(self._client.my_id)
        self._client.msg_list.append(self.id_yours)
        self._client.client_send()

        # ['new_talk', True or False, (True이면 받을 매치대화 파일 사이즈),내id, 매치 상대id]
        self._client.client_recv()

        if not os.path.isfile('./id_' + self._client.my_id + '/match/id_' + self.id_yours+'/match_talk.txt'):
            f = open('./id_' + self._client.my_id + '/match/id_' + self.id_yours+'/match_talk.txt','w')
            f.write('매치되었습니다. 대화를 시작해보세요!\n')
            f.close()

        #갱신된 값이 있으면 새로 받아서 저장
        if self._client.msg_list_server[1]:
            new_talk = self._client.ftp_recv_talk(self._client.msg_list_server[2],self._client.msg_list_server[4])
            fwrite = open('./id_' + self._client.my_id + '/match/id_' + self.id_yours+'/match_talk.txt','w')
            fwrite.write(new_talk)
            fwrite.close()
        #여태까지 저장된 매치 대화를 읽어서 화면에 출력
        fread = open('./id_' + self._client.my_id + '/match/id_' + self.id_yours+'/match_talk.txt','r')
        chat = fread.read()
        fread.close()
        #출력
        print(chat)
        self.chat_text_show.setText(chat)

        # 채팅서버와의 소켓연결
        self._client.client_chat_initiate(self.id_yours)
        #recv반복 스레드 시작
        self._client.start()


    def send_button_clicked(self):
        data = self.chat_text_edit.toPlainText()
        # QTextEdit의 마지막부분에 print(pickle.loads(data))해줘야함
        self.chat_text_show.append('me: '+data)
        f = open('./id_' + self._client.my_id + '/match/id_' + self.id_yours+'/match_talk.txt','a')
        f.write('me: '+data+'\n')
        f.close()
        self.chat_text_edit.clear()
        self._client.match_chat_send([data])


    def back_button_clicked(self):
        msg = 'chat_end'
        self._client.match_chat_send([msg, self.id_yours])
        self._client.chat_recv_thread_stop = 0
        self._client.chat_sock.close()
        self.close()

    # recv_msg_signal이 emit되면 self._client.chat_buffer 값을 처리함
    def process_recv_msg(self):
        data = pickle.loads(self._client.chat_buffer)
        #QTextEdit의 마지막부분에 print(pickle.loads(data))해줘야함
        data = self.id_yours+': '+ data[0]
        self.chat_text_show.append(data)
        f = open('./id_' + self._client.my_id + '/match/id_' + self.id_yours+'/match_talk.txt', 'a')
        f.write(data+'\n')
        f.close()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.chat_text_edit.setText(_translate("Dialog", "랜덤채팅, 매치채팅에 사용하는 ui는 틀은 똑같고 기능이 조금 다름"))
        self.send_button.setText(_translate("Dialog", "Send"))
        self.back_button.setText(_translate("Dialog", "Back"))
        self.chat_text_show.setText(_translate("Dialog", "채팅이 올라오는 부분"))
        self.chat_text_show.append('이것은 붙여진')