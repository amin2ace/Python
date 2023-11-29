
def write_file(_path:str):
    """Create and write or overwire to file

    Args:
        _path (str): path and name of file
        mode (str): opening file mode 'a', 'w',....
    """    
    def inner(func:str):
        def wrapper(*args, **kwargs) -> str:
            with open(_path, 'a') as f:
                f.write(func(*args, **kwargs))
            return func(*args, **kwargs)
        return wrapper
    return inner

@write_file('D:/Python/Projects/Codes/dfd.txt')
def ps():
    return(f'afwekj')