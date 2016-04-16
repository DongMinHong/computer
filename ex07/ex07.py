#-*-coding:cp949
#ex07 저장소에 error_note.txt 파일을 만들어서 실수를 했을 때 마다 적어 두고 그 다음 예제 시작 전에  한번씩 읽어 보기 바랍니다.

#python 3 인 경우 마지막에서 두번째는 예를 들어
#print(end1 + end2, end=' ')
#과 비슷하게 할 수 있을 것입니다.
print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "Lee Tae Hoon is sneezing as of %s." % "photo"
# %뒤에 문자열을 입력해줄때 만약 변수 지정을 안해줬다면 옆처럼 '' 사이에 넣어줘도됨 ""사이에 넣어줘도 된다
print "And everywhere that Mary went."
print "." * 10  # what'd that do?
#위처럼 문장을 곱해줄수도 있다. # 예를 들어보자
print "LEE is idle" * 10

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"


# watch that comma at the end.  try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12
# 여기서 ,의 역할은 밑의 print 문과 이어주는 역할이다
print end1 + end2 + end3 + end4 + end5 + end6
print end7 + end8 + end9 + end10 + end11 + end12
#위처럼 변수지정된 문자는 그냥 "" 없이 바로 출력이 가능하다
# ,의 역할에 대해 다시 알아보자
print "Why we should take notes when listning",
print "programming ?"
print "Because it is very important to study programmin"

