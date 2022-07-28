# Python Call by Object reference
# Call by sharing
# immutable object is 

# immutable object
# For immutable objects, there is no real difference between call by sharing and call by value
a = 1

def immutable_object_test(num):
    print( 'before allocated : {} '.format(id(num)) )
    num = 10
    print( 'after allocated : {} '.format(id(num)) )

print( 'a : {}'.format(id(a)))
immutable_object_test(a)
print( 'result : {}'.format(a))
print('-'*10)

# mutable object
# if the objects are mutable, within the function are visible to the caller, which may appear to differ from call by value semantics.
# Mutations of a mutable object within the function are visible to the caller because the object is not copied or cloned—it is shared.
a = [1,2,3,4]
def mutable_object_test( temp ):
    print( 'before allocated : {} '.format(id(temp)) )
    temp.append(5)
    print( 'after allocated : {} '.format(id(temp)) )

print( 'a : {}'.format(id(a)))
mutable_object_test( a )
print( 'result : {}'.format(a))