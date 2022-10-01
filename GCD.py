a, b = input().split()
a, b = int(a), int(b)
	
def gcd_sub(a, b):
	while a*b!=0:
		if a>b:
			a-=b
		else:
			b-=a
	return a+b

def gcd_mod(a, b):
	while a*b!=0:
		if a>b:
			a%=b
		else:
			b%=a
	return a+b
	
def gcd_rec(a, b):
	if a*b==0:
		return a+b
	if a>b:
		return gcd_rec(b, a%b)
	else:
		return gcd_rec(a, b%a)
	
x = gcd_sub(a, b)
y = gcd_mod(a, b)
z = gcd_rec(a, b)

print(x, y, z)
