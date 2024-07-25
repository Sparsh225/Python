
def debug(func):
    def wrapper(*args, **kwargs):
        args_result=','.join(str(arg) for arg in args)
        kwargs_result=', '.join(f'{k}={v} ' for k , v in kwargs.items())
        if len(args_result)==0:
            args_result=0
        print(f'calling: {func.__name__} with args {args_result} and kwargs {kwargs_result}')
        return func(*args ,**kwargs)
    return wrapper


@debug
def greet(name , greeting="Hello"):
    print(f'{greeting} , {name}')

@debug
def hello():
    print('hellllo')

greet('hanji',greeting='hello')
hello()