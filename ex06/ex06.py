#-*-coding:cp949
# # coding=utf-8�� �ڵ�� �ּ����� ������ �ɸ��� �� �ذ����ش�
x = "There are %d types of people." % 10
# ������ "" �� ����ص� �ǰ� ''�� ����ص� �ȴ�
# �⺻������ ���ڿ��̳� ���ڸ� ���������� ����Ҷ� ������ ""�� ''�� ����ؾ��Ѵ�.
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
#��ó�� ������ ���� ���� �����ϴ�.
brother= "brother"
z = "Mr.Lee is not human but devil's %s." % brother
# %d �� ���ڸ� ��Ÿ���ٞ� ���̴µ� ��ó�� ���ڴ� �ٷ� ���൵ ������ %s�� ���ڿ��� ��Ÿ���ִµ� �̶��� ��Ÿ���ְ����
# ���ڿ��� ��ó�� �������ش�
print x
print y
print z

print "I said: %r." % x #print "I said %s." % (repr(x)) �� ���� �ǹ�
print "I also said: '%s'." % y
#r�� s�� �������� ���� r�� ���ָ� ''�� �ٰ� s�� ������ ���� ''�� ������Ѵ� .
# �׷��� ���� %d�� ������ٶ��� ''�� ���� �ʴ´�
#���⼭ ����ִ� ���� %s ���� �ڵ��ε�, �� �ڵ�� � ������ ���̵� ��ȯ�� ���� �� �ִ�. ���� ������ ���� ���� Ȯ���� ����.

#>>> "I have %s apples" % 3
#'I have 3 apples'
#>>> "rate is %s" % 3.234
#'rate is 3.234'
#3�� ���ڿ� �ȿ� �����Ϸ��� %d�� ����ϰ�, 3.234�� �����Ϸ��� %f�� ����ؾ� �Ѵ�.
#������ %s�� ����ϸ� �̷� ���� �������� �ʾƵ� �ȴ�. �ֳ��ϸ� %s�� �ڵ����� % �ڿ� �ִ� ���� ���ڿ��� �ٲٱ� �����̴�.




hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
# �������� ���� �����ϴ�

g = "you are Lee"
h = "gang eun"

print g + h