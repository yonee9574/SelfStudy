#--------------------------------------------------------------------------------------------------------

# # try except 구문으로 예외를 처리합니다.

# try:
#     # 숫자로 변환합니다.
#     number_input_a = int(input("정수입력> "))
#     # 출력합니다.
#     print("원의 반지름:", number_input_a)
#     print("원의 둘레:", 2 * 3.14 * number_input_a)
#     print("원의 넓이:", 3.14 * number_input_a * number_input_a)
# except Exception as exception:
#     # 예외 객체를 출력해봅니다.
#     print("type(exception):", type(exception))
#     print("exception:", exception)

# # 정수 입력 > yes!! 를 했을때 
# # type(exception): <class 'ValueError'>
# # exception : invalid literal for int() with base 10: 'yes!!'

#--------------------------------------------------------------------------------------------------------

# # 변수를 선언합니다.

# list_number = [52,273,32,72,100]

# # try except 구문으로 예외를 처리합니다.

# try:
#     # 숫자를 입력받습니다.
#     number_input = int(input("정수입력>"))
#     # 리스트의 요소를 출력합니다.
#     print("{} 번쨰 요소: {}".format(number_input, list_number[number_input]))
# except Exception as exception:
#     # 예외 객체를 출력해봅니다.
#     print("type(exception):", type(exception))
#     print("exception:", exception)

#     # 정수 입력 > yes!! 를 했을때 
# # type(exception): <class 'ValueError'>
# # exception : invalid literal for int() with base 10: 'yes!!'

#--------------------------------------------------------------------------------------------------------

# # 변수를 선언합니다.
# list_number = [52,273,32,72,100]

# # try except 구문으로 예외를 처리합니다.
# try:
#     # 숫자를 입력받습니다.
#     number_input = int(input("정수 입력>"))
#     # 리스트의 요소를 출력합니다.
#     print("{}번째 요소:".format(number_input, list_number[number_input]))
# except ValueError as exception:
#     # VallueError가 발생하는 경우
#     print("정수를 입력해 주세요!")
# except IndexError:
#     # IndexError가 발생하는 경우
#     print("리스트의 인덱스를 벗어났어요!")

#--------------------------------------------------------------------------------------------------------

# # 변수를 선언합니다.

# list_number = [52,273,32,72,100]

# # try except 구문으로 예외를 처리합니다.

# try:
#     # 숫자를 입력 받습니다.
#     number_input = int(input("정수 입력> "))
#     # 리스트에 요소를 출력합니다.
#     print("{} 번쨰 요소 {}".format(number_input, list_number[number_input]))
# except ValueError as exception:
#     # ValueError가 발생하는 경우
#     print("정수를 입력해 주세요!")
#     print("exception:", exception)
# except IndexError as exception:
#     # IndexError가 발생하는 경우
#     print("리스트의 인덱스를 벗어났어요!")
#     print("exception:", exception)

#--------------------------------------------------------------------------------------------------------

# # 변수를 선언합니다.

# list_number = [52,273,32,72,100]

# # try except 구문으로 예외를 처리합니다.

# try:
#     # 숫자를 입력 받습니다.
#     number_input = int(input("정수 입력> "))
#     # 리스트의 요소를 출력합니다.
#     print("{}번째 요소:{}".format(number_input, list_number[number_input]))
#     예외.발생해주세요()

# except ValueError as exception:
#     #valueError 가 발생하는 경우
#     print("정수를 입력해 주세요!")
#     print(type(exception), exception)
# except IndexError as exception:
#     # 이외의 예외가 발생한 경우
#     print("미리 파악하지 못한 예외가 발생했습니다.")
#     print(type(exception), exception)

# # 정수입력 > 1 
# # 1번째 요소 : 273
# # 미리 파악하지 못한 예외가 발생하였습니다.
# # <class 'nameError'> name '예외' is not defined

#--------------------------------------------------------------------------------------------------------

# 입력을 받습니다.

number = input("정수입력 > ")
number = int(number)

# 조건문 사용

if number > 0:
    # 양수일 때 : 아직 미구현 상태입니다.
    raise NotImplementedError

else:
    # 음수일 때 : 아직 미구현 상태입니다.
    raise NotImplementedError

#--------------------------------------------------------------------------------------------------------

