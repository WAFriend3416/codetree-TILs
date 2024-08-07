class Student:
    def __init__(self, h, w,number):
        self.h = h
        self.w = w
        self.number = number

n = int(input())
Students = []

for i in range(1,n+1):
    h,w = map(int,input().split())
    student = Student(h,w,i)
    Students.append(student)

Students.sort(key=lambda x : (-x.h,-x.w,x.number))


# 정렬 이후 등수별 학생 번호 출력
for student in Students:
    print(student.h,student.w,student.number)