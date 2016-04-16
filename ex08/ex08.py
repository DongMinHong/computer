#-*-coding:cp949
formatter = "%r %r %r %r"
here = 1
we = 3
are= 4

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", 'four')
#위의 결과에서 "" 나 ''은 결과값이 같다
print formatter % (True, False, False, True)
# True False 는 따로 변수 지정 해줄 필요 없다
print formatter % (formatter, formatter, formatter, formatter)
#변수 지정을 해주면 위처럼 알아서 해준다
print formatter % (here, we, are, we)
#here나 we , are은 따로 변수지정 해줘야한다.
print formatter % ("I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight.")