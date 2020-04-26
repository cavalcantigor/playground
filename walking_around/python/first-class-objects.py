"""
    Functions are first-class objects. You can assign them to variables,
    store them in data structures, pass them as arguments to other functions,
    and even return them as values from other functions.

    https://dbader.org/blog/python-first-class-functions
"""


def yell(text: str):
    return text.upper() + "!"


def greet(func):
    """
        Greet receives func as parameter; this ability can abstract behavior
        in your programs. Differents greeting behaviors can be passed.
    """
    greeting = func('Hi, I am a Python program')
    return greeting


def whisper(text):
    return text.lower() + '...'


def speak(text):
    """
        Nested (or inner) functions can be defined inside other functions.
        inner_whisper does not exist outside speak.
    """
    def inner_whisper(t):
        return t.lower() + '...'
    return inner_whisper(text)


def get_speak_func(text, volume):
    """
        But if you want access inner_whisper outside speak? You can return
        inner functions to the caller on the parent function.
    """
    def inner_whisper():
        return text.lower() + '...'

    def inner_yell():
        return text.upper() + '!'

    if volume > 0.5:
        return inner_yell
    else:
        return inner_whisper


def make_adder(n):
    """
        A closure remembers the values from its enclosing lexical scope
        even when the program flow is no longer in that scope.
    """
    def add(x):
        return x + n
    return add


class Adder:
    """
        Objects can be called.
    """
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return self.n + x


if __name__ == "__main__":
    print(yell('hello'))                        # HELLO!

    foo = yell
    print(foo('foo'))                           # FOO!

    del yell                                    # yell('hello') -> NameError
    print(foo('hello'))                         # HELLO!
    print(foo.__name__)                         # 'yell'

    funcs = [foo, str.lower, str.capitalize]
    for f in funcs:
        print(f('hi'))                          # HI! hi Hi

    print(funcs[0]('hello world'))              # HELLO WORLD!

    print(greet(foo))                           # HI, I AM A PYTHON PROGRAM!
    print(greet(whisper))                       # hi, i am a python program...
    print(list(map(foo, ['hello', 'hey'])))     # [HELLO!, HEY!]

    print(speak('Hello, World'))                # hello, world...

    print(get_speak_func('hello', 0.7)())       # HELLO!

    plus_3 = make_adder(3)
    print(plus_3(4))                            # 7
    print(plus_3(6))                            # 9

    adder = Adder(5)
    print(adder(5))                             # 10
