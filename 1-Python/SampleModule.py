def sayHello(text: str) -> str:
    '''
    This says hello
    '''
    return f"Hello, {text} from a Module!"

assert sayHello("x") == "Hello, x from a Module!"