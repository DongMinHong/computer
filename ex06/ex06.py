#-*-coding:cp949
# 이 코드는 주석에서 오류가 걸릴때 다 해결해준다
# # coding=utf-8
x = "There are %d types of people." % 10
u = "Theare are 20 musician."
print u
#위처럼 굳이 %d 해서 뒤에 %10으로 d의값을 나타내지않고 그냥 써줘도되는것을 알아두자
# 위에서 "" 를 사용해도 되고 ''를 사용해도 된다
# 기본적으로 문자열이나 문자를 변수지정후 사용할때 무조건 ""나 ''를 사용해야한다.
# 숫자를 지정해줄때는 ""나 ''를 사용하지 않아도 된다
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
#위처럼 문장과 문자을 변수 지정 가능하다.
brother= "brother"
z = "Mr.Lee is not human but devil's %s." % brother
# %d 는 숫자를 나타내줄욚 쓰이는데 위처럼 숫자는 바로 써줘도 되지만 %s는 문자열을 나타내주는데 이때는 나타내주고싶은
# 문자열을 위처럼 지정해준다
print x
print y
print z

print "I said: %r." % x #print "I said %s." % (repr(x)) 과 같은 의미
print "I also said: '%s'." % y
print "I said: '%r' " % x
print 'I said:  "%r" ' % x
#r과 s의 차이점을 보면 r로 해주면 ''가 붙고 s가 붙으면 따로 ''를 해줘야한다 .
# 그러나 숫자 %d를 대신해줄때는 ''가 붙지 않는다
print "shut up %r" % 20
#여기서 재미있는 것은 %s 포맷 코드인데, 이 코드는 어떤 형태의 값이든 변환해 넣을 수 있다. 무슨 말인지 예를 통해 확인해 보자.

#>>> "I have %s apples" % 3
#'I have 3 apples'
#>>> "rate is %s" % 3.234
#'rate is 3.234'
#3을 문자열 안에 삽입하려면 %d를 사용하고, 3.234를 삽입하려면 %f를 사용해야 한다.
#하지만 %s를 사용하면 이런 것을 생각하지 않아도 된다. 왜냐하면 %s는 자동으로 % 뒤에 있는 값을 문자열로 바꾸기 때문이다.




hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
# 변수끼리 합이 가능하다

g = "you are Lee"
h = "gang eun"

print g + h