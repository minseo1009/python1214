# ifelse.py
score = int(input("점수를 입력:"))

if 90 <= score <= 100:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
else:
    grade = "D"

print("등급은 ", grade)


for x in list(range(2,10)):
    print("---- {0}단 ----".format(x))
    for y in list(range(1,10)):
        print("{0} * {1} = {2}".format(x,y,x*y))


