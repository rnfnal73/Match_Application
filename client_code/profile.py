from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog
import os
from PyQt5 import QtWidgets
import pickle
import copy



class my_profile_ui(QtWidgets.QWidget, QtCore.QObject):
    start_main_signal = QtCore.pyqtSignal()

    def __init__(self,_client,parent=None):
        super(my_profile_ui, self).__init__(parent)
        self._client=_client
        self.intro = intro_ui(self._client)
        self.setupUi()

    def setupUi(self):
        # disable (but not hide) close button
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)

        self.setObjectName("Form")
        self.resize(750, 520)

        self.box = QtWidgets.QHBoxLayout()

        self.groupBox_2 = QtWidgets.QGroupBox()
        self.groupBox_2.setGeometry(QtCore.QRect(20, 30, 331, 421))
        self.groupBox_2.setObjectName("groupBox_2")

        self.label_nickname = QtWidgets.QLabel(self.groupBox_2)
        self.label_nickname.setGeometry(QtCore.QRect(50, 80, 56, 12))
        self.label_nickname.setObjectName("label_nickname")
        self.editline_nickname = QtWidgets.QLineEdit(self.groupBox_2)
        self.editline_nickname.setGeometry(QtCore.QRect(160, 80, 113, 20))
        self.editline_nickname.setObjectName("editline_nickname")
        self.label_password = QtWidgets.QLabel(self.groupBox_2)
        self.label_password.setGeometry(QtCore.QRect(50, 140, 56, 12))
        self.label_password.setObjectName("label_password")
        self.label_hobby = QtWidgets.QLabel(self.groupBox_2)
        self.label_hobby.setGeometry(QtCore.QRect(50, 260, 56, 12))
        self.label_hobby.setObjectName("label_hobby")
        self.label_residence = QtWidgets.QLabel(self.groupBox_2)
        self.label_residence.setGeometry(QtCore.QRect(50, 200, 61, 12))
        self.label_residence.setObjectName("label_residence")
        self.label_age = QtWidgets.QLabel(self.groupBox_2)
        self.label_age.setGeometry(QtCore.QRect(50, 320, 56, 12))
        self.label_age.setObjectName("label_age")

        self.editline_age = QtWidgets.QLineEdit(self.groupBox_2)
        self.editline_age.setGeometry(QtCore.QRect(160, 320, 113, 20))
        self.editline_age.setObjectName("editline_age")
        self.editline_residence = QtWidgets.QLineEdit(self.groupBox_2)
        self.editline_residence.setGeometry(QtCore.QRect(160, 200, 113, 20))
        self.editline_residence.setObjectName("editline_residence")
        self.editline_hobby = QtWidgets.QLineEdit(self.groupBox_2)
        self.editline_hobby.setGeometry(QtCore.QRect(160, 260, 113, 20))
        self.editline_hobby.setObjectName("editline_hobby")
        self.editline_password = QtWidgets.QLineEdit(self.groupBox_2)
        self.editline_password.setGeometry(QtCore.QRect(160, 140, 113, 20))
        self.editline_password.setObjectName("editline_password")

        self.intro_button = QtWidgets.QPushButton(self.groupBox_2)
        self.intro_button.setGeometry(QtCore.QRect(40, 400, 81, 31))
        self.intro_button.setObjectName("intro_button")
        self.revise_button = QtWidgets.QPushButton(self.groupBox_2)
        self.revise_button.setGeometry(QtCore.QRect(140, 400, 81, 31))
        self.revise_button.setObjectName("revise_button")
        self.back_button = QtWidgets.QPushButton(self.groupBox_2)
        self.back_button.setGeometry(QtCore.QRect(240, 400, 81, 31))
        self.back_button.setObjectName("back_button")

        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(360, 30, 371, 421))
        self.groupBox.setObjectName("groupBox")
        self.erase_pic_button = QtWidgets.QPushButton(self.groupBox)
        self.erase_pic_button.setGeometry(QtCore.QRect(250, 390, 75, 23))
        self.erase_pic_button.setObjectName("erase_pic_button")
        self.find_button = QtWidgets.QPushButton(self.groupBox)
        self.find_button.setGeometry(QtCore.QRect(150, 390, 75, 21))
        self.find_button.setObjectName("find_button")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 331, 321))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(0, 0, 331, 301))
        self.widget.setObjectName("widget")
        self.pic_1 = QtWidgets.QLabel(self.widget)
        self.pic_1.setGeometry(QtCore.QRect(0, 0, 331, 301))
        self.pic_1.setObjectName("pic_1")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.widget_2 = QtWidgets.QWidget(self.tab_2)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 331, 301))
        self.widget_2.setObjectName("widget_2")
        self.pic_2 = QtWidgets.QLabel(self.widget_2)
        self.pic_2.setGeometry(QtCore.QRect(0, 0, 331, 301))
        self.pic_2.setObjectName("pic_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.widget_3 = QtWidgets.QWidget(self.tab_3)
        self.widget_3.setGeometry(QtCore.QRect(0, 0, 331, 301))
        self.widget_3.setObjectName("widget_3")
        self.pic_3 = QtWidgets.QLabel(self.widget_3)
        self.pic_3.setGeometry(QtCore.QRect(0, 0, 331, 301))
        self.pic_3.setObjectName("pic_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.revise_pic_button = QtWidgets.QPushButton(self.groupBox)
        self.revise_pic_button.setGeometry(QtCore.QRect(50, 390, 71, 21))
        self.revise_pic_button.setObjectName("revise_pic_button")

        self.editline_filepath = QtWidgets.QTextEdit(self.groupBox)
        self.editline_filepath.setGeometry(QtCore.QRect(20, 350, 331, 20))
        self.editline_filepath.setObjectName("editline_filepath")
        self.editline_filepath.setTextInteractionFlags(
            QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)

        self.box.addWidget(self.groupBox_2)
        self.box.addWidget(self.groupBox)

        self.retranslateUi()
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.setLayout(self.box)

        self.intro_button.clicked.connect(self.intro_button_clicked)
        self.back_button.clicked.connect(self.back_button_clicked)
        self.find_button.clicked.connect(self.find_button_clicked)
        self.revise_pic_button.clicked.connect(self.revise_pic_button_clicked)
        self.erase_pic_button.clicked.connect(self.erase_pic_button_clicked)
        self.revise_button.clicked.connect(self.revise_button_clicked)

    def intro_button_clicked(self):
        self.intro.exec_()

    def revise_button_clicked(self):
        fread = open('./id_' + self._client.my_id + '/my_profile.txt', 'rb')
        list_read = pickle.loads(fread.read())
        fread.close()
        print(list_read)

        fread = open('./id_' + self._client.my_id + '/match/match_list.txt', 'rb')
        data = pickle.loads(fread.read())
        fread.close()
        if len(self.editline_nickname.text()) > 10 :
            self.editline_nickname.setText(self.editline_nickname.text()[0:10])
        if len(self.editline_password.text()) > 10 :
            self.editline_password.setText(self.editline_password.text()[0:10])
        if len(self.editline_hobby.text()) > 10 :
            self.editline_hobby.setText(self.editline_hobby.text()[0:10])
        if len(self.editline_age.text()) > 10 :
            self.editline_age.setText(self.editline_age.text()[0:10])
        if len(self.editline_residence.text()) > 10 :
            self.editline_residence.setText(self.editline_residence.text()[0:10])
        if len(self.intro.editline_introduce.toPlainText()) > 200 :
            self.intro.editline_introduce.setText(self.intro.editline_introduce.toPlainText()[0:200])

        #[ 내id, 비밀번호, 거주지, 취미, 나이, 닉네임, 성별, 자기소개 ]
        tmp_list = []
        tmp_list.append(self._client.my_id)
        tmp_list.append(self.editline_password.text())
        tmp_list.append(self.editline_residence.text())
        tmp_list.append(self.editline_hobby.text())
        tmp_list.append(self.editline_age.text())
        tmp_list.append(self.editline_nickname.text())
        tmp_list.append(list_read[6])
        tmp_list.append(self.intro.editline_introduce.toPlainText())

        if tmp_list == list_read:
            QtWidgets.QMessageBox.about(self, 'revise failed', '변경사항이 없습니다')
            return
        else:
            fwrite = open('./id_' + self._client.my_id + '/my_profile.txt','wb')
            fwrite.write(pickle.dumps(tmp_list))
            fwrite.close()
            fread.close()
            QtWidgets.QMessageBox.about(self, 'revise success', '변경사항이 저장됐습니다')

        # ['new_profile', profile_list, 매치리스트]
        self._client.msg_list.append('new_profile')
        self._client.msg_list.append(tmp_list)
        self._client.msg_list.append(data)
        self._client.client_send()
        self._client.client_recv()

    def erase_pic_button_clicked(self):
        self._client.img_resize('./tmp/base_image.jpg')
        fread = open('./tmp/resized.jpg','rb')
        data_base = fread.read()
        fwrite = open('./id_' + self._client.my_id+'/me'+str(self.tabWidget.currentIndex()+1) + '.jpg','wb')
        fwrite.write(data_base)
        fread.close()
        fwrite.close()

        self._client.msg_list.append('img_send')
        self._client.msg_list.append(self._client.my_id)
        self._client.msg_list.append(len(data_base))
        self._client.msg_list.append(self.tabWidget.currentIndex() + 1)
        print('삭제된 이미지 보내기(서버에 베이스 이미지로 교체)')
        print(self._client.msg_list)
        self._client.client_ftp_send('./tmp/resized.jpg')
        # self._client.img_send('resized.jpg')
        # self._client.client_recv()

        fread = open('./id_' + self._client.my_id + '/match/match_list.txt', 'rb')
        data = pickle.loads(fread.read())
        fread.close()

        self._client.msg_list.append('update_pic')
        self._client.msg_list.append(self._client.my_id)
        self._client.msg_list.append(data)
        self._client.msg_list.append(self.tabWidget.currentIndex() + 1)
        # ['update_pic', 내 id, 내 매치 리스트, 업데이트한 사진 인덱스]
        self._client.client_send()
        # ['update_pic', True or False, 내 id, 내 매치 리스트, 업데이트한 사진 인덱스]
        self._client.client_recv()

        self.pic_1.setPixmap(QtGui.QPixmap('./id_' + self._client.my_id + '/me1.jpg'))
        self.pic_2.setPixmap(QtGui.QPixmap('./id_' + self._client.my_id + '/me2.jpg'))
        self.pic_3.setPixmap(QtGui.QPixmap('./id_' + self._client.my_id + '/me3.jpg'))
        QtWidgets.QMessageBox.about(self, 'delete success', '사진을 삭제했습니다')

    def revise_pic_button_clicked(self):
        #print(self._client.my_id)
        if not self.editline_filepath.toPlainText():
            QtWidgets.QMessageBox.about(self, 'revise failed', '사진을 선택해주세요')
            return
        else:
            self._client.img_resize(self.editline_filepath.toPlainText())
            fread = open('./tmp/resized.jpg','rb')

            fwrite = open('./id_' + self._client.my_id+'/me'+str(self.tabWidget.currentIndex()+1) + '.jpg','wb')
            file_data = fread.read()
            file_size = len(file_data)
            fwrite.write(file_data)
            fread.close()
            fwrite.close()
            self._client.msg_list.append('img_send')
            self._client.msg_list.append(self._client.my_id)
            self._client.msg_list.append(file_size)
            self._client.msg_list.append(self.tabWidget.currentIndex()+1)
            print('이미지 보내기')
            print(self._client.msg_list)
            self._client.client_ftp_send('./tmp/resized.jpg')
            #self._client.img_send('resized.jpg')
            #self._client.client_recv()

            fread = open('./id_'+self._client.my_id+'/match/match_list.txt','rb')
            data = pickle.loads(fread.read())
            fread.close()

            self._client.msg_list.append('update_pic')
            self._client.msg_list.append(self._client.my_id)
            self._client.msg_list.append(data)
            self._client.msg_list.append(self.tabWidget.currentIndex()+1)
            #['update_pic', 내 id, 내 매치 리스트, 업데이트한 사진 인덱스]
            self._client.client_send()
            # ['update_pic', True or False, 내 id, 내 매치 리스트, 업데이트한 사진 인덱스]
            self._client.client_recv()

            self.pic_1.setPixmap(QtGui.QPixmap('./id_'+self._client.my_id+'/me1.jpg'))
            #self.pic_1.setPixmap(QtGui.QPixmap(resource_path('./id_3/me1.jpg')))
            self.pic_2.setPixmap(QtGui.QPixmap('./id_'+self._client.my_id+'/me2.jpg'))
            self.pic_3.setPixmap(QtGui.QPixmap('./id_'+self._client.my_id+'/me3.jpg'))
            QtWidgets.QMessageBox.about(self, 'revise success', '사진이 수정됐습니다')

    def initiate_profile(self):
        self.pic_1.setPixmap(QtGui.QPixmap('./id_'+self._client.my_id+'/me1.jpg'))
        self.pic_2.setPixmap(QtGui.QPixmap('./id_'+self._client.my_id+'/me2.jpg'))
        self.pic_3.setPixmap(QtGui.QPixmap('./id_'+self._client.my_id+'/me3.jpg'))
        print('./id_' + self._client.my_id + '/my_profile.txt')
        f = open('./id_' + self._client.my_id + '/my_profile.txt' , 'rb')
        profile = pickle.loads(f.read())
        f.close()
        self.editline_nickname.setText(profile[5])
        self.editline_password.setText(profile[1])
        self.editline_residence.setText(profile[2])
        self.editline_hobby.setText(profile[3])
        self.editline_age.setText(profile[4])
        self.intro.editline_introduce.setText(profile[7])
        self.tabWidget.setCurrentIndex(0)

    def back_button_clicked(self):
        self._client.number_of_widgets = self._client.number_of_widgets - 1
        self.start_main_signal.emit()
        self.close()

    def find_button_clicked(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Open file', './')
            self.editline_filepath.setText(fname[0])
            if os.path.getsize(fname[0]) == 0:
                QtWidgets.QMessageBox.about(self, 'fail', '다른 파일을 선택해주세요')
                return
            fname2, ext = os.path.splitext(fname[0])
            print(fname2)
            print(ext)
            if ext != '.jpg' and ext != '.png' and ext != '.jpeg' and ext != '.bmp':
                QtWidgets.QMessageBox.about(self, 'fail', '이미지 파일을 선택해주세요')
                self.editline_filepath.setText('')
                return
        except Exception as e:
            print(e)
            return

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.intro_button.setText(_translate("Form", "자기소개"))
        self.back_button.setText(_translate("Form", "돌아가기"))
        self.groupBox.setTitle(_translate("Form", "내 프로필 사진"))
        self.erase_pic_button.setText(_translate("Form", "사진삭제"))
        self.find_button.setText(_translate("Form", "사진찾기"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "사진1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "사진2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "사진3"))
        self.revise_pic_button.setText(_translate("Form", "사진수정"))
        self.groupBox_2.setTitle(_translate("Form", "내 프로필"))

        self.label_age.setText(_translate("Form", "나이"))
        self.label_nickname.setText(_translate("Form", "닉네임"))
        #self.editline_nickname.setText(_translate("Form", "my_nickname"))
        self.label_password.setText(_translate("Form", "비밀번호"))
        self.label_hobby.setText(_translate("Form", "취미"))
        self.label_residence.setText(_translate("Form", "거주지"))
        #self.editline_residence.setText(_translate("Form", "my_residence"))
        #self.editline_hobby.setText(_translate("Form", "my_hobby"))
        #self.editline_password.setText(_translate("Form", "empty"))
        self.revise_button.setText(_translate("Form", "수정"))


class intro_ui(QtWidgets.QDialog):
    def __init__(self, _client, parent=None):
        super(intro_ui, self).__init__(parent)
        self._client=_client
        self.setupUi()

    def setupUi(self):
        # disable (but not hide) close button
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)

        self.setObjectName("Dialog")
        self.resize(341, 386)
        self.confirm_button = QtWidgets.QPushButton(self)
        self.confirm_button.setGeometry(QtCore.QRect(120, 350, 101, 31))
        self.confirm_button.setObjectName("confirm_button")
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 321, 331))
        self.groupBox.setObjectName("groupBox")
        self.editline_introduce = QtWidgets.QTextEdit(self.groupBox)
        self.editline_introduce.setGeometry(QtCore.QRect(20, 20, 281, 301))

        #내 프로필, 회원가입 부분에서는 활성화, 로그인 이후의 매치화면에서는 비활성화 해야함
        #self.editline_introduce.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.editline_introduce.setObjectName("editline_introduce")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.confirm_button.clicked.connect(self.confirm_button_clicked)

    def confirm_button_clicked(self):
        self.close()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "자기소개 입력"))
        self.confirm_button.setText(_translate("Dialog", "확인"))
        self.groupBox.setTitle(_translate("Dialog", "자기소개"))
        #self.textEdit_2.setText(_translate("Dialog", ""))


class join_ui(QtWidgets.QWidget,QtCore.QObject):
    start_login_signal = QtCore.pyqtSignal()

    def __init__(self, _client, parent=None):
        super(join_ui, self).__init__(parent)
        QtCore.QObject.__init__(self)
        self._client = _client
        self.intro = intro_ui(self._client)
        self.setupUi()

    def setupUi(self):
        # disable (but not hide) close button
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)

        self.setObjectName("Form")
        self.resize(750, 520)

        self.join_interface = QtWidgets.QHBoxLayout()
        gb = QtWidgets.QGroupBox('회원가입')
        self.join_interface.addWidget(gb)
        self.join_box = QtWidgets.QVBoxLayout()
        gb1=QtWidgets.QGroupBox('정보')
        self.join_info_box = QtWidgets.QHBoxLayout()
        self.join_text = QtWidgets.QHBoxLayout()
        self.join_text_label = QtWidgets.QVBoxLayout()
        self.join_text_edit = QtWidgets.QVBoxLayout()
        self.join_pic = QtWidgets.QVBoxLayout()
        self.join_buttons = QtWidgets.QHBoxLayout()
        self.join_radio = QtWidgets.QHBoxLayout()

        self.male_radio = QtWidgets.QRadioButton('남성',self)
        self.male_radio.setChecked(True)
        self.female_radio = QtWidgets.QRadioButton('여성', self)

        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(190, 310, 56, 12))
        self.label_5.setObjectName("label_5")
        self.label_5.setFixedSize(100,20)
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(190, 370, 56, 12))
        self.label_6.setObjectName("label_6")
        self.label_6.setFixedSize(100, 20)
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(190, 190, 56, 12))
        self.label_2.setObjectName("label_2")
        self.label_2.setFixedSize(100, 20)
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(190, 250, 61, 16))
        self.label_4.setObjectName("label_4")
        self.label_4.setFixedSize(100, 20)
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(530, 200, 150, 16))
        self.label_7.setObjectName("label_7")
        self.label_7.setFixedSize(200, 20)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(190, 130, 56, 12))
        self.label.setObjectName("label")
        self.label.setFixedSize(100, 20)
        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(190, 430, 61, 16))
        self.label_8.setObjectName("label_8")
        self.label_8.setFixedSize(100, 20)

        self.join_button = QtWidgets.QPushButton(self)
        self.join_button.setGeometry(QtCore.QRect(230, 440, 81, 31))
        self.join_button.setObjectName("join_button")

        self.close_button = QtWidgets.QPushButton(self)
        self.close_button.setGeometry(QtCore.QRect(390, 440, 81, 31))
        self.close_button.setObjectName("close_button")

        self.find_button = QtWidgets.QPushButton(self)
        self.find_button.setGeometry(QtCore.QRect(540, 300, 81, 31))
        self.find_button.setObjectName("find_button")

        self.intro_button = QtWidgets.QPushButton(self)
        self.intro_button.setGeometry(QtCore.QRect(70, 440, 81, 31))
        self.intro_button.setObjectName("intro_button")

        self.editline_id = QtWidgets.QLineEdit(self)
        self.editline_id.setGeometry(QtCore.QRect(300, 130, 113, 20))
        self.editline_id.setObjectName("editline_id")
        self.editline_id.setFixedSize(200,30)

        self.editline_password = QtWidgets.QLineEdit(self)
        self.editline_password.setGeometry(QtCore.QRect(300, 190, 113, 20))
        self.editline_password.setObjectName("editline_password")
        self.editline_password.setFixedSize(200,30)

        self.editline_residence = QtWidgets.QLineEdit(self)
        self.editline_residence.setGeometry(QtCore.QRect(300, 250, 113, 20))
        self.editline_residence.setObjectName("editline_residence")
        self.editline_residence.setFixedSize(200,30)

        self.editline_hobby = QtWidgets.QLineEdit(self)
        self.editline_hobby.setGeometry(QtCore.QRect(300, 310, 113, 20))
        self.editline_hobby.setObjectName("editline_hobby")
        self.editline_hobby.setFixedSize(200,30)

        self.editline_age = QtWidgets.QLineEdit(self)
        self.editline_age.setGeometry(QtCore.QRect(300, 370, 113, 20))
        self.editline_age.setObjectName("editline_age")
        self.editline_age.setFixedSize(200,30)

        self.editline_nickname = QtWidgets.QLineEdit(self)
        self.editline_nickname.setGeometry(QtCore.QRect(300, 430, 113, 20))
        self.editline_nickname.setObjectName("editline_nickname")
        self.editline_nickname.setFixedSize(200, 30)


        self.editline_filepath = QtWidgets.QTextEdit(self)
        self.editline_filepath.setGeometry(QtCore.QRect(500, 250, 160, 20))
        self.editline_filepath.setObjectName("editline_filepath")
        self.editline_filepath.setFixedSize(200,30)
        self.editline_filepath.setTextInteractionFlags(
            QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.join_button.clicked.connect(self.join_button_clicked)
        self.close_button.clicked.connect(self.close_button_clicked)
        self.find_button.clicked.connect(self.find_button_clicked)
        self.intro_button.clicked.connect(self.intro_button_clicked)

        self.join_text_label.addWidget(self.label)
        self.join_text_label.addWidget(self.label_2)
        self.join_text_label.addWidget(self.label_4)
        self.join_text_label.addWidget(self.label_5)
        self.join_text_label.addWidget(self.label_6)
        self.join_text_label.addWidget(self.label_8)

        self.join_text_edit.addWidget(self.editline_id)
        self.join_text_edit.addWidget(self.editline_password)
        self.join_text_edit.addWidget(self.editline_residence)
        self.join_text_edit.addWidget(self.editline_hobby)
        self.join_text_edit.addWidget(self.editline_age)
        self.join_text_edit.addWidget(self.editline_nickname)

        self.join_radio.addWidget(self.male_radio)
        self.join_radio.addWidget(self.female_radio)

        self.join_pic.addLayout(self.join_radio)
        self.join_pic.addWidget(self.label_7)
        self.join_pic.addWidget(self.editline_filepath)
        self.join_pic.addWidget(self.find_button)

        self.join_text.addLayout(self.join_text_label)
        self.join_text.addLayout(self.join_text_edit)
        gb1.setLayout(self.join_text)
        #gb2.setLayout(self.join_pic)

        self.join_info_box.addWidget(gb1)
        #self.join_info_box.addWidget(gb2)
        self.join_info_box.addLayout(self.join_pic)

        self.join_buttons.addWidget(self.intro_button)
        self.join_buttons.addWidget(self.join_button)
        self.join_buttons.addWidget(self.close_button)

        self.join_box.addLayout(self.join_info_box)
        self.join_box.addLayout(self.join_buttons)

        gb.setLayout(self.join_box)
        self.setLayout(self.join_interface)

    def intro_button_clicked(self):
        self.intro.exec_()

    # 파일 경로를 찾으면 copy를 생성하고 join_button_clicked가 호출되면 사진정보도 보내줌
    def find_button_clicked(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Open  file', './')
            if not fname:
                return
            self.editline_filepath.setText(fname[0])

            if os.path.getsize(fname[0]) == 0:
                QtWidgets.QMessageBox.about(self, 'fail', '다른 파일을 선택해주세요')
                return
            fname2, ext = os.path.splitext(fname[0])
            print(fname2)
            print(ext)
            if ext != '.jpg' and ext != '.png' and ext != '.jpeg' and ext != '.bmp':
                QtWidgets.QMessageBox.about(self, 'fail', '이미지 파일을 선택해주세요')
                self.editline_filepath.setText('')
                return

        except Exception as e:
            print(e)
            return

    def join_button_clicked(self):
        if len(self.editline_id.text()) > 10:
            self.editline_id.setText(self.editline_id.text()[0:10])
        if len(self.editline_nickname.text()) > 10:
            self.editline_nickname.setText(self.editline_nickname.text()[0:10])
        if len(self.editline_password.text()) > 10:
            self.editline_password.setText(self.editline_password.text()[0:10])
        if len(self.editline_hobby.text()) > 10:
            self.editline_hobby.setText(self.editline_hobby.text()[0:10])
        if len(self.editline_age.text()) > 10:
            self.editline_age.setText(self.editline_age.text()[0:10])
        if len(self.editline_residence.text()) > 10:
            self.editline_residence.setText(self.editline_residence.text()[0:10])
        if len(self.intro.editline_introduce.toPlainText()) > 200:
            self.intro.editline_introduce.setText(self.intro.editline_introduce.toPlainText()[0:200])

        #self._client.msg_list.append('join_info')
        self._client.msg_list.append(self.editline_id.text())
        self._client.msg_list.append(self.editline_password.text())
        self._client.msg_list.append(self.editline_residence.text())
        self._client.msg_list.append(self.editline_hobby.text())
        self._client.msg_list.append(self.editline_age.text())
        self._client.msg_list.append(self.editline_nickname.text())
        if self.male_radio.isChecked():
            self._client.msg_list.append('남성')
        else:
            self._client.msg_list.append('여성')
        self._client.msg_list.append(self.intro.editline_introduce.toPlainText())

        tmp_list = copy.deepcopy(self._client.msg_list)
        self._client.msg_list.insert(0,'join_info')

        if self.intro.editline_introduce.toPlainText() and self.editline_filepath.toPlainText() and self.editline_id.text() and self.editline_password.text() and self.editline_residence.text() and self.editline_hobby.text() and self.editline_age.text() and self.editline_nickname.text() :
            self._client.client_send()
            self._client.client_recv()
            print("recving list")
        else:
            QtWidgets.QMessageBox.about(self, 'join fail', '빈 정보를 채워주세요')
            self._client.msg_list = []
            return

        if self._client.msg_list_server[1]:
            self._client.mkdir()
            matchlist = []

            f = open('./id_' + self.editline_id.text() + '/match/match_candidate_list.txt', 'wb')
            f.write(pickle.dumps(matchlist))
            f.close()

            f = open('./id_' + self.editline_id.text() + '/match/match_list.txt', 'wb')
            f.write(pickle.dumps(matchlist))
            f.close()

            f = open('./id_' + self.editline_id.text() + '/my_profile.txt', 'wb')
            f.write(pickle.dumps(tmp_list))
            f.close()
            QtWidgets.QMessageBox.about(self, 'join success', '회원가입 성공')
        else:
            QtWidgets.QMessageBox.about(self, 'join failed', '아이디가 이미 존재합니다')
            return
        print(self._client.msg_list_server[1])

        #['img_send',내 id, 이미지 size, 사진인덱스]
        self._client.img_resize(self.editline_filepath.toPlainText())
        self._client.msg_list.append('img_send')
        self._client.msg_list.append(self.editline_id.text())
        self._client.msg_list.append(self._client.img_size('./tmp/resized.jpg'))
        self._client.msg_list.append(1)
        self._client.client_ftp_send('./tmp/resized.jpg')
        #self._client.img_send('resized.jpg')
        fp = open('./tmp/resized.jpg','rb')

        f = open('./id_' + self.editline_id.text() + '/me1.jpg','wb')
        f.write(fp.read())
        f.close()
        fp.close()

        self._client.img_resize('./tmp/base_image.png')
        self._client.msg_list.append('img_send')
        self._client.msg_list.append(self.editline_id.text())
        self._client.msg_list.append(self._client.img_size('./tmp/resized.jpg'))
        self._client.msg_list.append(2)
        self._client.client_ftp_send('./tmp/resized.jpg')
        #self._client.img_send('base_image.jpg')
        #self._client.client_recv()
        fp = open('./tmp/resized.jpg', 'rb')
        fread = fp.read()
        fp.close()
        f = open('./id_' + self.editline_id.text() + '/me2.jpg', 'wb')
        f.write(fread)
        f.close()

        self._client.msg_list.append('img_send')
        self._client.msg_list.append(self.editline_id.text())
        self._client.msg_list.append(self._client.img_size('./tmp/resized.jpg'))
        self._client.msg_list.append(3)
        self._client.client_ftp_send('./tmp/resized.jpg')
        #self._client.img_send('base_image.jpg')
        #self._client.client_recv()
        f = open('./id_' + self.editline_id.text() + '/me3.jpg', 'wb')
        f.write(fread)
        f.close()
        self._client.number_of_widgets = self._client.number_of_widgets - 1
        self.start_login_signal.emit()
        self.close()

        self.editline_id.clear()
        self.editline_password.clear()
        self.editline_residence.clear()
        self.editline_hobby.clear()
        self.editline_age.clear()
        self.editline_nickname.clear()
        self.intro.editline_introduce.clear()
        self.editline_filepath.clear()

    def close_button_clicked(self):
        self._client.number_of_widgets = self._client.number_of_widgets - 1
        self.start_login_signal.emit()
        self.close()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "회원가입"))
        self.label_5.setText(_translate("Form", "취미"))
        #self.label_3.setText(_translate("Form", "Insert Your Profile"))
        self.label_2.setText(_translate("Form", "비밀번호"))
        self.label_4.setText(_translate("Form", "거주지"))
        self.label_6.setText(_translate("Form", "나이"))
        self.label_8.setText(_translate("Form","닉네임"))
        self.label_7.setText(_translate("Form", "*사진을 선택하세요"))
        self.label.setText(_translate("Form", "아이디"))
        self.join_button.setText(_translate("Form", "회원가입"))
        self.close_button.setText(_translate("Form", "닫기"))
        self.find_button.setText(_translate("Form", "사진 찾기"))
        self.intro_button.setText(_translate("Form", "자기소개"))


class login_ui(QtWidgets.QWidget, QtCore.QObject):
    start_main_signal = QtCore.pyqtSignal()
    start_join_signal = QtCore.pyqtSignal()

    def __init__(self, _client, parent=None):
        super(login_ui, self).__init__(parent)
        QtCore.QObject.__init__(self)
        self._client = _client
        self.setupUi()

    def setupUi(self):
        # disable (but not hide) close button
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)

        self.setObjectName("Form")
        self.resize(750, 520)

        self.login_button = QtWidgets.QPushButton(self)
        self.login_button.setGeometry(QtCore.QRect(150, 330, 111, 61))
        self.login_button.setObjectName("login_button")
        self.login_button.setFixedSize(100, 50)

        self.join_button = QtWidgets.QPushButton(self)
        self.join_button.setGeometry(QtCore.QRect(315, 330, 101, 61))
        self.join_button.setObjectName("join_button")
        self.join_button.setFixedSize(100,50)

        self.exit_button = QtWidgets.QPushButton(self)
        self.exit_button.setGeometry(QtCore.QRect(480, 330, 111, 61))
        self.exit_button.setObjectName("exit_button")
        self.exit_button.setFixedSize(100, 50)

        self.label_id = QtWidgets.QLabel(self)
        self.label_id.setGeometry(QtCore.QRect(140, 100, 56, 12))
        self.label_id.setObjectName("label_id")
        self.label_id.setFixedSize(150, 30)

        self.label_password = QtWidgets.QLabel(self)
        self.label_password.setGeometry(QtCore.QRect(140, 200, 56, 12))
        self.label_password.setObjectName("label_password")
        self.label_password.setFixedSize(150,30)

        self.editline_id = QtWidgets.QLineEdit(self)
        self.editline_id.setGeometry(QtCore.QRect(290, 80, 161, 51))
        self.editline_id.setText("")
        self.editline_id.setObjectName("editline_id")
        self.editline_id.setFixedSize(300,30)


        self.editline_password = QtWidgets.QLineEdit(self)
        self.editline_password.setGeometry(QtCore.QRect(290, 180, 161, 51))
        self.editline_password.setText("")
        self.editline_password.setObjectName("editline_password")
        self.editline_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.editline_password.setFixedSize(300,30)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.login_button.clicked.connect(self.login_button_clicked)
        self.join_button.clicked.connect(self.join_button_clicked)
        self.exit_button.clicked.connect(self.exit_button_clicked)

        login_ = QtWidgets.QVBoxLayout()
        gb = QtWidgets.QGroupBox('로그인')
        login_.addWidget(gb)

        login_interface = QtWidgets.QVBoxLayout()
        login_box = QtWidgets.QHBoxLayout()
        login_label = QtWidgets.QVBoxLayout()
        login_text = QtWidgets.QVBoxLayout()
        login_button = QtWidgets.QHBoxLayout()

        login_box.addLayout(login_label)
        login_box.addLayout(login_text)
        login_interface.addLayout(login_box)
        login_interface.addLayout(login_button)

        login_button.addWidget(self.login_button)
        login_button.addWidget(self.join_button)
        login_button.addWidget(self.exit_button)

        login_label.addWidget(self.label_id)
        login_label.addWidget(self.label_password)

        login_text.addWidget(self.editline_id)
        login_text.addWidget(self.editline_password)

        gb.setLayout(login_interface)
        self.setLayout(login_)


    def login_button_clicked(self):
        self._client.msg_list.append('login_info')
        self._client.msg_list.append(self.editline_id.text())
        self._client.msg_list.append(self.editline_password.text())
        #self._client.instruction = 'login_info'
        self._client.client_send()
        self._client.client_recv()
        if self._client.msg_list_server[1]:
            QtWidgets.QMessageBox.about(self, 'login success', '반갑습니다!')
            self._client.mkdir()
            self._client.my_id = self.editline_id.text()
            #self._client.my_dir = self._client.my_dir + '/id_' +self._client.my_id
            self._client.number_of_widgets = self._client.number_of_widgets - 1
            self.start_main_signal.emit()
            self.close()
        else:
            QtWidgets.QMessageBox.about(self, 'login failed', '아이디 또는 비밀번호를 확인하세요')

    def join_button_clicked(self):
        self._client.number_of_widgets = self._client.number_of_widgets - 1
        self.start_join_signal.emit()
        self.close()

    def exit_button_clicked(self):
        tmp = self._client.number_of_widgets - 1
        self._client.number_of_widgets = self._client.number_of_widgets - 1
        if not tmp:
            self._client.msg_list.append('exit_login')
            #self._client.msg_list.append(self._client.my_id)
            self._client.client_send()
        self.close()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "데이팅 어플"))
        self.join_button.setText(_translate("Form", "회원가입"))
        self.label_password.setText(_translate("Form", "비밀번호"))
        self.exit_button.setText(_translate("Form", "종료"))
        self.label_id.setText(_translate("Form", "아이디"))
        self.login_button.setText(_translate("Form", "로그인"))
