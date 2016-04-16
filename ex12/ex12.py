#-*-coding:utf-8

#-*-coding:cp949
age_old = raw_input("How old are you?")
height_cm = raw_input("How tall are you?")
weight_kg = raw_input("How much do you weigh?")
#age에 대고 crtl+b를 누르면 처음의 age 자리로 간다
print "So, you're %r old, %r tall and %r heavy." % (age_old, height_cm, weight_kg)