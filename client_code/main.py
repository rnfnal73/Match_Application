from PyQt5 import QtCore, QtWidgets


class main_ui(QtWidgets.QWidget):
    def __init__(self,_client,parent=None):
        super(main_ui,self).__init__(parent)
        self._client=_client
        self.number_of_users=0
        self.setupUi()

    def setupUi(self):
        # disable (but not hide) close button
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)

        self.setObjectName("Form")
        self.resize(750, 520)

        self.my_profile_button = QtWidgets.QPushButton(self)
        self.my_profile_button.setGeometry(QtCore.QRect(40, 460, 75, 41))
        self.my_profile_button.setObjectName("my_profile_button")
        self.do_match_button = QtWidgets.QPushButton(self)
        self.do_match_button.setGeometry(QtCore.QRect(150, 460, 75, 41))
        self.do_match_button.setObjectName("do_match_button")
        self.my_match_button = QtWidgets.QPushButton(self)
        self.my_match_button.setGeometry(QtCore.QRect(260, 460, 75, 41))
        self.my_match_button.setObjectName("my_match_button")
        self.anonymous_chat_button = QtWidgets.QPushButton(self)
        self.anonymous_chat_button.setGeometry(QtCore.QRect(370, 460, 101, 41))
        self.anonymous_chat_button.setObjectName("anonymous_chat_button")
        self.close_button = QtWidgets.QPushButton(self)
        self.close_button.setGeometry(QtCore.QRect(620, 460, 75, 41))
        self.close_button.setObjectName("close_button")

        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 481, 421))
        self.groupBox.setObjectName("groupBox")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox)
        self.tabWidget.setGeometry(QtCore.QRect(20, 30, 451, 370))
        self.tabWidget.setObjectName("tabWidget")

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.editline_notice1 = QtWidgets.QTextEdit(self.tab)
        self.editline_notice1.setGeometry(QtCore.QRect(20, 60, 401, 271))
        self.editline_notice1.setObjectName("editline_notice1")
        self.editline_title1 = QtWidgets.QTextEdit(self.tab)
        self.editline_title1.setGeometry(QtCore.QRect(20, 20, 401, 31))
        self.editline_title1.setObjectName("editline_title1")
        self.tabWidget.addTab(self.tab, "")
        self.editline_notice1.setTextInteractionFlags(
            QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.editline_title1.setTextInteractionFlags(
            QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.editline_notice2 = QtWidgets.QTextEdit(self.tab_2)
        self.editline_notice2.setGeometry(QtCore.QRect(20, 60, 401, 271))
        self.editline_notice2.setObjectName("editline_notice2")
        self.editline_title2 = QtWidgets.QTextEdit(self.tab_2)
        self.editline_title2.setGeometry(QtCore.QRect(20, 20, 401, 31))
        self.editline_title2.setObjectName("editline_title2")
        self.tabWidget.addTab(self.tab_2, "")
        self.editline_notice2.setTextInteractionFlags(
            QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.editline_title2.setTextInteractionFlags(
            QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)

        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.editline_title3 = QtWidgets.QTextEdit(self.tab_3)
        self.editline_title3.setGeometry(QtCore.QRect(20, 20, 401, 31))
        self.editline_title3.setObjectName("editline_title3")
        self.editline_notice3 = QtWidgets.QTextEdit(self.tab_3)
        self.editline_notice3.setGeometry(QtCore.QRect(20, 60, 401, 271))
        self.editline_notice3.setObjectName("editline_notice3")
        self.tabWidget.addTab(self.tab_3, "")
        self.editline_notice3.setTextInteractionFlags(
            QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.editline_title3.setTextInteractionFlags(
            QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)

        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.editline_title4 = QtWidgets.QTextEdit(self.tab_4)
        self.editline_title4.setGeometry(QtCore.QRect(20, 20, 401, 31))
        self.editline_title4.setObjectName("editline_title4")
        self.editline_notice4 = QtWidgets.QTextEdit(self.tab_4)
        self.editline_notice4.setGeometry(QtCore.QRect(20, 60, 401, 271))
        self.editline_notice4.setObjectName("editline_notice4")
        self.tabWidget.addTab(self.tab_4, "")
        self.editline_notice4.setTextInteractionFlags(
            QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.editline_title4.setTextInteractionFlags(
            QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)

        self.label_num_clients = QtWidgets.QLabel(self)
        self.label_num_clients.setGeometry(QtCore.QRect(520, 110, 101, 16))
        self.label_num_clients.setObjectName("label_num_clients")
        self.label_num_clients_2 = QtWidgets.QLabel(self)
        self.label_num_clients_2.setGeometry(QtCore.QRect(640, 110, 56, 12))
        self.label_num_clients_2.setObjectName("label_num_clients_2")

        self.groupBox_2 = QtWidgets.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(500, 160, 241, 251))
        self.groupBox_2.setObjectName("groupBox_2")
        self.editline_vote = QtWidgets.QTextEdit(self.groupBox_2)
        self.editline_vote.setGeometry(QtCore.QRect(10, 30, 221, 81))
        self.editline_vote.setObjectName("editline_vote")

        self.radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton.setGeometry(QtCore.QRect(30, 130, 90, 16))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_2.setGeometry(QtCore.QRect(130, 130, 90, 16))
        self.radioButton_2.setObjectName("radioButton")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_3.setGeometry(QtCore.QRect(30, 170, 90, 16))
        self.radioButton_3.setObjectName("radioButton")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_4.setGeometry(QtCore.QRect(130, 170, 90, 16))
        self.radioButton_4.setObjectName("radioButton_2")
        self.submit_Button = QtWidgets.QPushButton(self.groupBox_2)
        self.submit_Button.setGeometry(QtCore.QRect(80, 210, 75, 23))
        self.submit_Button.setObjectName("submit_Button")


        self.retranslateUi()
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.close_button.clicked.connect(self.close_button_clicked)
        self.submit_Button.clicked.connect(self.submit_button_clicked)

    def close_button_clicked(self):
        self._client.number_of_widgets = self._client.number_of_widgets - 1
        if self._client.number_of_widgets == 0:
            self._client.msg_list.append('close_thread')
            self._client.msg_list.append(self._client.my_id)
            self._client.client_send()
        print(self._client.number_of_widgets)
        self.close()

    def submit_button_clicked(self):
        self._client.msg_list.append('vote_apply')
        self._client.msg_list.append(self._client.my_id)
        if self.radioButton.isChecked():
            self._client.msg_list.append(1)
        elif self.radioButton_2.isChecked():
            self._client.msg_list.append(2)
        elif self.radioButton_3.isChecked():
            self._client.msg_list.append(3)
        elif self.radioButton_4.isChecked():
            self._client.msg_list.append(4)
        else:
            QtWidgets.QMessageBox.about(self, 'vote fail', '투표할 대상을 선택하세요')
            self._client.msg_list=[]
            return
        self._client.client_send()
        self._client.client_recv()

        if self._client.msg_list_server[1]:
            QtWidgets.QMessageBox.about(self, 'fail', '투표에 성공했습니다')
        else:
            QtWidgets.QMessageBox.about(self, 'fail', '다시 시도해주세요')

    def count_users(self):
        self._client.msg_list.append('count_users')
        self._client.client_send()
        self._client.client_recv()
        self.number_of_users = self._client.msg_list_server[1]
        self.label_num_clients_2.setText(str(self.number_of_users)+'명')

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.my_profile_button.setText(_translate("Form", "내 프로필"))
        self.do_match_button.setText(_translate("Form", "매치하기"))
        self.my_match_button.setText(_translate("Form", "매치목록"))
        self.anonymous_chat_button.setText(_translate("Form", "익명 채팅"))
        self.close_button.setText(_translate("Form", "종료"))

        self.groupBox.setTitle(_translate("Form", "공지사항"))

        self.editline_title1.setText(_translate("Form", "2020년 공휴일"))
        self.editline_notice1.setText(_translate("Form", "1월 1일	수요일	새해\n1월 24일 ~ 1월 26일	금요일 ~ 일요일	설날\n3월 1일	일요일	3·1 운동/삼일절\n4월 30일	목요일	부처님 오신 날\n5월 5일	화요일	어린이날\n6월 6일	토요일	현충일\n8월 15일	토요일	광복절\n9월 30일 ~ 10월 2일	수요일 ~ 금요일	추석\n10월 3일	토요일	개천절\n10월 9일	금요일	한글날\n12월 25일	금요일	크리스마스"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "알림 1"))

        self.editline_title2.setText(_translate("Form", "맛있는 과일 고르는 방법"))
        self.editline_notice2.setText(_translate("Form", "꼭지 부분의 색이 골고루 잘 들어있고 밝은 느낌이 나는 것이 맛있는 과일이며, 향기가 강하지 않고 은은한 것이 신선하다.\n과일을 들었을 때 묵직한 느낌이 들고 단단한 것이 좋으며,\n과일 전체에 색이 고르게 착색되고 꼭지가 붙어 있는 것을 고른다."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "알림 2"))

        self.editline_title3.setText(_translate("Form", "아이유 - 이름에게"))
        self.editline_notice3.setText(_translate("Form", "꿈에서도 그리운 목소리는\n이름 불러도 대답을 하지 않아\n글썽이는 그 메아리만 돌아와\n그 소리를 나 혼자서 들어\n깨어질 듯이 차가워도\n이번에는 결코 놓지 않을게\n아득히 멀어진 그날의 두 손을\n끝없이 길었던\n짙고 어두운 밤 사이로\n조용히 사라진\n네 소원을 알아\n오래 기다릴게\n반드시 너를 찾을게\n보이지 않도록 멀어도\n가자 이 새벽이 끝나는 곳으로\n어김없이 내 앞에 선 그 아이는\n고개 숙여도 기어이 울지 않아\n안쓰러워 손을 뻗으면 달아나\n텅 빈 허공을 나 혼자 껴안아\n에어질듯이 아파와도\n이번에는 결코 잊지 않을게\n한참을 외로이 기다린 그 말을\n끝없이 길었던\n짙고 어두운 밤 사이로\n영원히 사라진 네 소원을 알아\n오래 기다릴게\n반드시 너를 찾을게\n보이지 않도록 멀어도\n가자 이 새벽이 끝나는 곳\n수없이 잃었던\n춥고 모진 날 사이로\n조용히 잊혀진\n네 이름을 알아\n멈추지 않을게\n몇 번 이라도 외칠게\n믿을 수 없도록 멀어도\n가자 이 새벽이 끝나는 곳으로"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "알림 3"))

        self.editline_title4.setText(_translate("Form", "2019_2학기 시간표"))
        self.editline_notice4.setText(_translate("Form", "네트워크 프로그래밍\n선형대수학\n데이터베이스\n신기술세미나\n현대사회와패션\n상허스콜라리움\n음악의이해"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "알림 4"))

        self.label_num_clients.setText(_translate("Form", "현재 접속자 수 :"))
        self.label_num_clients_2.setText(_translate("Form", "xxx 명"))
        self.groupBox_2.setTitle(_translate("Form", "투표"))
        self.submit_Button.setText(_translate("Form", "제출하기"))
        self.editline_vote.setText(_translate("Form", "다음 중 가장 좋아하는 노래를 골라 투표하세요~"))
        self.radioButton.setText(_translate("Form", "빨간맛"))
        self.radioButton_2.setText(_translate("Form", "시간을달려서"))
        self.radioButton_3.setText(_translate("Form", "다시만난세계"))
        self.radioButton_4.setText(_translate("Form", "우아하게"))

