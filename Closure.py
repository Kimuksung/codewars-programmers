
def nested_func(text):
    temp = text
    def test2():
        print( 'temp : {}'.format(temp))

    return test2()

# free_variable is non-local variable
nested_func('test')

def closure(text):
    text = text
    def test():
        print( 'free variable : {}'.format(text))

    return test

a = closure('closure_test')
print(a)
#> <function closure.<locals>.test at 0x0000017E492D8700>
a()
#> free variable : closure_test

def logger(func):
    def log_func(*args):
        print(func(*args))
    return log_func

def risk_up(x,y):
        return x+y
def risk_down(x,y):
    return x-y

add_logger = logger(risk_up)
add_logger(3,3)
# > 6
sub_logger = logger(risk_down)
sub_logger(6,2)
# > 4