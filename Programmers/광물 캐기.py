def mineral_result(pick, minerals):
    maps = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
    answer = 0
    for mineral in minerals:
        if mineral == "diamond":
            material = 0
        elif mineral == "iron":
            material = 1
        else:
            material = 2
        answer += maps[pick][material]
    return answer

def solution(picks, minerals):
    #backtracking
    target = min(len(list(range(0, len(minerals), 5))),sum(picks))
    answer = []
    min_value = 0
    
    def backtracking(n):
        nonlocal target
        nonlocal min_value
        if n == target:
            answer.append(min_value)
            return

        for i in range(3):
            if picks[i] > 0:
                picks[i] -= 1

                temp = mineral_result(i, minerals[n * 5:(n + 1) * 5])
                min_value += temp
                backtracking(n + 1)
                min_value -= temp
                picks[i] += 1

    backtracking(0)
    return min(answer)