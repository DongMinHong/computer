#-*-coding:cp949
formatter = "%r %r %r %r"
here = 1
we = 3
are= 4

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", 'four')
#���� ������� "" �� ''�� ������� ����
print formatter % (True, False, False, True)
# True False �� ���� ���� ���� ���� �ʿ� ����
print formatter % (formatter, formatter, formatter, formatter)
#���� ������ ���ָ� ��ó�� �˾Ƽ� ���ش�
print formatter % (here, we, are, we)
#here�� we , are�� ���� �������� ������Ѵ�.
print formatter % ("I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight.")