class Student:
    def __init__(self,name,kor,eng,mat):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat
    

n = int(input())
Students = []


for _ in range(n):
    name,kor,eng,mat = map(str,input().split())
    student = Student(name,int(kor),int(eng),int(mat))
    Students.append(student)

Students.sort(lambda x:(-x.kor,-x.eng,-x.mat))

for student in Students:
    print(student.name,student.kor,student.eng,student.mat)