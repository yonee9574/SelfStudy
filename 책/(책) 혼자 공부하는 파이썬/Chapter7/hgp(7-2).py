#--------------------------------------------------------------------------------------------------------

# # 모듈을 읽어 들입니다. (외부모듈)

# from urllib import request
# from bs4 import BeautifulSoup #module not found 에러가 납니다. 

# # urlopen() 함수로 기상청의 전국 날씨를 읽습니다.

# target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

# # BeautifulSoup 이용해 웹 페이지를 분석합니다.
# soup = BeautifulSoup(target, "html.parser")

# # location 태그를 찾습니다.
# for location in soup.select("location"):
#     #내부의 city,wf,tmn,tmx 태그를 찾아 출력합니다.
#     print("도시:", location.select_one("city").string)
#     print("날씨:", location.select_one("wf").string)
#     print("최저기온:", location.select_one("tmn").string)
#     print("최고기온:", location.select_one("tmx").string)
#     print()

#--------------------------------------------------------------------------------------------------------

# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "<h1>Hello World!</h1>"

#--------------------------------------------------------------------------------------------------------

# # 모듈을 읽어 들입니다.

# from flask import Flask
# from urllib import request
# from bs4 import BeautifulSoup

# # 웹 서버를 생성합니다.

# app = Flask(__name__)
# @app.route("/")

# def hello():
#     #urlopen () 함수로 기상청의 전국 날씨를 읽습니다.
#     target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

#     #BeautifulSoup를 사용해 웹 페이지를 분석합니다.
#     soup = BeautifulSoup(target, "html.parser")

#     #location 태그를 찾습니다.
#     output = ""
#     for location in soup.select("location"):
#         #내부의 city, wf, tmn, tmx 태그를 찾아 출력합니다.
#         output += "<h3>{}</h3>".format(location.select_one("city").string)
#         output += "날씨: {}<br/>".format(location.select_one("wf").string)
#         output += "최저/최고 기온: {}/{}"\
#             .format(\
#                 location.select_one("tmn").string,\
#                 location.select_one("tmx").string\
#                     )
#         output += "<hr/>"
#     return output

#--------------------------------------------------------------------------------------------------------

# # 모듈을 읽어 들입니다.

# from math import sin, cos, tan, floor, ceil

# # sin, cos, tan를 구합니다.

# print("sin(1):", sin(1))
# print("cos(1):", cos(1))
# print("tan(1):", tan(1))

# # 내림과 올림을 구합니다.

# print("floor(2.5):", floor(2.5))
# print("ceil(2.5):", ceil(2.5))

#--------------------------------------------------------------------------------------------------------

# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "<h1>Hello World!</h1>"

#--------------------------------------------------------------------------------------------------------

# def hello():
#     print("hello")

#--------------------------------------------------------------------------------------------------------

# def test(funtion):
#     def wrapper():
#         print("인사가 시작되었습니다.")
#         funtion()
#         print("인사가 종료되었습니다.")
#     return wrapper

# # 데코레이터를 붙여 함수를 만듭니다.
# @test
# def hello():
#     print("hello")

# # 함수를 호출합니다.
# hello()

#--------------------------------------------------------------------------------------------------------

# # 모듈을 가져옵니다.
# from functools import wraps

# # 함수로 데코레이터를 생성합니다.
# def test(function):
#     @wraps(function)
# def wrapper(*arg, **kwargs):
#     print("인사가 시작되었습니다.")
#     function(*arg, **kwargs)
#     print("인사가 종료되었습니다.")
#     return wrapper

#--------------------------------------------------------------------------------------------------------

