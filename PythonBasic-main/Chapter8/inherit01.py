# 부모 클래스 선언

class Parent:
    def __init__(self):
        self.value = "테스트"
        print("Parent 클래스의 __init()__ 메소드가 호출되었습니다.")
    def test(self):
        print("Parent 클래스의 test() 메소드입니다.")

# 자식 클래스를 선언

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print("Child 클래스의 __init()__ 메소드가 호출되었습니다.")

# 자식 클래스의 인스턴스를 생성하고 부모의 메소드 호출

child = Child()
child.test()
print(child.value)
