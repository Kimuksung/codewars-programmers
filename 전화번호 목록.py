phoneBook = ["12","123","1235","567","88" , '1234']
print ( phoneBook[1:] )
print ( list ( zip ( phoneBook , phoneBook[1:])) ) 
print (sorted(phoneBook))
for p1, p2 in zip(phoneBook, phoneBook[1:]):
    print ( p1 , p2 )