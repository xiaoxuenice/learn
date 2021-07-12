from selenium import  webdriver
from selenium.webdriver.support.select import Select
import time,os,re,easygui
with open('yuming.txt', 'r', encoding='utf-8') as f:
    all = f.read()
    all = all.split()
u=all[0].strip()
p=all[0].strip()
Web_url = "https://dns.he.net"
c = os.getenv("SystemDrive")  # 获取主盘符
path = c + "\chromedriver.exe"
header = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"}
a = webdriver.Chrome(executable_path=path, desired_capabilities=header)
print("正在打开浏览器.....")
# a.minimize_window()
a.get(Web_url)
a.find_element_by_name("email").send_keys(u)
a.find_element_by_name("pass").send_keys(p)
a.find_element_by_name("submit").click()
def change_cname(domain,cname):
    a.find_element_by_name(domain).click()
    b = re.findall("dns_tr\" id=\"(.*?)\"", a.page_source)
    a.find_element_by_id(b[-2]).click()
    time.sleep(1)
    a.find_element_by_id("_content").clear()
    a.find_element_by_id("_content").send_keys(cname)
    a.find_element_by_id("_hds").click()
    a.find_element_by_link_text("Return to main").click()
def add_domain(domain,cname):
    a.find_element_by_xpath("//a[contains(@onclick,'launchWindow')]").click()
    a.find_element_by_name("add_domain").send_keys(domain)
    a.find_element_by_name("submit").click()
    a.find_element_by_name(domain).click()
    a.find_element_by_link_text("New CNAME").click()
    time.sleep(1)
    a.find_element_by_id("_name").send_keys('www.{}'.format(domain))
    a.find_element_by_id("_content").send_keys(cname)
    a.find_element_by_id("_hds").click()
    a.find_element_by_link_text("New ALIAS").click()
    time.sleep(1)
    a.find_element_by_id("_name").send_keys(domain)
    a.find_element_by_id("_content").send_keys('www.{}'.format(domain))
    a.find_element_by_id("_hds").click()
    b = re.findall("dns_tr\" id=\"(.*?)\"", a.page_source)
    for i in b:
        a.find_element_by_id(i).click()
        time.sleep(1)
        c = a.find_element_by_name("TTL")
        time.sleep(1)
        Select(c).select_by_value("300")
        a.find_element_by_id("_hds").click()
    a.find_element_by_link_text("Return to main").click()
def aee():
    cname = all[2]
    for i in all[3::]:
        add_domain(i.strip(), cname.strip())
def bee():
    cname = all[2]
    for i in all[3::]:
        change_cname(i.strip(), cname.strip())
if __name__=="__main__":
    aux=easygui.choicebox('在程序同目录下 yuming.txt \n第一行写 用户名\n第二行写 密码\n第三行写 cname \n第四行写 域名\n第五行写 域名','注意',['添加域名','改CNAME'])
    if aux == "添加域名":
        aee()
    elif aux == "改CNAME":
        bee()
