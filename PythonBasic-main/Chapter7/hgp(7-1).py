#--------------------------------------------------------------------------------------------------------

# import math

# print(math.sin(1))

# print(math.cos(1))

# print(math.tan(1))

# print(math.floor(2.5))

# print(math.ceil(2.5))

#--------------------------------------------------------------------------------------------------------

# import math

# print(round(1.5))
# print(round(2.5))
# print(round(3.5))
# print(round(4.5))

#--------------------------------------------------------------------------------------------------------

# from math import sin, cos, tan, floor, ceil

# print(sin(1))
# print(cos(1))
# print(tan(1))
# print(floor(2.5))
# print(ceil(2.5))

#--------------------------------------------------------------------------------------------------------

import math as yeon

print(yeon.sin(1))
print(yeon.cos(1))
print(yeon.tan(1))
print(yeon.floor(2.5))
print(yeon.ceil(2.5))

#--------------------------------------------------------------------------------------------------------

# import random
# print(" # random 모듈")

# # random(): 0.0 <= x <1.0 사이의 float를 리턴합니다.

# print("- random(): ", random.random())

# # uniform(min.max): 지정한 범위 사이의 float를 리턴합니다.

# print("- uniform(10, 20):", random.uniform(10,20))

# # randrange() : 지정한 범위의 int 를 리턴합니다.
# #~randrange(max) : 0 부터 max 사이의 값을 리턴합니다.
# #~randrange(min,max) : min 부터 max 사이의 값을 리턴합니다.
# print("- randrange(10):", random.randrange(10))

# # choice(list) : 리스트 내부에 있는 요소를 랜덤하게 선택합니다.
# print("- choice([1,2,3,4,5]):", random.choice([1,2,3,4,5]))

# # shuffle(list) : 리스트의 요소들을 랜덤하게 섞습니다.
# print("- shuffle([1,2,3,4,5]):", random.shuffle([1,2,3,4,5]))

# # sample(list, k=<숫자>) : 리스트의 요소 중에 K개를 뽑습니다.
# print("- sample([1,2,3,4,5]), k=2):", random.sample([1,2,3,4,5], k=2))

#--------------------------------------------------------------------------------------------------------

# # 모듈을 읽어 들입니다.

# import sys

# # 명령 매개변수를 출력합니다.
# print(sys.argv)
# print("---")

# # 컴퓨터 환경과 관련된 정보를 출력합니다.
# print("getwindowsversion:()", sys.getwindowsversion())
# print("---")
# print("copyright", sys.copyright)
# print("---")
# print("version:", sys.version)

# # 프로그램을 강제로 종료합니다.
# sys.exit()

#--------------------------------------------------------------------------------------------------------

# # 모듈을 읽어 들입니다.

# import os

# # 기본 정보를 몇 개 출력해 봅니다.

# print("현재 운영체제:", os.name)
# print("현재 폴더:", os.getcwd)
# print("현재 폴더 내부의 요소:", os.listdir())

# # 폴더를 만들고 제거합니다.(폴더가 비어 있을떄만 제거 가능.)

# os.mkdir("hello")
# os.rmdir("hello")

# # 파일을 생성하고 + 파일 이름을 변경합니다.

# with open("original.txt" , "w") as file:
#     file.write("hello")
# os.rename("original.txt", "new.txt")

# # 파일을 제거합니다.
# os.remove("new.txt")
# #os.unlink("new.txt")

# # 시스템 명령어 실행
# os.system("dir")

#--------------------------------------------------------------------------------------------------------

# # 모듈을 읽어 들입니다.

import datetime

# 현재 시각을 구하고 출력하기

print("# 현재 시각 출력하기")
now = datetime.datetime.now()
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")
print()

# 시간 출력 방법
print("# 시간을 포맷에 맞춰 출력하기")
output_a = now.strftime("%Y.%m.%d %H:%M:%S")
output_b = "{}년 {}월 {}일 {}시 {}분 {}초".format(now.year,\
    now.month,\
    now.day,\
    now.hour,\
    now.minute,\
    now.second)
output_c = now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초")
print(output_a)
print(output_b)
print(output_c)
print()

#--------------------------------------------------------------------------------------------------------

# 모듈을 읽어 들입니다.

import datetime
now = datetime.datetime.now()

# 특정 시간 이후의 시간 구하기

print("# datetime.timedelta로 시간 더하기")
after = now + datetime.timedelta(\
    weeks=1,\
    days=1,\
    hours=1,\
    minutes=1,\
    seconds=1)

print(after.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년일월시분초"))
print()

# 특정 시간 요소 교체하기

print("# now.replace()로 1년 더하기")
output = now.replace(year=(now.year + 1))
print(output.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))

#--------------------------------------------------------------------------------------------------------

import time

print("지금부터 5초 동안 정지합니다!")
time.sleep(5)
print("프로그램을 종료합니다.")

#--------------------------------------------------------------------------------------------------------

# 모듈을 읽어 들입니다.

from urllib import request

# urlopen() 함수로 구글의 메인 페이지를 읽습니다.

target = request.urlopen("https://google.com")
output = target.read()

# 출력합니다.
print(output)

#--------------------------------------------------------------------------------------------------------

# 모듈을 읽어 들입니다.
from math import sin, cos, tan, floor, ceil

# sin, cos, tan를 구합니다.
print("sin(1):", sin(1))
print("cos(1):", cos(1))
print("tan(1):", tan(1))

# 내림과 올림을 구합니다.
print("floor(2.5):", floor(2.5))
print("ceil(2.5):", ceil(2.5))

#--------------------------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"

#--------------------------------------------------------------------------------------------------------
