#프로그래머스 - [3차] 파일명 정렬

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]

def split_data(index,files):
    left , right  = 0 , len(files)
    for idx,file in enumerate(files) :
        if file.isnumeric() :
            left = idx
            break
    
    for idx,file in enumerate(files[left:]) :
        if not file.isnumeric() :
            right = idx+left
            break

    return (files , files[:left].upper() , int(files[left:right]) , index )

def solution(files):
    files = sorted( [split_data(idx,file) for idx,file in enumerate(files)] , key=lambda x:(x[1],x[2],x[3]))
    return [file[0] for file in files]

print( solution(files) )