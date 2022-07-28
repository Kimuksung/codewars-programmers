#First class Functions

# 1. Functions are Objects
def change_lower(text):
    return text.lower()

test = change_lower
print(test('HELLO World'))

# 2. Functions can be passed as arguements to other functions
def change_lower(text):
    return text.lower()

def change_upper(text):
    return text.upper()

def change_word(func,text):
    return func(text)

text = 'HELLO World'
print( change_word(change_lower,text) )
print( change_word(change_upper,text) )

# 3. Functions can return another functions
def logging(text):
    def log_message():
        print( 'log_msg : {}'.format(text))

    return log_message

log = logging('test')
print(log)
log()

def logging(risk):
    def wrap_msg(msg):
        print('{0}-{1} '.format(risk,msg))

    return wrap_msg

risk_4 = logging('4')
risk_4('404')
risk_4('400')
risk_2 = logging(2)
risk_2('200')