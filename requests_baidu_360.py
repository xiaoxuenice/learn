from tkinter import *
import time,re,requests,random,threading
class MY_GUI_SET():

    def __init__(self, init_window_name):
        self.init_window_name = init_window_name

    def set_init_window(self):
        self.init_window_name.title("baidu & 360 关键字查询软件 以管理员身份运行")
        self.init_window_name.geometry("740x500+10+10")
        self.init_window_name.attributes("-alpha", 1)  # 虚化 值越小虚化程度越高
        # 标签
        self.init_data_label = Label(self.init_window_name, text="输入查询的域名")
        self.init_data_label.grid(row=0, column=0)
        self.name_data_label = Label(self.init_window_name, text="输入关键词")
        self.name_data_label.grid(row=0, column=12)
        self.result_data_label = Label(self.init_window_name, text="错误信息")
        self.result_data_label.grid(row=12, column=12)
        self.log_label = Label(self.init_window_name, text="请求频繁，遭到阻挡")
        self.log_label.grid(row=12, column=0)
        self.log_label = Label(self.init_window_name, text="信息输出")
        self.log_label.grid(row=24, column=0)

    # 文本框
        self.scroll = Scrollbar()
        self.log_Text = Text(self.init_window_name, width=102, height=14)  # jilu
        self.scroll.config(command=self.log_Text.yview)
        self.log_Text.config(yscrollcommand=self.scroll.set)
        self.log_Text.grid(row=26, column=0, columnspan=30)
        self.scroll.grid(column=90,row=26, sticky='NS')
        self.log_Text.tag_config("tag1", foreground="green", font=2)
        self.log_Text.tag_config("tag2", foreground="red", font=2)


        self.init_data_Text = Text(self.init_window_name, width=45, height=9)  # 原始数据录入框
        self.init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
        self.log_data_Text = Text(self.init_window_name, width=45, height=9)  # 日志框
        self.log_data_Text.grid(row=13, column=0, columnspan=10)

        self.name_data_Text = Text(self.init_window_name, width=45, height=9)  # 处name果展示
        self.name_data_Text.grid(row=1, column=12, rowspan=10, columnspan=10)
        self.result_data_Text = Text(self.init_window_name, width=45, height=9)  # 处理结果展示
        self.result_data_Text.grid(row=13, column=12, columnspan=10)

        # 按钮
        self.str_trans_to_md5_button = Button(self.init_window_name, text="baidu", bg="lightblue", width=10,command=lambda: self.thread_it(self.Rbaidu))  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=1, column=11)
        self.str_trans_to_md5_butt = Button(self.init_window_name, text="360", bg="lightblue", width=10,command=lambda: self.thread_it(self.R360))  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_butt.grid(row=5, column=11)
    @staticmethod
    def thread_it(func):
        t = threading.Thread(target=func)
        t.setDaemon(True)  # 守护--就算主界面关闭，线程也会留守后台运行（不对!）
        t.start()
    def Rbaidu(self):
        error = "百度安全验证"  # baidu
        fea = self.init_data_Text.get(1.0, END).strip()
        url = fea.split("\n")
        url = [i for i in url if i !='']
        uaList = ["Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
                  "Mozilla/5.0 (X11; Linux x86_64) Gecko/20100101 Firefox/60.0",
                  'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36']
        send_headers = {"User-Agent": random.choice(uaList), "accept": "text/plain, */*; q=0.01",
                        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,und;q=0.7", "Connection": "keep-alive"}
        name = self.name_data_Text.get(1.0, END).strip()
        c = name.split("\n")
        c = [i for i in c if i !='']
        for i in c:
          try:
            ci = (i.rstrip("\n"))
            u = 'https://www.baidu.com/s?wd={}'.format(ci)  # baidu
            a = requests.get(u, headers=send_headers).content.decode('utf-8')
            if error in a:
                self.log_data_Text.insert(END, ci+"\n")
                continue
            lb = re.findall(r"\"text-decoration\:none\;position\:relative\;\"\>(.*)?\/", a)

            strlb = ''.join(lb)
            z = "不在"
            for i in url:
                if i in strlb:
                    z = "在"
                    cc = ci + "    " + z + "\n"
                    self.log_Text.insert(END, cc, "tag1")
                    break
                else:
                    cc = ci + "    " + z + "\n"
                    self.log_Text.insert(END, cc, "tag2")
                    break
          except Exception as f :
              t=self.get_current_time()
              t="\n"+str(t)+"\n"
              self.result_data_Text.insert(END, t)
              self.result_data_Text.insert(END,f)

    def R360(self):

        error='360搜索_访问异常出错' 			 		 #360
        fea = self.init_data_Text.get(1.0, END).strip()
        url = fea.split("\n")
        url = [i for i in url if i != '']
        uaList = ["Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
                  "Mozilla/5.0 (X11; Linux x86_64) Gecko/20100101 Firefox/60.0",
                  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36']
        name = self.name_data_Text.get(1.0, END).strip()
        c = name.split("\n")
        c = [i for i in c if i != '']
        for i in c:
          try:
            ci = (i.rstrip("\n"))

            u='https://so.com/s?q={}&pn=1'.format(ci)      		 #360
            header = {'User-Agent': random.choice(uaList)}
            time.sleep(0.3)
            a = requests.get(u,headers=header).content.decode('utf-8')
            if error in a:
                self.log_data_Text.insert(END, ci+"\n")
                continue
            lb=re.findall(r"\<cite\>(.*?)</cite\>",a) 			     #360
            strlb = ''.join(lb)
            z = "不在"
            for i in url:
                if i in strlb:
                    z = "在"
                    cc=ci+"    "+z+"\n"
                    self.log_Text.insert(END,cc,"tag1")
                    break
                else:
                    cc = ci + "    " + z + "\n"
                    self.log_Text.insert(END, cc, "tag2")
                    break


          except Exception as f :
              t=self.get_current_time()
              t = "\n" + str(t) + "\n"
              self.result_data_Text.insert(END, t)
              self.result_data_Text.insert(END,f)

    def get_current_time(self):
        current_time = time.strftime('%H:%M:%S', time.localtime(time.time()))
        return current_time
if __name__=="__main__":
    init_window = Tk()
    MY_GUI_SET(init_window).set_init_window()
    init_window.mainloop()
