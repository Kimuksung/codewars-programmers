# Decorator
def decorator1(func):
    def wrapper():
        print('decorator1')
        func()
    return wrapper
 
def decorator2(func):
    def wrapper():
        print('decorator2')
        func()
    return wrapper

@decorator1
@decorator2
def hello():
    print('hello')

hello()
#decorated_hello = decorator1(decorator2(hello))
#decorated_hello()

# 1.1. Extending the function with a decorator
def decorator_list(fnc):
    def inner(list_of_tuples):
        return [fnc(val[0],val[1]) for val in list_of_tuples]
    return inner

@decorator_list    
def add_together(x,y):
    return x+y

print(add_together([(1, 3), (3, 17), (5, 5), (6, 7)]))


# 1-2. Decorators that can take arguments themselves

def meta_decorator(power):
    def decorator_list(fnc):
        def inner(list_of_tuples):
            return [fnc(val[0],val[1])**power for val in list_of_tuples]
        return inner
    
    return decorator_list

@meta_decorator(3)    
def add_together(x,y):
    return x+y

print(add_together([(1, 3), (3, 17), (5, 5), (6, 7)]))    

# 1-3. Default arguments in Decorators
def meta_decorator(arg):
    def decorator_list(fnc):
        def inner(list_of_tuples):
            return [fnc(val[0],val[1])**power for val in list_of_tuples]
        return inner

    if callable(arg):
        power=2
        return decorator_list(arg)
    else :
        power=arg
        return decorator_list

@meta_decorator
def add_together(x,y):
    return x+y

# @meta_decorator(3)
#def add_together(x,y):
#    return x+y

print(add_together([(1, 3), (3, 17), (5, 5), (6, 7)]))    
