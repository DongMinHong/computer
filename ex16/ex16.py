#-*-coding:utf-8

#-*-coding:cp949
from sys import argv


#위에서 open() 의 역할은
#* filename 변수 안에 저장된 문자열과 같은 이름을 가진 어떤 파일과
#* 위 프로그램 안의 target을 연결 시켜 주는 것입니다.
#* target.read() 하면 그 파일의 내용을 읽으려고 할 것이고
#* target.write(content) 하면 그 파일에 content 라는 변수에 저장된 문자열을 쓰려고 할 것입니다.

#target.truncate() 는 target 으로 연결된 파일의 내용을 모두 지우는 기능을 할 것입니다.

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')
# 여기서 w의 역할은 파이참에서 열어서 사용을 함으로써 다른곳에서 수정을 방지할수 있다.
print "Truncating the file.  Goodbye!"
target.truncate()
# truncate는 열려있는 파일의 내용을 다 삭제
print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
# 파일을 출력으로만 사용하고있다.

print "And finally, we close it."
