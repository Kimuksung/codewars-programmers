def change_str(datas):
    char_list = []
    for idx,data in enumerate(datas) :
        if data == '#':
            continue
        if idx < len(datas)-1 :
            if datas[idx+1] == '#' :
                char_list.append(''.join(datas[idx:idx+2]))
                continue
        char_list.append(data)
        
    return char_list , len(char_list)
    
def solution(m, musicinfos):
    answer = []
    m , n = change_str(m)

    for idx , musicinfo in enumerate(musicinfos) :
        musicinfo = musicinfo.split(',')
        target_music , target_music_len = change_str(list(musicinfo[3]))
        start_time = list(map(int,musicinfo[0].split(':')))
        end_time = list(map(int,musicinfo[1].split(':')))
        times = (end_time[0]*60+end_time[1]) - (start_time[0]*60+start_time[1] )
        
        #조건 1. 들은 음악보다 길어야한다.
        if times < n :
            continue
        
        #조건 2.음악 길이보다 재생된 시간이 짧을 때는 처음부터 재생 시간만큼만 재생된다.
        if times < target_music_len :
            target_music , target_music_len = target_music[:times] , times
            
        times=times*2
        temp_data = []
        for time in range(times) :
            temp_data.append(target_music[time%target_music_len])
        
        for i in range(times-n):
            if m==temp_data[i:i+n] :
                answer.append((musicinfo[2],times//2,idx))
                break
                
    answer = sorted(answer,key=lambda x:(-x[1],[2]))                

    if answer :
        return answer[0][0]
    else :
        return "(None)"