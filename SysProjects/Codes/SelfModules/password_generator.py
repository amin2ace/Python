from random import sample
from string import ascii_letters, punctuation


class PasswordGenerator:
    """Generates password like string in length of 'length'
       Attributes:
       length: int - determine string's length
       numeric: bool - if True includes numeric character in generated string. default is False
       punctuation: bool - if True includes punctuation character in generated string. default is False

    Returns:
        str: return str by __repr__
    """
    __ALPHABET: list[str] = [alpha for alpha in ascii_letters]
    __NUMERICS: list[str] = [str(num) for num in range(0, 10)]
    __PUNCTS: list[str] = [p for p in punctuation]

    def __init__(
        self,
        length: int,
        numeric: bool = False,
        punctuation: bool = False,
    ) -> None:
        self.length: int = length
        self._numeric: bool = numeric
        self._punctuation: bool = punctuation

    @property
    def ALPHABET(self):
        return f'{' '.join(self.__ALPHABET)}'
    @property
    def NUMERIC(self):
        return f'{' '.join(self.__NUMERICS)}'
    @property
    def PUNCTS(self):
        return f'{' '.join(self.__PUNCTS)}'
    def _generator(self) -> str:
        """generate string with sampling of alphanumeric and punctuation characters

        Returns:
            str
        """        
        p1 = ''.join(sample(self.__ALPHABET, len(self.__ALPHABET)))
        p2 = ''.join(sample(self.__NUMERICS, len(self.__NUMERICS)))
        p3 = ''.join(sample(self.__PUNCTS, len(self.__PUNCTS)) )
        assert self.length <= 90, ValueError('length must be lower than 90')
        match self._numeric, self._punctuation:
            case True, True:
                password = sample(p1 + p2 + p3, self.length)
            case True, False:
                password = sample(p1 + p2, self.length)
            case False, True:
                password = sample(p1 + p3, self.length)
            case _:
                password = sample(p1, self.length)

        result = "".join(password)
        return f"{result}"
    
    def __repr__(self) -> str:
        return self._generator()
    
a = PasswordGenerator(100, True, True)
# a.ALPHABET=['a','s']
print(a)