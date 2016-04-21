#-*-coding:utf-8

#-*-coding:cp949
from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename # %r로 해줘서 '' 나온것을 잊지 말자
print txt.read()
#read는 읽어들이는것

print "Type the filename again:"
file_again = raw_input("> ")
#여기서 file_again의 변수값을 사용자에게 지정을 요구하고있으며
txt_again = open(file_again)
#위에서 보듯이 지정한 file_again 값을 여는것을 변수지정하고있다.
print txt_again.read()
#그리고 마지막으로 사용자에게 지정을 요구한 file_again 값을 열고 읽으라고 명령하고있다.