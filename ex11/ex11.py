#-*-coding:utf-8

#-*-coding:cp949
print "How old are you?",
age_old = raw_input()
print "How tall are you?",
height_cm = raw_input()
print "How much do you weigh?",
weight_kg = raw_input()
#물리량에 단위를 꼭 표시하자
#raw_input() 은 사용자로부터 입력값을 받는 함수이다 print의 일종
print"what is your favorite number?",
number = raw_input()

print "So, you're %r old, %r tall, %r heavy and %r number" % (
    age_old, height_cm, weight_kg, number)