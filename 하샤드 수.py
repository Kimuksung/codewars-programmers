def solution(x):
    hasad = sum ( [ int(data) for data in str(x)] )
        
    if x % hasad != 0 :
        return False
    return True