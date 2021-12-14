class Person:
    pass
class Bird:
    pass

# 상속
class Student(Person):
    pass

# 인스턴스 생성
p, s = Person(), Student()

print("p is instance of Person: ", isinstance(p, Person))
print("s is instance of Person: ", isinstance(s, Person))   # 상속받았기 때문에 True
print("p is instance of Object: ", isinstance(p, object))
print("p is instance of Bird: ", isinstance(p, Bird))
print("int is instance of Object: ", isinstance(int, object))