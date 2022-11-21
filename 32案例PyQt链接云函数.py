import sys
import json
import time
import requests

from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QThread,pyqtSignal
class LoginThread(QThread):
    #创建自定义信号
    start_login_signal=pyqtSignal(str)
    def __init__(self,signal):
        super(LoginThread, self).__init__()
        self.login_complete_signal=signal

    def login_by_requests(self,user_password_json):
        # 将json字符串，转换为自定，从而实现传递了用户名及密码 todo
        user_password_dict= json.loads(user_password_json)
        # print(user_password_json.get("user_name"))#dont do it ,it will show 'get do not contribute to str'it need dict
        # print(user_password_json.get("password"))
        # 使用requests模块发送请求(POST)
        r = requests.post(url="https://service-hderh1ls-1315173933.gz.apigw.tencentcs.com/release/qt_login",json=user_password_dict)
        print("接收到腾讯服务器的响应:", r.content.decode())
        ret=r.json()
        # print(r.json())

        print("这里要发送信号给UI线程。。。。")
        self.login_complete_signal.emit(json.dumps(ret))

    def run(self):
        while True:
            print("子线程正在执行。。。")
            time.sleep(1)

class MyWindow(QWidget):
    login_status_signal=pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("./QtDesiner/login-2.ui")
        self.user_name_qwidget = self.ui.lineEdit  # 用户名输入框
        self.password_qwidget = self.ui.lineEdit_2  # 密码输入框
        self.login_btn = self.ui.pushButton  # 登录按钮
        self.forget_password_btn = self.ui.pushButton_2  # 忘记密码按钮
        self.textBrowser = self.ui.textBrowser  # 文本显示区域

        # 绑定信号与槽函数
        self.login_btn.clicked.connect(self.login)

        # 创建个信hao用来让子线程登录成功之后像主线程发送
        self.login_status_signal.connect(self.login_status)
        # 创建一个子线程注意这里要将login_thread变量变为对象的属性，如果不是对象属性，而是一个普通的局部变量的话
        # 会随着init_ui函数执行结束而被释放况时夺线程还没有执行完毕所有会产生问题)
        self.login_thread=LoginThread(self.login_status_signal)
        self.login_thread.start_login_signal.connect(self.login_thread.login_by_requests)
        self.login_thread.start()

    def login(self):
        """登录按钮的槽函数"""
        user_name = self.user_name_qwidget.text()
        password = self.password_qwidget.text()
        #发送信号，让子线程开始登陆
        self.login_thread.start_login_signal.emit(json.dumps({"user_name": user_name,"password": password}))

    def login_status(self,status):
        print("status.. ..", status)
        status_dict = json.loads(status)
        self.textBrowser.setText(status_dict.get("errmsg"))
        self.textBrowser.repaint()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    # 展示窗口
    w.ui.show()

    app.exec()

