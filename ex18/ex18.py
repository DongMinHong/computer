# this one is like your scripts with argv
#def 는 함수를 나타냄
#들여쓰기로 함수의 시작과 끝을 나타낼수있다.
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
#step into는 함수 안으로 들어가 세세히하나하나 다 실행한다
#step over는 함수를 건너 띈다
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one arg`ument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
    print "I got nothin'."


print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

#질의응답해보기