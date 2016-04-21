
#-*-coding:utf-8

#-*-coding:cp949

# 위의 코드는 backslash 와 code page 문제로 충돌이 있을때 해결해줌
# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun" #변수지정, #문자 변수지정할떄는 ""를 사용해야함
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

#\n은 다음줄로 뛰어쓰는것을 말함

print "Here are the days: ", days
print "Here are the months: ", months

#앞서 말한거와 같이 print 뒤에 , days 는 print days 를 연달아 입력하라는 것으로 days 는 변수 지정 되있으니
#바로 저런식으로 입력한다

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
print'''
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
'''
# \t 와 스페이스 4칸은 보이는 건 같으나 드래그가 되는게 다르다
# \n은 다음줄로 바꿔서 나타낼수 있다.
# 허나 문장이 지저분해 보일수 있으므로  연속된 작은따옴표 3개(''') 또는 큰따옴표 3개(""") 이용 이 방법으로도 뛰어쓰기가
# 가능하다
print " Hi my name is dongmin \n i'm majoring in mechanical engineereing \n It is very hard \t but i'm verry happy"


