import random

def jihuoma(length):
	s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
	return "".join(random.sample(s,length))
l=input("请输入激活码的长度： ")
print(jihuoma(int(l)))