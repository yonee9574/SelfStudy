#--------------------------------------------------------------------------------------------------------

# # 함수 선언

# def factorial(n):
#     # 변수 선언
#     output = 1
#     # 반복문을 돌려 숫자를 더함
#     for i in range(1, n + 1):
#         output *= i
#     #리턴
#     return output

# # 함수 호출

# print("1!:", factorial(1))
# print("2!:", factorial(2))
# print("3!:", factorial(3))
# print("4!:", factorial(4))
# print("5!:", factorial(5))

#--------------------------------------------------------------------------------------------------------

# # 함수 선언

# def factorial(n):
#     # n 이 0 이라면 1리턴
#     if n == 0:
#         return 1
#     # n이 0이 아니라면 n*(n-1)! 을 리턴
#     else:
#         return n * factorial(n-1)

# # 함수 호출

# print("1!:", factorial(1))
# print("2!:", factorial(2))
# print("3!:", factorial(3))
# print("4!:", factorial(4))
# print("5!:", factorial(5))

#--------------------------------------------------------------------------------------------------------

# # 변수 선언

# counter = 0

# # 함수 선언

# def fibonacci(n):
#     # 어떤 수를 구하는지 출력
#     print("fibonacci({})를 구합니다.".format(n))
#     global counter
#     counter +=1
    
#     #피보나치 수
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# # 함수 호출

# fibonacci(10)
# print("---")
# print("fibonacci(10) 계산에 활용된 덧셈 횟수는 {}번입니다.".format(counter))

#--------------------------------------------------------------------------------------------------------

# # 변수 선언

# counter = 0

# # 함수 선언

# def fibonacci(n):
#     counter += 1
#     #피보나치 수를 구합니다.
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# # 함수 호출
# print(fibonacci(10))

# #참조 오류

#--------------------------------------------------------------------------------------------------------

# # 메모 변수

# dictionary = {
#     1: 1,
#     2: 1
# }

# # 함수 선언

# def fibonacci(n):
#     if n in dictionary:
#         # 메모가 되어 있으면 메모된 값을 리턴
#         return dictionary[n]
#     else:
#         # 메모가 되어 있지 않으면 값을 구함
#         output = fibonacci(n - 1) + fibonacci(n - 2)
#         dictionary[n] = output
#         return output

# # 함수 호출
# print("fibonacci(10):", fibonacci(10))
# print("fibonacci(20):", fibonacci(20))
# print("fibonacci(30):", fibonacci(30))
# print("fibonacci(40):", fibonacci(40))
# print("fibonacci(50):", fibonacci(50))

#--------------------------------------------------------------------------------------------------------

# # 함수 선언

# def fibonacci(n):
#     if n in dictionary:
#         # 메모되어 있으면 메모된 값을 리턴
#         return dictionary[n]
#     else:
#         #메모되어 있지 않으면 값을 구함
#         output = fibonacci(n - 1) + fibonacci(n - 2)
#         dictionary[n] = output
#         return output

#--------------------------------------------------------------------------------------------------------

# # 함수 선언
# def fibonacci(n):
#     if n in dictionary:
#         #메모되어 있으면 메모된 값 리턴
#         return dictionary[n]
#     #메모 되어 있지 않으면 값을 구함
#     output = fibonacci(n - 1) + fibonacci(n - 2)
#     dictionary[n] = output
#     return output

#--------------------------------------------------------------------------------------------------------

# number_input_a = input("숫자 입력> ")
# radius = float(number_input_a)

# print(2*3.14*radius)
# print(3.14*radius*radius)

#--------------------------------------------------------------------------------------------------------

