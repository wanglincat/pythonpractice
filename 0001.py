import random

def jihuoma(length):
	s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
	return "".join(random.sample(s,length))
l=input("�����뼤����ĳ��ȣ� ")
print(jihuoma(int(l)))