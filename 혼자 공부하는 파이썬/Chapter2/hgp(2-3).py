pi = 3.14159265
# print(pi)

print(pi+2)
print(pi-2)
print(pi*2)
print(pi/2)
print(pi%2)
print(pi*pi)

# 변수 선언과 할당
pi = 3.14159265
r=10

# 변수 참조
print("원주율 = " , pi)
print("반지름 =" , r)
print("원의 둘레 =" , 2*pi*r)
print("원의 넓이 =" , pi*r*r)

number = 100
number += 10
number += 20
number += 30
print("number :" , number)

string = "안녕하세요"
string += "!"
string += "!"
print("string :" , string)

input("인사말을 입력하세요>")
string = input("인사말을 입력하세요>")
print(string)

print(type(string))

number = input("숫자를 입력하세요>")
print(number)
print(type(number))
#----------------------------------------------------------------------------------------------------

# 입력을 받습니다.
string = input("입력>")

#출력합니다.
print("자료", string)
print("자료형", type(string))

#-------------------------------------------------------------------------------------------------------

string_a = input("입력A> ")
int_a = int(string_a)

string_b = input("입력B> ")
int_b = int(string_b)

print("문자열 자료" , string_a + string_b)
print("숫자 자료" , int_a + int_b)

#--------------------------------------------------------------------------------------------------------

output_a = int("52")
output_b = float("52.273")

print(type(output_a) , output_a)
print(type(output_b) , output_b)

#--------------------------------------------------------------------------------------------------------

input_a = float(input("첫 번째 숫자>"))
input_b = float(input("두 번째 숫자>"))

print("덧셈 결과" , input_a + input_b)
print("뺄셈 결과" , input_a - input_b)
print("곱셈 결과" , input_a * input_b)
print("나눗셈 결과" , input_a / input_b)

#--------------------------------------------------------------------------------------------------------

int("523")

print(int)

#--------------------------------------------------------------------------------------------------------

output_a = str(52)
output_b = str(52.273)
print(type(output_a) , output_a)
print(type(output_b) , output_b)

# The End