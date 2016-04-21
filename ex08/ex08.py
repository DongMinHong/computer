#-*-coding:cp949
formatter = "%r %r %r %r"
here = 1
we = 3
are= 4

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", 'four')
#one, two, three, four는 변수지정이 안되잇으므로 "" 를 사용해야한다
#위의 결과에서 "" 나 ''은 결과값이 같다
print formatter % (True, False, False, True)
# True False 는 따로 변수 지정 해줄 필요 없다
print formatter % (formatter, formatter, formatter, formatter)
# %r 로 해줘서 위에서 formatter 를 "%r %r %r %r" 로 해주 었지만 '%r %r %r %r'로 나온다
#변수 지정을 해주면 위처럼 알아서 해준다
print formatter % (here, we, are, we)
#here나 we , are은 따로 변수지정 해줘야한다.
print formatter % ("I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    'So I said goodnight.')
# 2번졎와 4번졎를 보면 알수 있듯이 ""로 하나 ''로 하나 답은 같다.
# 여기서 %r 로 지정을 해주었으니 답은 무조건''로 나온다 허나 But it din't sing 은 중간에 ' 가 들어갔으므로
# "" 으로 나온다. ""사이에 ' 올수 있고 ''사이에 "" 올수 있는것과 같은것
