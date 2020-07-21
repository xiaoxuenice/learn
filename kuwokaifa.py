from tkinter import *
from selenium import  webdriver
import time,re,requests,os,zipfile
LOG_LINE_NUM = 0
class MY_GUI_SET():
    """小工具"""

    def __init__(self, init_window_name):
        self.init_window_name = init_window_name

    def set_init_window(self):
        self.init_window_name.title("酷我音乐免下载收费的下载软件  注意:收费听取的下载不了!    箭头转圈，请勿点击以免卡顿（管理员身份运行）")
        self.init_window_name.geometry("730x320+10+10")
        self.init_window_name.attributes("-alpha", 1)  # 虚化 值越小虚化程度越高
        # 标签
        self.init_data_label = Label(self.init_window_name, text="输入播放页url  例如:http://www.kuwo.cn/play_detail/111")
        self.init_data_label.grid(row=0, column=0)
        self.name_data_label = Label(self.init_window_name, text="输入歌曲名字")
        self.name_data_label.grid(row=0, column=12)
        self.result_data_label = Label(self.init_window_name, text="文件路径")
        self.result_data_label.grid(row=12, column=12)
        self.log_label = Label(self.init_window_name, text="下载信息")
        self.log_label.grid(row=12, column=0)
        self.log_label = Label(self.init_window_name, text="@ 2020版权所有       https://blog.51cto.com/982439641")
        self.log_label.grid(row=24, column=0)
    # 文本框
        self.init_data_Text = Text(self.init_window_name, width=45, height=9)  # 原始数据录入框
        self.init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
        self.log_data_Text = Text(self.init_window_name, width=45, height=9)  # 日志框
        self.log_data_Text.grid(row=13, column=0, columnspan=10)
        self.name_data_Text = Text(self.init_window_name, width=45, height=9)  # 处name果展示
        self.name_data_Text.grid(row=1, column=12, rowspan=10, columnspan=10)
        self.result_data_Text = Text(self.init_window_name, width=45, height=9)  # 处理结果展示
        self.result_data_Text.grid(row=13, column=12, columnspan=10)
        # 按钮
        self.str_trans_to_md5_button = Button(self.init_window_name, text="开始下载", bg="lightblue", width=10,
                                              command=self.Get_music_url)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=1, column=11)
    def Get_music_url(self):
        try:
            a=self.init_data_Text.get(1.0, END).strip().replace("\n", "").encode()
            b = self.name_data_Text.get(1.0, END).strip().replace("\n", "").encode()
            Web_url=str(a,encoding="utf-8")
            name=str(b,encoding="utf-8")
            c=os.getenv("SystemDrive")                 #获取主盘符
            path = c+ "\chromedriver.exe"
            self.write_log_to_Text("第一次安装环境会慢一点....")
            self.write_log_to_Text("检测浏览器驱动....")
            if not os.path.exists(path):                    #判断有没有Gg启动程序,安装Gg启动程序
                exe = requests.get("https://raw.githubusercontent.com/xiaoxuenice/xiaoxue/master/chromedriver.exe")
                with open('{}'.format(path), 'wb') as f:
                    f.write(exe.content)
                    self.write_log_to_Text("安装浏览器驱动....")
            g_path = c+"\Program Files (x86)\Google"
            if not os.path.exists(g_path):                       #判断有没有Gg浏览器,安装Gg浏览器
                g_exe=requests.get("https://raw.githubusercontent.com/xiaoxuenice/xiaoxue/master/Google.zip")
                with open('{}.zip'.format(g_path),'wb') as f:
                    f.write(g_exe.content)
                    a = zipfile.ZipFile("{}\Program Files (x86)\Google.zip".format(c))
                    a.extractall("{}\Program Files (x86)\\".format(c))
                    self.write_log_to_Text("安装浏览器....")

            header = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"}
            a = webdriver.Chrome(executable_path=path, desired_capabilities=header)
            self.write_log_to_Text("正在打开浏览器.....")
            a.minimize_window()
            a.get(Web_url)
            try:
                a.find_element_by_class_name("play").click()
                time.sleep(5)
                self.write_log_to_Text("正在获取歌曲url....")
                url = re.findall('src=\"(https\:\/\/.*?mp3)\"', a.page_source)[0]
                try:
                    url[0]
                except Exception as f :
                    self.write_log_to_Text("歌曲URL获取失败！！！\n")
                    exit()
                a.close()
                dir = c + "\歌曲"
                if not os.path.exists(dir):
                    os.makedirs(dir)
                mi = requests.get(url)
                with open('{}/{}.mp3'.format(dir,name), 'wb') as f:
                    f.write(mi.content)
                    self.result_data_Text.delete(1.0, END)
                    self.result_data_Text.insert(1.0, '{}\{}.mp3'.format(dir,name))
                    self.write_log_to_Text("歌曲{}下载成功！！！\n".format(name))
            except Exception as error:
                print(error)
                self.write_log_to_Text( "下载错误，付费歌曲！！！\n")
        except Exception as f:
            self.write_log_to_Text(f)
    # 获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%H:%M:%S', time.localtime(time.time()))
        return current_time

    # 日志动态打印
    def write_log_to_Text(self, logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) + " " + str(logmsg) + "\n"  # 换行
        if LOG_LINE_NUM <= 5:
            self.log_data_Text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0, 2.0)
            self.log_data_Text.insert(END, logmsg_in)

if __name__=="__main__":
    init_window = Tk()
    MY_GUI_SET(init_window).set_init_window()
    init_window.mainloop()





#pip3 install pyinstaller
#pip install pypiwin32
#pyinstall -F -w kuwokaifa.py
