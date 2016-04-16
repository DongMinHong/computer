#-*-coding:utf-8

#-*-coding:cp949

#  ex17 하는법은 2개가 있는데 첫번째는 소스트리 terminal 에서 명령어로 text.txt와 new_file.txt를 만들어서 가동시키는방법과
#  그냥 파이썬에서 text.txt 와 new_file.txt를 각각 from_file , to_file 로 변수지정해서 하는법이 있다.

# 소스트리에서 명령어로 text.txt를 지정하는방법   echo "this is a test file." >text.txt
# 소스트리에서 명령어로 new_file.txt를 지정하는방법 python ex17.py text.txt new_file.txt
# 이처럼 하면 자동적으로 txt 파일이 2개 만들어진다.

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#text,txt가 from_file에 해당 new_file.txt가 to_file에 해당

# we could do these two on one line, how?
in_file = open(from_file) #form_file 을 열고 그걸 임의의 변수 in_file로 지정해주었다.
indata = in_file.read() #in_file을 읽는것을 변수 indata에 지정하였다.

x = "don'tt"
print"don't is %d bytes long" % len(x)

print "The input file is %d bytes long" % len(indata)
#여기서 len 은 글자수를 말해준다.
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w') #to_file을 열고 write 모드로 사용하면 그것을 변수 out_file에 넣어준다
out_file.write(indata) #out_file에 indata 즉 infile 을 읽은값을 써준다 (from_file에서 to_file로 내용을 복사하는것)

print "Alright, all done."

out_file.close()
in_file.close()
#파일을 열었으니 닫아주는것
#처음 run때는 Does the outpu file exsit? 에서 false 가 나올것이지만 두번째 부터는 true가 나온다 이유는
# run을통해 to_file이 생성되고 값이 한번 입력 되니까 이제부터는 to_file이 계속 존재하기 때문이다.