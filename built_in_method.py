class Complex:
    def __init__(self, real, image):
        self.real = real
        self.image = image

    def __str__(self):
        return str(self.real)+'+'+str(self.image)+'i'

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __le__(self, other):
        return self.age <= other.age

if __name__ == '__main__':
    c = Complex(3.2, 5.3)
    print(c)
    print('复数c={}'.format(c))

    stu1= Student('李晓明', 19)
    stu2 = Student('马红', 20)
    print(stu2 <= stu1)



# 3.2+5.3i
# 复数c=3.2+5.3i
# False
