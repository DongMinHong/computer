#-*-coding:utf-8

#-*-coding:cp949

from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third


#파이썬 3시리즈부터 괄호가 필요
#ex13:from sys import argv
#sys라는 모듈에서 argv라는 것을 쓰겟다
#git bash(터미널)에서 pydoc file - 1ess 를 치면 file 에 대한 정보가 나옴
#ex13에서
#cd
#bash shell (SourceTree 에서 Terminal 을 누르면 나오는 검은 화면) 에서는 어떤 폴더가 "작업 대상 경로"로 선택 됩니다.
#cd 는 작업 대상 경로를 다른 폴더로 바꾸는 역할을 합니다.
#ls
#다른 매개 변수 없이 ls 만 입력하면 현재의 작업 경로 안의 파일과 폴더 목록을 (축약된 형태로) 보여 줍니다.
#terminal에서
#pwd는 현재 작업중인 파일 위치
#cd ex13을하면작업위치가 ex13으로 바뀜
#ls 를 치면 ex13.py가 있구나 하고 암

# 첫번째 방법: edit configuration 가서 script parameters 에 a b c 대입
# 두번째 방법: 터미널에서 cd d:\F BCD\ex13 치고 엔터 누르고
# python ex13.py a b c 치면 됨