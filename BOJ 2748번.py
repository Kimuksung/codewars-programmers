#BOJ 2748번
n = int(input())
num_list = [0,1] + [0]*90

for i in range( 2,n+1) :
    num_list[i] = num_list[i-1] + num_list[i-2]

print ( num_list[n] )