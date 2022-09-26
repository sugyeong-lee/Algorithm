import time, random

def compute_e_ver1(n):
	# code for O(n^2)-time version
	e, f = 1, 1
	for i in range(1, n+1):
		for k in range(1, i+1):
			f *= k
		e += 1/f
		f = 1
	return e
	
def compute_e_ver2(n):
	# code for O(n)-time version
	e, f = 1, 1
	for k in range(1, n+1):
		f *= k
		e += 1/f
	return e

n= int(input())
k1 = compute_e_ver1(n)
k2 = compute_e_ver2(n)
print("오일러 수(O(n^2), O(n)) : ", k1, k2)

# # 두 함수의 수행시간 출력
before1 = time.process_time()
# compute_e_ver1 호출
compute_e_ver1(n)
after1 = time.process_time()
print("O(n^2) :", after1-before1)

before2 = time.process_time()
# compute_e_ver2 호출
compute_e_ver2(n)
after2 = time.process_time()
print("O(n) :", after2-before2)
