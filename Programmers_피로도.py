#Programmers 피로도

# No greedy
# Simulation
from itertools import permutations

k = 80
dungeons= [[80,20],[50,40],[30,10]]
answer = 0

for case_dungeon in list(permutations(dungeons)) :
    temp_k = k
    temp_answer = 0

    for dungeon in case_dungeon :
        if dungeon[0] <= temp_k :
            temp_k -= dungeon[1]
            temp_answer += 1
        else :
            continue
    
    answer = max(answer,temp_answer)

print(answer)
