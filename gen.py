#参考自https://blog.csdn.net/hackzkaq/article/details/119676876
from urllib.parse import urlencode
import execjs # 导入PyExecJS 库
import os

def get_js(): # 导入js文件
    f = open("login.js", 'r', encoding='UTF-8')
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr + line
        line = f.readline()
    f.close()
    return htmlstr

print("Please enter the router ip:")
ip = input()
print("Please enter password: ")
passwd = input()
jsstr = get_js()
ctx = execjs.compile(jsstr)
utf = ctx.call("tokenGen", passwd)
#print(utf)
en = urlencode(utf, encoding='utf-8')
cmd = "curl -X POST -H \"Accept-Encoding:gzip, deflate\" -H \"Accept-Language:zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7\" -H \"Host:192.168.114.1\" -H \"Connection:keep-alive\" -H \"User-Agent:Mozilla/5.0 (Linux; Android 12; 22081212C Build/SKQ1.220303.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36\" -H \"Content-Length:126\" -H \"Accept:*/*\" -H \"X-Requested-With:XMLHttpRequest\" -H \"Content-Type:application/x-www-form-urlencoded; charset=UTF-8\" -H \"Origin:http://"+ip+"\" -H \"Referer:http://"+ip+"/cgi-bin/luci/web\" -d \""+en+"\" \"http://"+ip+"/cgi-bin/luci/api/xqsystem/login\"|jq -r \".token\""
#print(cmd)
apikey = os.popen(cmd).read()[:-1]
print(os.popen("curl \"http://"+ip+"/cgi-bin/luci/;stok="+apikey+"/api/xqnetwork/pppoe_status\"|jq").read())