#-*-coding:utf-8

#-*-coding:cp949

print 5.000 % 3.001
my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'
#변수 값을 지정할때 숫자는 바로 해줘도 되지만 문자는 '' 사이에 넣어줘야한다.
# %s(string)=문자열(데이터를 문자열로 바까주는 변수) %d=정수, %f(float)=숫자열(숫자가 실수로 나오게 하는 변수)
# %c=문자 1개 %g=실수 #int=정수(숫자가 정수로 나오게 해주는 변수)
print "Let's talk about %s." % my_name
print "He's %s inches tall." % my_height # 보다시피 s 는 데이터 즉 74 를 문자열로 바꿔주니까 s로 사용할수 있다
print "He's %d inches tall." % my_height
print "He's %r pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)

print "My favorite number is %d" % (my_age + my_height + my_weight)
# 위처럼 여러개 더하는 수를 한번에 나타낼때는 괄호를 사용한다.