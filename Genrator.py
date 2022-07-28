# Genrator
def test_generator() :
    yield 1
    yield 2
    yield 3

test = test_generator()
print(test)

print( next(test) )
print( next(test) )
print( next(test) )
print('-'*10)

import time
def sleep_func(num) :
    print('sleep')
    time.sleep(1)

    return num

# test list_comprehension
list = [sleep_func(i) for i in range(5)]
for i in list:
    print(i)

print('-'*10)
# test generator_comprehension
gen = (sleep_func(i) for i in range(5))
for i in gen:
    print(i)