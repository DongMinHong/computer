#-*-coding:utf-8

#-*-coding:cp949

# 위의 코드는 backslash 와 code page 문제로 충돌이 있을때 해결해줌
#-*-coding:cp949는 한글 나타내줄때 쓰임
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

print' %\ '
print" % \\"
#\을 나타내기위해 \\ 와 같이 두번 써준다 %를 나타내기위해 %%로 나타내는것과 같다

#age에 대고 crtl+b를 누르면 처음의 age 자리로 간다

#백슬래시\:서로 다른숫자가아닌 연관된숫자임을 알려줌

#탭 문자 ('\t') 와 공백(' ') 사이의 차이점에 대해 잘 생각해 보기 바랍니다.
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
    print """
#\n은 한줄 띄는것을 의미하고 \t는 4칸 띄기를 의마함
#space 4칸은 \t와 의미각 같다고 볼수있으나 space 는 드래그가 되고
# \t는 한꺼번에 드래그가 된다
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat