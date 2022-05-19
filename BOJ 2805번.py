#BOJ 2805번

len_tree , need_tree = map(int,input().split())
trees = list(map(int,input().split()))

left , right = 0 , max(trees)

while left < right :
    middle = (left+right)//2+1
    if sum( [ tree-middle if tree-middle > 0 else 0 for tree in trees] ) >= need_tree :
        left = middle
    else :
        right = middle-1
        
print(left)