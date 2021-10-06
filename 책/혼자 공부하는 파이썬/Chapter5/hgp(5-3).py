#--------------------------------------------------------------------------------------------------------

# tuple_test = (10,20,30)

# print(tuple_test[0])
# print(tuple_test[1])
# print(tuple_test[2])

#--------------------------------------------------------------------------------------------------------

# # 리스트와 튜플의 특이한 사용

# [a, b] = [10,20]
# (c, d) = (10,20)

# # 출력

# print("a:", a)
# print("b:", b)
# print("c:", c)
# print("d:", d)

#--------------------------------------------------------------------------------------------------------

# # 괄호가 없는 튜플

# tuple_test = 10,20,30,40
# print("# 괄호가 없는 튜플의 값과 자료형 출력")
# print("tuple_test:",tuple_test)
# print("type(tuple_test):", type(tuple_test))
# print()

# # 괄호가 없는 튜플 활용
# a,b,c = 10,20,30
# print("# 괄호가 없는 튜플을 활용한 할당")
# print("a:", a)
# print("b:", b)
# print("c:", c)

#--------------------------------------------------------------------------------------------------------

# a, b = 10,20

# print("# 교환 전 값")
# print("a:",a)
# print("b:",b)
# print()

# # 값 교환

# a, b = b, a

# print("# 교환 후 값")
# print("a:", a)
# print("b:", b)
# print()

#--------------------------------------------------------------------------------------------------------

# # 함수 선언

# def test():
#     return (10,20)

# # 여러 개의 값 리턴

# a, b = test()

# # 출력

# print("a:", a)
# print("b:", b)

#--------------------------------------------------------------------------------------------------------

# # 함수를 선언합니다.

# def power(item):
#     return item * item

# def under_3(item):
#     return item < 3

# # 변수를 선언합니다.

# list_input_a = [1,2,3,4,5]

# # map() 함수를 사용합니다.

# output_a = map(power, list_input_a)
# print("# map() 함수의 실행결과")
# print("map(power, list_input_a):", output_a)
# print("map(power, list_input_a):", list(output_a))
# print()

# # filter() 함수를 사용합니다.

# output_b = filter(under_3, list_input_a)
# print("# filter() 함수의 실행결과")
# print("filter(under_3, list_input_a):", output_b)
# print("filter(under_3, list_input_a):", list(output_b))

#--------------------------------------------------------------------------------------------------------

# # 함수를 선언합니다.

# power = lambda x: x * x
# under_3 = lambda x: x < 3

# # 변수를 선언합니다.

# list_input_a = [1,2,3,4,5]

# # map() 함수를 사용합니다.

# output_a = map(power, list_input_a)
# print("# map() 함수의 실행결과")
# print("map(power, list_input_a):", output_a)
# print("map(power, list_input_a):", list(output_a))
# print()

# # filter() 함수를 사용합니다.

# output_b = filter(under_3, list_input_a)
# print("# filter() 함수의 실행결과")
# print("filter(under_3, list_input_a):", output_b)
# print("filter(under_3, list_input_a):", list(output_b))

#--------------------------------------------------------------------------------------------------------

# # 변수를 선언합니다.

# list_input_a = [1,2,3,4,5]

# # map() 함수를 사용합니다.

# output_a = map(lambda x: x* x , list_input_a)
# print("#map() 함수의 실행결과")
# print("map(power, list_input_a):", output_a)
# print("map(power, list_input_a):", list(output_a))
# print()

# # filter() 함수를 사용합니다.

# output_b = filter(lambda x: x < 3, list_input_a)
# print("# filter() 함수의 실행결과")
# print("filter(under_3, list_input_a):", output_b)
# print("filter(under_3, list_input_a):", list(output_b))

#--------------------------------------------------------------------------------------------------------

# # 파일을 엽니다.

# file = open("basic.txt", "w")

# # 파일에 텍스트를 씁니다.

# file.write("hello python programing...!")

# # 파일을 닫습니다.

# file.close()

#--------------------------------------------------------------------------------------------------------

# # 파일을 엽니다.

# with open("basic.txt", "r") as file:
#     # 파일을 읽고 출력합니다.
#     contents = file.read()

# print(contents)

#--------------------------------------------------------------------------------------------------------

# # 랜덤한 숫자를 만들기 위해 가져옵니다.

# import random

# # 간단한 한글 리스트를 만듭니다.

# hanguls = list("가나다라마바사아자차카타파하")

# # 파일을 쓰기 모드로 엽니다.

# with open("into txt", "w") as file:
#     for i in range (1000):
#         #랜덤한 값으로 변수를 생성합니다.
#         name = random.choice(hanguls) + random.choice(hanguls)
#         weight = random.randrange(40, 100)
#         height = random.randrange(140,200)
#         #텍스트를 씁니다.
#         file.write("{},{},{}\n".format(name,weight,height))

#--------------------------------------------------------------------------------------------------------

# with open("into.txt" , "r") as file:
#     for line in file:
#         #변수를 선언합니다.
#         (name, weight, height) = line.strip().split(", ")

#         # 데이터가 문제없는지 확인합니다. 문제가 없으면 지나감
#         if (not name) or (not weight) or (not height):
#             continue

#         #결과를 계산합니다.
#         bmi = int(weight) / ((int(height) / 100) **2)
#         result = ""
#         if 25 <= bmi:
#             result = "과체중"
#         elif 18.5 <= bmi:
#             result = "정상 체중"
#         else:
#             result = "저체중"
        
#         #출력합니다.

#         print('\n'.join([
#             "이름 : {}",
#             "몸무게 : {}",
#             "키 : {}",
#             "BMI : {}",
#             "결과 : {}"
#         ]).format(name, weight, height, bmi, result))
#         print()


# # 안됨 파일을 찾을수 없다고함

#--------------------------------------------------------------------------------------------------------

# # 함수를 선언합니다.

# def test():
#     print("함수가 호출되었습니다.")
#     yield "test"

# # 함수를 호출합니다.

# print("A 지점 통과")
# test()

# print("A 지점 통과")
# test()

# print("B 지점 통과")
# test()
# print(test())

#--------------------------------------------------------------------------------------------------------

# # 함수를 선언합니다.

# def test():
#     print("A 지점 통과")
#     yield 1
#     print("B 지점 통과")
#     yield 2
#     print("C 지점 통과")

# # 함수를 호출합니다.

# output = test()

# # next() 함수를 호출합니다.

# print("D 지점 통과")
# a = next(output)
# print(a)

# print("E 지점 통과")
# b = next(output)
# print(b)

# print("F 지점 통과")
# c = next(output)
# print(c)

# #한 번 더 실행하기

# next(output)

#--------------------------------------------------------------------------------------------------------

# # 매개 변수로 받은 함수를 10번 호출하는 함수

# def call_10_times(func):
#     for i in range(10):
#         func()

# # 간단하게 출력하는 함수

# def print_hello():
#     print("안녕하세요")

# # 조합하기
# call_10_times(print_hello)

####################################################################################################################

# 파일을 엽니다.
with open("basic.txt", "w") as file:
    # 파일에 텍스트를 씁니다.
        file.write("hello python programing....!")