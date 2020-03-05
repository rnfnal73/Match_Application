import sys
from PyQt5 import QtWidgets
import client
from PyQt5 import QtCore
import match
import chat
import profile
import main


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self._client = client.client()

        # ui 객체 선언
        self.login_uii = profile.login_ui(self._client)
        self.join_uii = profile.join_ui(self._client)
        self.my_profile_uii = profile.my_profile_ui(self._client)
        self.main_uii = main.main_ui(self._client)
        self.do_match_uii = match.do_match_ui(self._client)
        self.my_match_uii = match.my_match_ui(self._client)
        self.anonymous_chat_uii = chat.anonymous_chat_ui(self._client)

        self.login_uii.start_main_signal.connect(self.startMainUI)
        self.login_uii.start_join_signal.connect(self.startJoinUI)
        self.main_uii.my_profile_button.clicked.connect(self.startProfileUI)
        self.main_uii.do_match_button.clicked.connect(self.startDomatchUI)
        self.my_profile_uii.start_main_signal.connect(self.startMainUI)
        self.join_uii.start_login_signal.connect(self.startLoginUI)
        self.do_match_uii.start_main_signal.connect(self.startMainUI)
        self.my_match_uii.start_main_signal.connect(self.startMainUI)
        self.main_uii.my_match_button.clicked.connect(self.startMymatchUI)
        self.main_uii.anonymous_chat_button.clicked.connect(self.startRandomchatUI)
        self.anonymous_chat_uii.start_main_signal.connect(self.startMainUI)
        self.startLoginUI()

    def startLoginUI(self):
        self._client.number_of_widgets=self._client.number_of_widgets+1
        self.login_uii.setWindowTitle(QtCore.QCoreApplication.translate("Form", "로그인"))
        self.login_uii.show()

    def startJoinUI(self):
        self._client.number_of_widgets=self._client.number_of_widgets+1
        self.join_uii.setWindowTitle(QtCore.QCoreApplication.translate("Form", "회원가입"))
        self.join_uii.show()

    def startMainUI(self):
        self._client.number_of_widgets=self._client.number_of_widgets+1
        self.main_uii.count_users()
        self.main_uii.setWindowTitle(QtCore.QCoreApplication.translate("Form", "메인화면_"+self._client.my_id))
        self.main_uii.show()

    def startProfileUI(self):
        self._client.number_of_widgets=self._client.number_of_widgets+1
        self.main_uii.close_button_clicked()
        self.my_profile_uii.setWindowTitle(QtCore.QCoreApplication.translate("Form", "프로필_"+self._client.my_id))
        self.my_profile_uii.initiate_profile()
        self.my_profile_uii.show()

    def startDomatchUI(self):
        self._client.number_of_widgets = self._client.number_of_widgets + 1
        self.main_uii.close_button_clicked()
        self.do_match_uii.setWindowTitle(QtCore.QCoreApplication.translate("Form", "매치하기_" + self._client.my_id))
        self.do_match_uii.initiate_match()

    def startMymatchUI(self):
        self._client.number_of_widgets = self._client.number_of_widgets + 1
        self.main_uii.close_button_clicked()
        self.my_match_uii.setWindowTitle(QtCore.QCoreApplication.translate("Form", "매치목록_" + self._client.my_id))
        self.my_match_uii.initiate_my_match()

    def startRandomchatUI(self):
        self._client.number_of_widgets = self._client.number_of_widgets + 1
        self.main_uii.close_button_clicked()
        self.anonymous_chat_uii.anonymous_chat_initiate()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myWindow = MyWindow()
    app.exec_()
