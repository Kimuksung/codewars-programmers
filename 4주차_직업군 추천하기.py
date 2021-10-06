def solution(tables, languages, preference):
    answer = []
    '''
    lang_dict = dict()
    
    for lang , pref in zip (languages , preference) :
        lang_dict[lang] = pref
    '''
    lang_dict = dict( zip (languages , preference) )  
    
    for table in tables :

        dev = table.split( ' ')
        dev_pref = 0
        for idx , data in enumerate ( reversed(dev[1:]) ) :
            if data in lang_dict :
                dev_pref += lang_dict[data] * (idx + 1)
        answer.append( [dev[0] , dev_pref])   
    return sorted( answer , key = lambda x : ( -x[1] , x[0] ) )[0][0]

print ( 
    solution( ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"] 
    , ["JAVA", "JAVASCRIPT"]
    , [7, 5]
    )
)