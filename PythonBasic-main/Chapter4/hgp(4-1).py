#--------------------------------------------------------------------------------------------------------

# array = [273, 32, 103, "문자열" , True , False]
# print(array)

#--------------------------------------------------------------------------------------------------------

# [1,2,3,4]

# ["안","녕","하","세","요"]

#--------------------------------------------------------------------------------------------------------

# list_a = [273, 32, 103, "문자열", True, False]

# print(list_a[0])

# print(list_a[1])

# print(list_a[2])

# print(list_a[1:3])

#--------------------------------------------------------------------------------------------------------

# list_a = [273, 32, 103, "문자열", True, False]

# list_a[0] = "변경"

# print(list_a)

#--------------------------------------------------------------------------------------------------------

# list_a = [273, 32, 103, "문자열", True, False]

# print(list_a[-1])

# print(list_a[-2])

# print(list_a[-3])

#--------------------------------------------------------------------------------------------------------

# list_a = [273, 32, 103, "문자열", True, False]

# print(list_a[3])

# print(list_a[3][0])

#--------------------------------------------------------------------------------------------------------

# list_a = [[1,2,3],[4,5,6],[7,8,9]]

# print(list_a[1])

# print(list_a[1][1])

#--------------------------------------------------------------------------------------------------------

# list_a = [273, 32, 103]

# print(list_a[3])

# # 0,1,2 가 list에 존재하는데 3은 존재하지 않기에 indexError가 발생한다.

#--------------------------------------------------------------------------------------------------------

# #리스트를 선언합니다.

# list_a = [1, 2, 3]
# list_b = [4, 5, 6]

# #출력합니다.

# print("# 테스트")

# print("list_a = ", list_a)
# print("list_b = ", list_b)

# print()

# #기본 연산자

# print("# 리스트 기본 연산자")
# print("list_a + list_b =", list_a + list_b)
# print("list * 3 =", list_a * 3)

# print()

# #함수

# print("# 길이 구하기")
# print("len(list_a) =", len(list_a))

#--------------------------------------------------------------------------------------------------------

# # 리스트를 선언합니다.

# list_a = [1,2,3]

# # 리스트 뒤에 요소 추가하기

# print("# 리스트 뒤에 요소 추가하기")

# list_a.append(4)
# list_a.append(5)

# print(list_a)

# print()

# #리스트 중간에 요소 추가하기

# print("# 리스트 중간에 요소 추가하기")
# list_a.insert(0,10)
# print(list_a)

#--------------------------------------------------------------------------------------------------------

# list_a = [1,2,3]
# list_a.extend([4,5,6])
# print(list_a)

#--------------------------------------------------------------------------------------------------------

# list_a = [1,2,3]
# list_b = [4,5,6]

# print(list_a + list_b)

#--------------------------------------------------------------------------------------------------------

# list_a = [1,2,3]
# list_b = [4,5,6]

# list_a.extend(list_b)

# print(list_a)
# print(list_b)

#--------------------------------------------------------------------------------------------------------

# list_a = [0,1,2,3,4,5]
# print("# 리스트의 요소 하나 제거하기")

# #제거 방법[1] - del

# del list_a[1]

# print("del list_a[1]: ", list_a)

# #제거 방법[2] - pop()

# list_a.pop(2)
# print("pop(2): ", list_a)

#--------------------------------------------------------------------------------------------------------

# list_b = [0,1,2,3,4,5,6]

# del list_b[3:6]

# print(list_b)

#--------------------------------------------------------------------------------------------------------

# list_c = [0,1,2,3,4,5,6]

# del list_c[:3]

# print(list_c)

#--------------------------------------------------------------------------------------------------------

# list_d = [0,1,2,3,4,5,6]

# del list_d[3:]

# print(list_d)

#--------------------------------------------------------------------------------------------------------

# list_c = [1,2,1,2]

# list_c.remove(2)

# print(list_c)

#--------------------------------------------------------------------------------------------------------

# list_d = [0,1,2,3,4,5]

# list_d.clear()

# print(list_d)

#--------------------------------------------------------------------------------------------------------

# list_a = [273, 32, 103, 57, 52]

# print(273 in list_a)

# print(99 not in list_a)

# print(100 not in list_a)

# print(52 not in list_a)

# print(not 273 in list_a)

#--------------------------------------------------------------------------------------------------------

# print("출력")
# print("출력")
# print("출력")
# print("출력")
# print("출력")

# for i in range(100):
#     print("출력")

#--------------------------------------------------------------------------------------------------------

#리스트를 선언합니다.

array = [273, 32, 103, 57, 52]

#리스트에 반복문을 적용합니다.

for element in array:
    #출력합니다.
    print(element)

for character in "안녕하세요":
    print("-", character)
    
#--------------------------------------------------------------------------------------------------------

for i in range(100):
    print("출력")