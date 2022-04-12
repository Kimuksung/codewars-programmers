# BOJ 10808번
datas = input()
alpha_list = [0] * 26

for data in datas :
    alpha_list[ord(data)-ord('a')] += 1

print ( *alpha_list )