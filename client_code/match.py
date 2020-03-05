from PyQt5 import QtCore, QtGui, QtWidgets
import pickle
import os
import shutil
import chat
import profile


class my_match_ui(QtWidgets.QWidget, QtCore.QObject):
    start_main_signal = QtCore.pyqtSignal()

    def __init__(self, _client, parent=None):
        super(my_match_ui, self).__init__(parent)
        self._client = _client
        self.id_yours = ''
        self.match_list = []
        self.match_list_index = 0
        self.match_chat_uii = chat.match_chat_ui(self._client)
        self.intro = profile.intro_ui(self._client)
        self.setupUi()

    def setupUi(self):
        # disable (but not hide) close button
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)

        self.setObjectName("Form")
        self.resize(750, 520)

        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(40, 40, 671, 431))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")

        self.tabWidget = QtWidgets.QTabWidget(self.groupBox)
        self.tabWidget.setGeometry(QtCore.QRect(320, 20, 331, 321))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(0, 0, 331, 301))
        self.widget.setObjectName("widget")
        self.label_pic1 = QtWidgets.QLabel(self.widget)
        self.label_pic1.setGeometry(QtCore.QRect(0, 0, 331, 301))
        self.label_pic1.setObjectName("label_pic1")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.widget_2 = QtWidgets.QWidget(self.tab_2)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 331, 301))
        self.widget_2.setObjectName("widget_2")
        self.label_pic2 = QtWidgets.QLabel(self.widget_2)
        self.label_pic2.setGeometry(QtCore.QRect(0, 0, 331, 301))
        self.label_pic2.setObjectName("label_pic2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.widget_3 = QtWidgets.QWidget(self.tab_3)
        self.widget_3.setGeometry(QtCore.QRect(0, 0, 331, 301))
        self.widget_3.setObjectName("widget_3")
        self.label_pic3 = QtWidgets.QLabel(self.widget_3)
        self.label_pic3.setGeometry(QtCore.QRect(0, 0, 331, 301))
        self.label_pic3.setObjectName("label_pic3")
        self.tabWidget.addTab(self.tab_3, "")

        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 30, 271, 311))
        self.groupBox_2.setObjectName("groupBox_2")

        self.label_nickname = QtWidgets.QLabel(self.groupBox_2)
        self.label_nickname.setGeometry(QtCore.QRect(40, 50, 56, 12))
        self.label_nickname.setObjectName("label_nickname")
        self.label_residence = QtWidgets.QLabel(self.groupBox_2)
        self.label_residence.setGeometry(QtCore.QRect(40, 100, 71, 16))
        self.label_residence.setObjectName("label_residence")
        self.label_age = QtWidgets.QLabel(self.groupBox_2)
        self.label_age.setGeometry(QtCore.QRect(40, 200, 56, 12))
        self.label_age.setObjectName("label_age")
        self.label_hobby = QtWidgets.QLabel(self.groupBox_2)
        self.label_hobby.setGeometry(QtCore.QRect(40, 150, 61, 16))
        self.label_hobby.setObjectName("label_hobby")
        self.label_gender = QtWidgets.QLabel(self.groupBox_2)
        self.label_gender.setGeometry(QtCore.QRect(40, 250, 61, 16))
        self.label_gender.setObjectName("label_gender")
        self.label_nickname_text = QtWidgets.QLabel(self.groupBox_2)
        self.label_nickname_text.setGeometry(QtCore.QRect(150, 50, 56, 12))
        self.label_nickname_text.setObjectName("label")
        self.label_residence_text = QtWidgets.QLabel(self.groupBox_2)
        self.label_residence_text.setGeometry(QtCore.QRect(150, 100, 56, 12))
        self.label_residence_text.setObjectName("label_residence_text")
        self.label_hobby_text = QtWidgets.QLabel(self.groupBox_2)
        self.label_hobby_text.setGeometry(QtCore.QRect(150, 150, 56, 12))
        self.label_hobby_text.setObjectName("label_hobby_text")
        self.label_age_text = QtWidgets.QLabel(self.groupBox_2)
        self.label_age_text.setGeometry(QtCore.QRect(150, 200, 56, 12))
        self.label_age_text.setObjectName("label_age_text")
        self.label_gender_text = QtWidgets.QLabel(self.groupBox_2)
        self.label_gender_text.setGeometry(QtCore.QRect(150, 250, 56, 12))
        self.label_gender_text.setObjectName("label_age_text")

        self.intro_button = QtWidgets.QPushButton(self.groupBox)
        self.intro_button.setGeometry(QtCore.QRect(30, 370, 75, 41))
        self.intro_button.setObjectName("intro_button")
        self.chat_button = QtWidgets.QPushButton(self.groupBox)
        self.chat_button.setGeometry(QtCore.QRect(130, 370, 75, 41))
        self.chat_button.setObjectName("chat_button")
        self.cancel_match_button = QtWidgets.QPushButton(self.groupBox)
        self.cancel_match_button.setGeometry(QtCore.QRect(230, 370, 100, 41))
        self.cancel_match_button.setObjectName("cancel_match_button")
        self.back_button = QtWidgets.QPushButton(self.groupBox)
        self.back_button.setGeometry(QtCore.QRect(360, 370, 75, 41))
        self.back_button.setObjectName("back_button")
        self.previous_button = QtWidgets.QPushButton(self.groupBox)
        self.previous_button.setGeometry(QtCore.QRect(460, 370, 85, 41))
        self.previous_button.setObjectName("previous_button")
        self.next_button = QtWidgets.QPushButton(self.groupBox)
        self.next_button.setGeometry(QtCore.QRect(570, 370, 75, 41))
        self.next_button.setObjectName("next_button")

        self.retranslateUi()
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.back_button.clicked.connect(self.back_button_clicked)
        self.cancel_match_button.clicked.connect(self.cancel_match_button_clicked)
        self.chat_button.clicked.connect(self.chat_button_clicked)
        self.next_button.clicked.connect(self.next_button_clicked)
        self.previous_button.clicked.connect(self.previous_button_clicked)
        self.intro_button.clicked.connect(self.intro_button_clicked)

    def intro_button_clicked(self):
        self.intro.setWindowTitle(
            QtCore.QCoreApplication.translate("Dialog", self.label_nickname_text.text() + "님의 자기소개"))
        self.intro.editline_introduce.setTextInteractionFlags(
            QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.intro.exec_()

    def next_button_clicked(self):
        if self.match_list_index == len(self.match_list) - 1:
            print('마지막 페이지')
            QtWidgets.QMessageBox.about(self, 'last', '마지막 회원입니다')
        else:
            self.tabWidget.setCurrentIndex(0)
            self.match_list_index = self.match_list_index + 1
            self.setInfo()

    def previous_button_clicked(self):
        if self.match_list_index == 0:
            print('첫번째 페이지')
            QtWidgets.QMessageBox.about(self, 'first', '첫번째 회원입니다')
        else:
            self.tabWidget.setCurrentIndex(0)
            self.match_list_index = self.match_list_index - 1
            self.setInfo()

    def back_button_clicked(self):
        self._client.number_of_widgets = self._client.number_of_widgets - 1
        self.id_yours = ''
        self.start_main_signal.emit()
        self.close()

    # ['get_cancel',내id,보낸 match_list]
    def get_cancel_match(self):

        fread = open('./id_' + self._client.my_id + '/match/match_list.txt', 'rb')
        matchlist = pickle.loads(fread.read())
        fread.close()

        self._client.msg_list.append('get_cancel')
        self._client.msg_list.append(self._client.my_id)
        self._client.msg_list.append(matchlist)
        self._client.client_send()

        # ['get_cancel',True or False,매치취소된 목록(is_match=2였다가 -1이됨),내id,보낸 match_list]
        self._client.client_recv()
        print(self._client.msg_list_server)
        # print(f'매치취소된 목록{self._client.msg_list_server[2]}')

        if self._client.msg_list_server[1]:
            cancel_list = self._client.msg_list_server[2]
            fread = open('./id_' + self._client.my_id + '/match/match_list.txt', 'rb')
            data_list = pickle.loads(fread.read())
            fread.close()

            for item in cancel_list:
                data_list.remove(item)
                # 폴더 삭제 해줘야함
                print('삭제할 폴더경로 다음줄에 출력')
                print('./id_' + self._client.my_id + '/match/id_' + item)
                shutil.rmtree('./id_' + self._client.my_id + '/match/id_' + item)
            fwrite = open('./id_' + self._client.my_id + '/match/match_list.txt', 'wb')
            fwrite.write(pickle.dumps(data_list))
            fwrite.close()

    # 매치된사람(두 사람 DB에서 is_match=1일때 값을 2로 바꿔줌 )을 체크해주고
    # match_candidate_list.txt에서 삭제, match_list.txt에 상대 이름을 추가함
    def initiate_my_match(self):
        self.get_cancel_match()

        fread = open('./id_' + self._client.my_id + '/match/match_list.txt', 'rb')
        match_list = pickle.loads(fread.read())
        fread.close()
        # ['get_matched',내id,내 match_list]
        self._client.msg_list.append('get_matched')
        self._client.msg_list.append(self._client.my_id)
        self._client.msg_list.append(match_list)
        self._client.client_send()

        # ['get_matched',True or False,새로운 match_list(비어있을수있음),내id,보낸 match_list]
        self._client.client_recv()
        if self._client.msg_list_server[1]:
            match_list = self._client.msg_list_server[2]
            if match_list:
                for item in match_list:
                    fread = open('./id_' + self._client.my_id + '/match/match_candidate_list.txt', 'rb')
                    data_list = pickle.loads(fread.read())
                    fread.close()
                    data_list.remove(item)
                    fwrite = open('./id_' + self._client.my_id + '/match/match_candidate_list.txt', 'wb')
                    fwrite.write(pickle.dumps(data_list))
                    fwrite.close()

                    fread = open('./id_' + self._client.my_id + '/match/match_list.txt', 'rb')
                    data_list = pickle.loads(fread.read())
                    fread.close()
                    data_list.append(item)
                    fwrite = open('./id_' + self._client.my_id + '/match/match_list.txt', 'wb')
                    fwrite.write(pickle.dumps(data_list))
                    fwrite.close()

        fread = open('./id_' + self._client.my_id + '/match/match_candidate_list.txt', 'rb')
        match_candidate_list = pickle.loads(fread.read())
        fread.close()

        # 서버에서 나의 매치후보목록에 있는 사람도 나에게 like를 했을때 그 리스트를 받아와서 매치목록에 추가해줌
        # [['confirm_match_list', 내id, 내가 like한사람(is_match=1)의 list]
        if len(match_candidate_list):
            self._client.msg_list.append('confirm_match_list')
            self._client.msg_list.append(self._client.my_id)
            self._client.msg_list.append(match_candidate_list)
            self._client.client_send()
            # [ 'confirm_match_list',True or False, 매치 성공_list(is_match=2, false이면 빈 리스트), 내 id, 나의like_list ]
            self._client.client_recv()

            # 매치된 상대와 나의 candidate_list, match_list 모두 수정해줘야함
            if self._client.msg_list_server[1]:
                # 매치성공한 리스트를 candidate에서 제거
                match_success_list = self._client.msg_list_server[2]
                fread = open('./id_' + self._client.my_id + '/match/match_candidate_list.txt', 'rb')
                candidate_list = pickle.loads(fread.read())
                fread.close()
                for item in match_success_list:
                    candidate_list.remove(item)
                fwrite = open('./id_' + self._client.my_id + '/match/match_candidate_list.txt', 'wb')
                fwrite.write(pickle.dumps(candidate_list))
                # print(candidate_list)
                fwrite.close()
                # 매치성공한 리스트를 match_list에 추가
                fread = open('./id_' + self._client.my_id + '/match/match_list.txt', 'rb')
                match_list = pickle.loads(fread.read())
                fread.close()
                for item in match_success_list:
                    # print(item)
                    match_list.append(item)
                fwrite = open('./id_' + self._client.my_id + '/match/match_list.txt', 'wb')
                fwrite.write(pickle.dumps(match_list))
                # print(match_list)
                fwrite.close()
                # 이 부분은 my_id클라이언트에서 직접 만질수없는 부분 => my_match 눌렀을때 서버로 부터 정보를 받아야함
                '''
                for item in match_success_list:
                    fread = open(os.getcwd()+'/id_'+item+'/match/match_candidate_list.txt','rb')
                    data_list = pickle.loads(fread.read())
                    fread.close()
                    data_list.remove(self._client.my_id)
                    fwrite = open(os.getcwd()+'/id_'+item+'/match/match_candidate_list.txt','wb')
                    fwrite.write(pickle.dumps(data_list))
                    fwrite.close()

                    fread = open(os.getcwd() + '/id_' + item + '/match/match_list.txt', 'rb')
                    data_list = pickle.loads(fread.read())
                    fread.close()
                    data_list.append(self._client.my_id)
                    fwrite = open(os.getcwd() + '/id_' + item + '/match/match_list.txt', 'wb')
                    fwrite.write(pickle.dumps(data_list))
                    fwrite.close()
                '''
            else:
                pass

        fread = open('./id_' + self._client.my_id + '/match/match_list.txt', 'rb')
        match_list = pickle.loads(fread.read())
        fread.close()
        print(f'매치리스트: {match_list}')
        if len(match_list):
            self.update_info(match_list)

        if len(match_list):
            self.match_list_index = 0
            self.match_list = match_list
            self.tabWidget.setCurrentIndex(0)
            self.setInfo()
            self.show()
        else:
            print('매치된 사람이 없음')
            QtWidgets.QMessageBox.about(self, 'fail', '아직 매치된 회원이 없습니다')
            self.back_button_clicked()

    # 업데이트된 사진과 프로필 정보를 서버로 부터 받아서 업데이트
    def update_info(self, match_list):
        self._client.msg_list.append('get_updated_profile')
        self._client.msg_list.append(self._client.my_id)
        self._client.msg_list.append(match_list)

        # ['get_updated_profile', 내id, [내 매치 리스트]]
        self._client.client_send()

        # ['get_updated_profile', True or False, 내id, 보낸 매치리스트, [[ 매치회원id, [매치회원의 프로필]],~]
        # 이때 프로필은 [ 내id, 비밀번호, 거주지, 취미, 나이, 닉네임, 성별, 자기소개 ] 형태
        # profile = [ 닉네임, 거주지, 취미, 나이, 성별, 자기소개 ]
        self._client.client_recv()
        if self._client.msg_list_server[1]:
            profile_list = self._client.msg_list_server[4]
            for item in profile_list:
                profile = []
                profile.append(item[1][5])
                profile.append(item[1][2])
                profile.append(item[1][3])
                profile.append(item[1][4])
                profile.append(item[1][6])
                profile.append(item[1][7])
                f = open('./id_' + self._client.my_id + '/match/id_' + item[0] + '/profile.txt', 'wb')
                f.write(pickle.dumps(profile))
                f.close()

        self._client.msg_list.append('get_updated_pic')
        self._client.msg_list.append(self._client.my_id)
        self._client.msg_list.append(match_list)

        # ['get_updated_pic', 내id, [내 매치 리스트]]
        self._client.client_send()

        # ['get_updated_pic', True or False, 내id, 내가 보낸 내 매치리스트, [[ 매치회원id, [매치회원의 업데이트된 사진 번호]],~]
        self._client.client_recv()

        if self._client.msg_list_server[1]:
            for item in self._client.msg_list_server[4]:
                for index in item[1]:
                    # ['img_recv',내id,상대id,사진index]
                    self._client.msg_list.append('img_recv')
                    self._client.msg_list.append(self._client.my_id)
                    self._client.msg_list.append(item[0])
                    self._client.msg_list.append(index)
                    self._client.client_ftp_recv()

    def setInfo(self):
        # next를 누르면 index++, previous를 누르면 index--
        # self.match_list_index = 0
        id_to_show = self.match_list[self.match_list_index]
        self.id_yours = id_to_show

        fread = open('./id_' + self._client.my_id + '/match/id_' + id_to_show + '/profile.txt', 'rb')
        profile = pickle.loads(fread.read())
        fread.close()
        print(profile)
        self.label_nickname_text.setText(profile[0])
        self.label_residence_text.setText(profile[1])
        self.label_hobby_text.setText(profile[2])
        self.label_age_text.setText(profile[3])
        self.label_gender_text.setText(profile[4])
        self.intro.editline_introduce.setText(profile[5])

        self.label_pic1.setPixmap(QtGui.QPixmap('./id_' + self._client.my_id + '/match/id_' + id_to_show + '/me1.jpg'))
        self.label_pic2.setPixmap(QtGui.QPixmap('./id_' + self._client.my_id + '/match/id_' + id_to_show + '/me2.jpg'))
        self.label_pic3.setPixmap(QtGui.QPixmap('./id_' + self._client.my_id + '/match/id_' + id_to_show + '/me3.jpg'))

    def cancel_match_button_clicked(self):
        fread = open('./id_' + self._client.my_id + '/match/match_list.txt', 'rb')
        data_list = pickle.loads(fread.read())
        fread.close()
        data_list.remove(self.id_yours)
        fwrite = open('./id_' + self._client.my_id + '/match/match_list.txt', 'wb')
        fwrite.write(pickle.dumps(data_list))
        fwrite.close()

        shutil.rmtree('./id_' + self._client.my_id + '/match/id_' + self.id_yours)

        # ['match_cancel',내id,매치취소할id]
        self._client.msg_list.append('match_cancel')
        self._client.msg_list.append(self._client.my_id)
        self._client.msg_list.append(self.id_yours)
        self._client.client_send()
        # ['match_cancel',True or False, 내id,매치취소할id]
        self._client.client_recv()

        self.initiate_my_match()

    def chat_button_clicked(self):
        # 채팅서버와 새로운 소켓을 연결
        # 처음 연결이 되면 id_내id 테이블의 new_talk 값을 받아서 값이 1이면 서버에 저장된 대화 내용 (id_내id/match/id_상대id.txt) 을 로컬에 업데이트해야함
        # 다이얼로그 창이 뜨면 txt파일을 읽어서 화면에 출력해주면서 시작함
        # 채팅소켓으로부터 recv대기하는 스레드 생성필요
        # 서버로부터 recv한 값을 대화.txt에 업데이트 해주고 chat_text_show에 출력해줌
        # 대화를 전송할때 로컬파일에 내용을 저장한 후 서버로 전송
        self.match_chat_uii.id_yours = self.id_yours
        self.match_chat_uii.setWindowTitle(QtCore.QCoreApplication.translate("Dialog", self.label_nickname_text.text()+'님과의 대화'))
        self.match_chat_uii.initiate_chat()
        self.match_chat_uii.exec_()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.label_pic1.setText(_translate("Form", "1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "사진1"))
        self.label_pic2.setText(_translate("Form", "2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "사진2"))
        self.label_pic3.setText(_translate("Form", "3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "사진3"))
        self.groupBox_2.setTitle(_translate("Form", "상대 프로필"))
        self.label_nickname.setText(_translate("Form", "닉네임"))
        self.label_residence.setText(_translate("Form", "거주지"))
        self.label_age.setText(_translate("Form", "나이"))
        self.label_hobby.setText(_translate("Form", "취미"))
        self.label_gender.setText(_translate("Form", "성별"))
        self.label_nickname_text.setText(_translate("Form", "nickname"))
        self.label_residence_text.setText(_translate("Form", "residence"))
        self.label_hobby_text.setText(_translate("Form", "hobby"))
        self.label_age_text.setText(_translate("Form", "age"))
        self.label_gender_text.setText(_translate("Form", "gender"))
        self.chat_button.setText(_translate("Form", "채팅하기"))
        self.cancel_match_button.setText(_translate("Form", "매치 취소"))
        self.back_button.setText(_translate("Form", "메인화면"))
        self.next_button.setText(_translate("Form", "다음"))
        self.previous_button.setText(_translate("Form", "이전"))
        self.intro_button.setText(_translate("Form", "소개보기"))

class do_match_ui(QtWidgets.QWidget,QtCore.QObject):
    start_main_signal = QtCore.pyqtSignal()

    def __init__(self, _client, parent=None):
        super(do_match_ui, self).__init__(parent)
        self._client=_client
        self.id_yours=''
        self.intro = profile.intro_ui(self._client)
        self.setupUi()

    def setupUi(self):
        # disable (but not hide) close button
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)

        self.setObjectName("Form")
        self.resize(750, 520)

        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(40, 40, 671, 431))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")

        self.tabWidget = QtWidgets.QTabWidget(self.groupBox)
        self.tabWidget.setGeometry(QtCore.QRect(320, 20, 331, 321))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(0, 0, 331, 301))
        self.widget.setObjectName("widget")
        self.label_pic1 = QtWidgets.QLabel(self.widget)
        self.label_pic1.setGeometry(QtCore.QRect(0, 0, 331, 301))
        self.label_pic1.setObjectName("label_pic1")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.widget_2 = QtWidgets.QWidget(self.tab_2)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 331, 301))
        self.widget_2.setObjectName("widget_2")
        self.label_pic2 = QtWidgets.QLabel(self.widget_2)
        self.label_pic2.setGeometry(QtCore.QRect(0, 0, 331, 301))
        self.label_pic2.setObjectName("label_pic2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.widget_3 = QtWidgets.QWidget(self.tab_3)
        self.widget_3.setGeometry(QtCore.QRect(0, 0, 331, 301))
        self.widget_3.setObjectName("widget_3")
        self.label_pic3 = QtWidgets.QLabel(self.widget_3)
        self.label_pic3.setGeometry(QtCore.QRect(0, 0, 331, 301))
        self.label_pic3.setObjectName("label_pic3")
        self.tabWidget.addTab(self.tab_3, "")

        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 30, 271, 311))
        self.groupBox_2.setObjectName("groupBox_2")

        self.label_nickname = QtWidgets.QLabel(self.groupBox_2)
        self.label_nickname.setGeometry(QtCore.QRect(40, 50, 56, 12))
        self.label_nickname.setObjectName("label_nickname")
        self.label_residence = QtWidgets.QLabel(self.groupBox_2)
        self.label_residence.setGeometry(QtCore.QRect(40, 100, 71, 16))
        self.label_residence.setObjectName("label_residence")
        self.label_age = QtWidgets.QLabel(self.groupBox_2)
        self.label_age.setGeometry(QtCore.QRect(40, 200, 56, 12))
        self.label_age.setObjectName("label_age")
        self.label_hobby = QtWidgets.QLabel(self.groupBox_2)
        self.label_hobby.setGeometry(QtCore.QRect(40, 150, 61, 16))
        self.label_hobby.setObjectName("label_hobby")
        self.label_gender = QtWidgets.QLabel(self.groupBox_2)
        self.label_gender.setGeometry(QtCore.QRect(40, 250, 61, 16))
        self.label_gender.setObjectName("label_gender")
        self.label_nickname_text = QtWidgets.QLabel(self.groupBox_2)
        self.label_nickname_text.setGeometry(QtCore.QRect(150, 50, 56, 12))
        self.label_nickname_text.setObjectName("label")
        self.label_residence_text = QtWidgets.QLabel(self.groupBox_2)
        self.label_residence_text.setGeometry(QtCore.QRect(150, 100, 56, 12))
        self.label_residence_text.setObjectName("label_residence_text")
        self.label_hobby_text = QtWidgets.QLabel(self.groupBox_2)
        self.label_hobby_text.setGeometry(QtCore.QRect(150, 150, 56, 12))
        self.label_hobby_text.setObjectName("label_hobby_text")
        self.label_age_text = QtWidgets.QLabel(self.groupBox_2)
        self.label_age_text.setGeometry(QtCore.QRect(150, 200, 56, 12))
        self.label_age_text.setObjectName("label_age_text")
        self.label_gender_text = QtWidgets.QLabel(self.groupBox_2)
        self.label_gender_text.setGeometry(QtCore.QRect(150, 250, 56, 12))
        self.label_gender_text.setObjectName("label_age_text")
        self.like_button = QtWidgets.QPushButton(self.groupBox)
        self.like_button.setGeometry(QtCore.QRect(220, 370, 75, 41))
        self.like_button.setObjectName("like_button")
        self.pass_button = QtWidgets.QPushButton(self.groupBox)
        self.pass_button.setGeometry(QtCore.QRect(370, 370, 75, 41))
        self.pass_button.setObjectName("pass_button")
        self.back_button = QtWidgets.QPushButton(self.groupBox)
        self.back_button.setGeometry(QtCore.QRect(520, 370, 75, 41))
        self.back_button.setObjectName("back_button")
        self.intro_button = QtWidgets.QPushButton(self.groupBox)
        self.intro_button.setGeometry(QtCore.QRect(70, 370, 75, 41))
        self.intro_button.setObjectName("intro_button")

        self.retranslateUi()
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.back_button.clicked.connect(self.back_button_clicked)
        self.pass_button.clicked.connect(self.pass_button_clicked)
        self.like_button.clicked.connect(self.like_button_clicked)
        self.intro_button.clicked.connect(self.intro_button_clicked)

    def intro_button_clicked(self):
        self.intro.editline_introduce.setTextInteractionFlags(
            QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.intro.exec_()

    def initiate_match(self):
        self._client.msg_list.append('initiate_match')
        self._client.msg_list.append(self._client.my_id)

        self._client.client_send()
        # recv ['initiate_match',True,내id, [상대id,nickname,residence,hobby,age,gender,intro]]
        self._client.client_recv()
        can_match = self._client.msg_list_server[1]

        if can_match:
            print('match 정보 도달')
            f = open('./tmp/tmp_profile.txt', 'wb')
            f.write(pickle.dumps(self._client.msg_list_server[3]))
            f.close()

            self.label_nickname_text.setText(self._client.msg_list_server[3][1])
            self.label_residence_text.setText(self._client.msg_list_server[3][2])
            self.label_hobby_text.setText(self._client.msg_list_server[3][3])
            self.label_age_text.setText(self._client.msg_list_server[3][4])
            self.label_gender_text.setText(self._client.msg_list_server[3][5])
            self.intro.editline_introduce.setText(self._client.msg_list_server[3][6])

            self.id_yours = self._client.msg_list_server[3][0]
            # ['img_recv',내id,상대id,사진index]
            self._client.msg_list.append('img_recv')
            self._client.msg_list.append(self._client.my_id)
            self._client.msg_list.append(self.id_yours)
            self._client.msg_list.append(1)
            self._client.client_ftp_recv_tmp()

            self._client.msg_list.append('img_recv')
            self._client.msg_list.append(self._client.my_id)
            self._client.msg_list.append(self.id_yours)
            self._client.msg_list.append(2)
            self._client.client_ftp_recv_tmp()

            self._client.msg_list.append('img_recv')
            self._client.msg_list.append(self._client.my_id)
            self._client.msg_list.append(self.id_yours)
            self._client.msg_list.append(3)
            self._client.client_ftp_recv_tmp()

            self.label_pic1.setPixmap(QtGui.QPixmap('./tmp/tmp1.jpg'))
            self.label_pic2.setPixmap(QtGui.QPixmap('./tmp/tmp2.jpg'))
            self.label_pic3.setPixmap(QtGui.QPixmap('./tmp/tmp3.jpg'))
            self.tabWidget.setCurrentIndex(0)
            self.show()
        else:
            print('매치 가능한 사람이 없음')
            QtWidgets.QMessageBox.about(self, 'fail', '더 이상 매치할 회원이 없습니다\n잠시후 다시 시도해주세요')
            self.back_button_clicked()

    #['match_pass',내아이디,상대아이디]
    #내 아이디 DB에서 상대 아이디의 is_match값을 -1로 바꿔줌
    def pass_button_clicked(self):
        # ['match_pass', 내id, 상대id]
        self._client.msg_list.append('match_pass')
        self._client.msg_list.append(self._client.my_id)
        self._client.msg_list.append(self.id_yours)
        self.id_yours = ''
        self._client.client_send()
        self._client.client_recv()

        self.initiate_match()

    #['match_like,내아이디,상대아이디]
    #내 아이디 DB에서 상대 아이디의 is_match값을 1로 바꿔줌
    #client lcoal에서 id_내아이디/match에 id_상대아이디 폴더 만들고 프로필, 사진 저장
    def like_button_clicked(self):
        self._client.msg_list=[]
        #['match_like', 내id, 상대id]
        self._client.msg_list.append('match_like')
        self._client.msg_list.append(self._client.my_id)
        self._client.msg_list.append(self.id_yours)

        self._client.client_send()
        self._client.client_recv()

        fread = open('./id_'+self._client.my_id+'/match/match_candidate_list.txt','rb')
        match_list =pickle.loads(fread.read())
        match_list.append(self.id_yours)
        fread.close()
        fwrite = open('./id_'+self._client.my_id+'/match/match_candidate_list.txt','wb')
        fwrite.write(pickle.dumps(match_list))
        fwrite.close()

        try:
            if not (os.path.isdir('./id_' + self._client.my_id + '/match/id_'+self.id_yours)):
                os.makedirs(os.path.join('./id_' + self._client.my_id + '/match/id_'+self.id_yours))
        except OSError:
            print('failed to mkdir' + 'id_'+self.id_yours)
            return
        # profile = [ 닉네임, 거주지, 취미, 나이, 성별, 자기소개 ]
        profile = []
        profile.append(self.label_nickname_text.text())
        profile.append(self.label_residence_text.text())
        profile.append(self.label_hobby_text.text())
        profile.append(self.label_age_text.text())
        profile.append(self.label_gender_text.text())
        profile.append(self.intro.editline_introduce.toPlainText())

        f = open('./id_' + self._client.my_id + '/match/id_' + self.id_yours+'/profile.txt','wb')
        f.write(pickle.dumps(profile))
        f.close()

        fread = open('./tmp/tmp1.jpg','rb')
        fwrite = open('./id_' + self._client.my_id + '/match/id_' + self.id_yours + '/me1.jpg','wb')
        data=fread.read()
        fwrite.write(data)
        fread.close()
        fwrite.close()

        fread = open('./tmp/tmp2.jpg', 'rb')
        fwrite = open('./id_' + self._client.my_id + '/match/id_' + self.id_yours + '/me2.jpg', 'wb')
        data = fread.read()
        fwrite.write(data)
        fread.close()
        fwrite.close()

        fread = open('./tmp/tmp3.jpg', 'rb')
        fwrite = open('./id_' + self._client.my_id + '/match/id_' + self.id_yours + '/me3.jpg', 'wb')
        data = fread.read()
        fwrite.write(data)
        fread.close()
        fwrite.close()

        self.id_yours = ''
        #self._client.msg_list=[]
        self.initiate_match()


    def back_button_clicked(self):
        self._client.number_of_widgets = self._client.number_of_widgets - 1
        self.id_yours=''
        self.start_main_signal.emit()
        self.close()


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.intro.setWindowTitle(
            QtCore.QCoreApplication.translate("Dialog", self.label_nickname_text.text() + "님의 자기소개"))
        self.setWindowTitle(_translate("Form", "Form"))
        self.label_pic1.setText(_translate("Form", "1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "사진1"))
        self.label_pic2.setText(_translate("Form", "2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "사진2"))
        self.label_pic3.setText(_translate("Form", "3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "사진3"))
        self.groupBox_2.setTitle(_translate("Form", "상대 프로필"))
        self.label_nickname.setText(_translate("Form", "닉네임"))
        self.label_residence.setText(_translate("Form", "거주지"))
        self.label_age.setText(_translate("Form", "나이"))
        self.label_hobby.setText(_translate("Form", "취미"))
        self.label_gender.setText(_translate("Form", "성별"))
        self.label_nickname_text.setText(_translate("Form", "nickname"))
        self.label_residence_text.setText(_translate("Form", "residence"))
        self.label_hobby_text.setText(_translate("Form", "hobby"))
        self.label_age_text.setText(_translate("Form", "age"))
        self.label_gender_text.setText(_translate("Form", "gender"))
        self.intro_button.setText(_translate("Form", "소개보기"))
        self.like_button.setText(_translate("Form", "좋아요"))
        self.pass_button.setText(_translate("Form", "싫어요"))
        self.back_button.setText(_translate("Form", "메인화면"))