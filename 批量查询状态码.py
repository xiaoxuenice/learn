from tkinter import *
from socket import gethostbyname
import time,requests,threading
LOG_LINE_NUM = 0
class MY_GUI_SET():
    """小工具"""

    def __init__(self, init_window_name):
        self.init_window_name = init_window_name
        self.ipdz=''

    def set_init_window(self):
        self.init_window_name.title("不要加 http://     红色和4开头 再测试一次或者打开浏览器测试")
        self.init_window_name.geometry("860x660+10+10")

        self.init_window_name.resizable(0, 0)
        self.init_window_name.attributes("-alpha", 1)  # 虚化 值越小虚化程度越高
        # 标签
        self.init_data_label = Label(self.init_window_name, text="输入域名")
        self.init_data_label.grid(row=0, column=0)
        self.name_data_label = Label(self.init_window_name, text="主机ip\t\t       状态码\t域名")
        self.name_data_label.grid(row=0, column=14)
        #  滚动条
        self.scroll1 = Scrollbar()
        self.scroll2 = Scrollbar()
        # 文本框
        self.init_data_Text = Text(self.init_window_name, width=45, height=39,font=2)  # 原始数据录入框
        self.scroll2.config(command=self.init_data_Text.yview)
        self.init_data_Text.config(yscrollcommand=self.scroll2.set)
        self.init_data_Text.grid(row=1, column=0, rowspan=3, columnspan=10)
        self.scroll2.grid(row=1, column=11,rowspan=3, columnspan=1, sticky='nsw')

        self.name_data_Text = Text(self.init_window_name, width=45, height=39,font=2)  # 处name果展示
        self.scroll1.config(command=self.name_data_Text.yview)
        self.name_data_Text.config(yscrollcommand=self.scroll1.set)
        self.name_data_Text.grid(row=1, column=14, rowspan=3, columnspan=10)
        self.scroll1.grid(row=1, column=25, rowspan=3, columnspan=1, sticky='nsw')


        self.name_data_Text.tag_config("tag2", foreground="green",font=2)
        self.name_data_Text.tag_config("tag1", foreground="red", font=2)
        self.str_trans_to_md5_button = Button(self.init_window_name, text="开始测试", bg="lightblue", width=10,
                                              command=lambda: self.thread_it(self.SH))  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=1, column=12)

    @staticmethod
    def thread_it(func):
        t = threading.Thread(target=func)
        t.setDaemon(True)  # 守护--就算主界面关闭，线程也会留守后台运行（不对!）
        t.start()
    def SH(self):
        a = self.init_data_Text.get(1.0, END).strip()
        a=a.split("\n")
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
            "accept": "text/plain, */*; q=0.01"}
        for i in a:
            self.ipdz=''
            i = i.strip()
            try:
                self.ipdz = gethostbyname(i)
                ztm=requests.get("http://" + str(i), headers=headers,stream=True).status_code

                strr=str(self.ipdz)+"     \t"+str(ztm)+"     \t"+i+"\n"
                self.name_data_Text.insert(END,strr,"tag2")
            except Exception as f:
                print(f)
                print(self.ipdz)
                strr = i +"     \t"+ str(self.ipdz)+"     \n" +str(f)+"\n"
                self.name_data_Text.insert(END,strr, "tag1")

            time.sleep(0.5)


if __name__=="__main__":
    init_window = Tk()
    MY_GUI_SET(init_window).set_init_window()
    init_window.mainloop()
