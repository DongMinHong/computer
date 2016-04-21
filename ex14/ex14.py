#-*-coding:utf-8

#-*-coding:cp949
# 우션 edit configuration 들어가서 변수 입력해주고
#그래도 안나오면 help-find action 들어가서 project encoding 들어가서 utf-8 을 windows 949로 바꿔주면 된다
from sys import argv

script, user_name = argv
prompt = '> '
# prompt 를  '' 사이에 < 나타나주면 밑에< 이 온다
# script는 파일이 있는 위치
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)
#raw_input이 안될경우 input을 사용해본다
#likes의 값을 raw_input 을 이용해 사용자에게 물으면서 동시에 변수지정
print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print"What is your favorite hobby %s?" %user_name ,
hobby = raw_input(prompt)
# ,의 기능은 바로 옆에서 나타내주는것을 잊지말고 만약에 user_name 뒤에 hobby= raw_input(prompt)로 해버리면
# %에 hobby 가 걸리기에 다음칸에 써줘야 한다
print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.
And your favorite hobby is %r. Thank you!.
""" % (likes, lives, computer, hobby)

# %s 로 해봐서 위와의 차이점을 비교

print """
Alright, so you said %s about liking me.
You live in %s.  Not sure where that is.
And you have a %s computer.
And your favorite hobby is %s. Thank you!.
""" % (likes, lives, computer, hobby)
# %r은 무조건 작음따옴표로 나옴 (숫자 빼고)

good = "dog"
print "I give you %r. " % good

print"Who are you? %s."  % "likes"
print"Who are you? %r."  % "동민"
print"Who are you? %s."  % "ab"

# %s %r에서 뒤에 ""로 한글을 바로 받을떄는 둘다 아뇌지만 %s 는 변수를 문자열로 바꾸는 기능이 있어서
# 변수를 한글로지정하고나서 그 변수를 %값으로 쓰면 출력이 가능하다. 이는 위에 두 프린트 예에서 알수 있다.
# 위의 두 프린트에서 볼수 있듯이 %r 은 한글 값을 못받는다. %s 는 문자열로 바꾸는 기능으로 받아줄수 있다.