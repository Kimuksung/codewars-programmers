from collections import defaultdict

def solution(genres, plays):
    answer = []
    # Init
    music = defaultdict(list)
    for idx,play in enumerate(plays) :
        music[genres[idx]].append( (play,idx) )
    
    # 많이 재생된 장르
    data = sorted( music.items() , key=lambda x: (-sum( list( map( lambda x:x[0] , x[1]) ) ) , x[0]) )

    # 장르 내에서 많이 재생된 노래 수록
    for temp in data:
        for t in sorted(temp[1] , key=lambda x:(-x[0],x[1]))[:2]:
            answer.append(t[1])
            
    return answer