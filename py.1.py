name=input("Enter student name:")
n=int(input("Enter number of subjects:"))
total=0
for i in range(1,n+1):
    mark=float(input(f"Enter mark for subject{i}:"))
    total+=mark
percentage=total/n
if percentage>=90:
    grade="A+"
    perfomance="outstanding"
elif percentage>=80:
    grade="A"
    perfomance="excellent"
elif percentage>=70:
    grade="B"
    perfomance="very good"
elif percentage>=60:
    grade="C"
    perfomance="good"
elif percentage>=50:
    grade="D"
    perfomance="average"
else:
    grade="F"
    perfomance="needs improvement"
print("\n---academic performance---")
print("student name:",name)
print("total marks:",total)
print("percentage:",round(percentage,2),"%")
print("grade:",grade)
print("perfomance:",perfomance)
