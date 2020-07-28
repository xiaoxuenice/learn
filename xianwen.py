import requests,re
send_headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"}
a=requests.get("http://www.360doc.com/content/17/0303/11/13179508_633585381.shtml",headers=send_headers).content.decode("utf-8")
dd=re.findall('700\;\"\>(.*?)<.*?28px\;\"\>(.*?)\<',a)
test=[]
n=0
for i in dd:
    if i[1] == "":
      dd[n+1]+=i
    n+=1
for i in dd:
    if i[1] == '':
        continue
    test.append(i)
for i in test:
    tt=[]
    for c in i:
        if c == "":
            continue
        tt.append(c)
    ee=""
    for b in range(len(tt)-1,1,-1):
          ee+=tt[b]
    ee+=tt[0]
    ee+="\n"
    ee+=tt[1]
    ee+="\n"
    with open("xianwen.txt",'a+') as f:
       f.write(ee)


