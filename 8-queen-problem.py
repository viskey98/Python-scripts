# This is the solution to the problem of placing 8 queens on a chessboard such that no queen attacks the other
rd = [0]*15
ld = [0]*15
r = [0]*8
pos = [0]*8

def backtrack(j):
	if(j == 8):
		return True
	else:
		for i in range(8):
			if r[i]!=1 and ld[7+i-j]!=1 and rd[i+j]!=1:
				r[i] = 1
				ld[7+i-j] = 1
				rd[i+j] = 1
				if backtrack(j+1):
					pos[j] =  i+1
					return True
				r[i] = 0
				ld[7+i-j] = 0
				rd[i+j] = 0
	return False

if __name__ == '__main__':
	backtrack(0);
	print('The order of placing the 8-queens is (1-index):')
	for it in range(8):
		print(pos[it])
	
