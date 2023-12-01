r"""_summary_

Returns:
    _type_: _description_
"""

class CharactersCast:
    def __init__(self, string_: str) -> None:
        self.string = string_

    def count_all_chars(self) -> dict:
        """Counts all the characters and return dictionary"""
        chars_count: dict[str, int] = {
            ch: self.string.count(ch) for ch in sorted(self.string)
        }
        return chars_count

    def count_char(self, *chars: str) -> dict:
        """Counts specific charachters and return number"""
        chars_count: dict[str, int] = {ch: self.string.count(ch) for ch in chars}
        return chars_count

    def compress(self) -> str:
        chars_count: dict[str, int] = self.count_all_chars()
        result: str = "".join([str(j) + i for i, j in chars_count.items()])
        return f"{result}"

    def decompress(self) -> str:
        chars: list[str] = list()
        counts: list[int] = list()
        for i in self.string:
            counts.append(int(i)) if i.isdigit() else chars.append(i)
        decom = map(lambda n, c: n * c, chars, counts)
        result = "".join(list(decom))
        return result


class Replace_:
    def __init__(self, string_: str, find_ch: str, replace_ch: str) -> None:
        self.string, self.find, self.replace = string_, find_ch, replace_ch

    ### Find and Replace specific characters
    def __str__(self):
        return self.string.replace(self.find, self.replace)


class PlainDrome_:
    """1.Reverse *arg as a list or **args as a dict just one in a time

    2. if last digit was zero it will ignore it

    3. kargs just will donw by reversing key and value indexes

    4. pass sentences as string, returns reverse"""

    def __init__(self, *arg, **kargs):
        self.original: list | dict = list(arg) if arg else kargs

    ### Reverse the original message
    def invoke(self) -> list | dict:
        if isinstance(self.original, dict):
            keys = list(self.original.keys())[::-1]
            values = list(self.original.values())
            list_result: dict = {
                i: [j for j in values[::-1]][k] for k, i in enumerate(keys)
            }
        else:
            for index in range(len(self.original)):
                arg = self.original[index]
                if isinstance(arg, str):
                    result = arg[::-1]
                if isinstance(arg, float):
                    result = str(arg)[::-1]
                    result = float(result)
                if isinstance(arg, int):
                    result = str(arg)[::-1]
                    result = int(result)
                self.original[index] = result
            list_result = self.original[::-1]

        return list_result


class IsInList_:
    """Return true if at list one char appears in string"""

    def __init__(self, list_of_strings, char) -> None:
        self.list, self.char = list_of_strings, char

    def __str__(self):
        a = map(lambda y: self.char in y[0], self.list)
        return f"{any(a)}"


class Swap_:
    """Swap first and second variables"""

    def __init__(self, first: float | str, second: float | str) -> None:
        self.first: float | str = first
        self.second: float | str = second

    def invoke(self) -> float | str:
        if isinstance(self.first, (float, int)) and isinstance(
            self.second, (float, int)
        ):
            self.first = self.first * self.second
            self.second = self.first / self.second
            self.first = self.first / self.second
        else:
            pass
        return self.first, self.second


class Calendar_:
    """Return month in text mode"""

    def __init__(self, day: int, month: int, year: int) -> None:
        self.day: int = day
        self.month: int = month
        self.year: int = year

    def invoke(self):
        months: list = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ]
        if self.month in range(1, 13):
            return f"{self.day} {months[self.month-1]} {self.year}"
        else:
            return f"Wrong Date..."


class TerminalGram:
    """Draw a Gram shape with rows and cols with char"""

    def __init__(self, rows: int, char: str = "*") -> None:
        self.rows: int = rows
        self.char: str = char

    def parallel(self, cols: int):
        ind: int = self.rows - 1
        gram: str = ""
        for r in range(self.rows):
            gram += " " * ind + self.char * cols + "\r\n"
            ind -= 1
        return gram[0 : len(gram) - 1]

    def dimond(self):
        """rows must be odd and >= 3"""
        if self.rows < 3 or self.rows % 2 == 0:
            return 0
        ind: int = self.rows // 2
        gram: str = ""
        for r in range(1, self.rows - 1, 2):
            gram += " " * ind + self.char * r + "\r\n"
            ind -= 1
        for r in range(self.rows, 0, -2):
            gram += " " * ind + self.char * r + "\r\n"
            ind += 1
        return gram[0 : len(gram) - 1]


class IsPrime:
    def __init__(self, number: int) -> None:
        self.number = number

    def invoke(self) -> bool:
        if self.number in range(0, 2):
            return False
        for divider in range(0, self.number):
            if divider == 1 or divider == 0:
                continue
            else:
                if self.number % divider == 0:
                    return False
        return True


class NumCast:
    """Convert methods on numbers"""

    def __init__(self, number: int) -> None:
        self.number: int = number

    def to_binary(self) -> str:
        """Convert number to binary (base2)"""
        result: str = ""
        try:
            assert isinstance(self.number, int)
        except:
            return "Error:: Value must be integer or integer like"
        else:
            if self.number == 0:
                return "0"
            while self.number != 0:
                for i in range(4):
                    bit_ = self.number % 2
                    result = str(bit_) + result
                    self.number = self.number // 2
                result = " " + result

        return result.lstrip()

    def to_letters(self) -> str:
        """Convert number to letter, alphabetically numbers"""
        try:
            assert isinstance(int(self.number), int)
        except:
            return "Error:: Value must be integer or integer like"
        else:
            letters: list = [
                "zero",
                "one",
                "two",
                "three",
                "four",
                "five",
                "six",
                "seven",
                "eight",
                "nine",
            ]
            result: str = ""
            for i in str(self.number):
                result += f"{letters[int(i)]} "
            return result

    def to_roman(self):
        """Converts to Roman Numbers X,XI,III,..."""
        num_dict: dict[int, str] = {
            1: "I",
            2: "II",
            3: "III",
            4: "IV",
            5: "V",
            6: "VI",
            7: "VII",
            8: "VIII",
            9: "IX",
            10: "X",
            20: "XX",
            30: "XXX",
            40: "XL",
            50: "L",
            60: "LX",
            70: "LXX",
            80: "LXXX",
            90: "XC",
            100: "C",
            200: "CC",
            300: "CCC",
            400: "CD",
            500: "D",
            600: "DC",
            700: "DCC",
            800: "DCCC",
            900: "CM",
        }
        m = self.number % 10

        return f"{num_dict[10]}{num_dict[m]}"


class LoginAttempts:
    """Will let check user and pass for 'attempts' times"""

    def __init__(self, username: str, password: str) -> None:
        self.username, self.password = username, password

    def attemp(self, attempts: int):
        att: int = attempts
        while attempts != 0:
            username, password = input("username: "), input("password: ")
            if self.username == username and self.password == password:
                return f"Login Successfull"
            else:
                print(f"username or password incorrect")
                attempts -= 1
                continue
        return f"Number of a login attempt is {att}"


class Guess:
    def __init__(self, phrase: str | int) -> None:
        self.phrase: str | int = phrase

    def get_number(self):
        if not isinstance(self.phrase, int):
            return 0
        g_number = 0
        import timeit

        t_1: float = timeit.default_timer()
        while g_number != self.phrase:
            g_number += 1
        else:
            t_2: float = timeit.default_timer()
            return f"Number is: {g_number}\tin {(t_2-t_1)} s"

    def get_phrase(self, depth: int = 2, include_digit: bool = False):
        import random as r
        import timeit

        resource_list: list = [chr(l) for l in range(97, 123)]
        if include_digit:
            resource_list.extend([n for n in range(0, 10)])
        phrase: str = ""
        t_1: float = timeit.default_timer()
        while phrase != self.phrase:
            sam_list: list = r.sample(resource_list, depth)
            phrase = "".join(sam_list)

        else:
            t_2: float = timeit.default_timer()
            return f"Phrase Founded: {phrase}\tin {t_2-t_1} s"


class Sorting():
    def __init__(self, *args) -> None:
        self.list: list[int]= list(args)

    def bubble_sort(self):
        import timeit
        sorted = 0
        while sorted!=len(self.list)-1:
            for index, item in enumerate(self.list):    
                for i, x  in enumerate(self.list):
                    if item>x:
                        self.list.pop(index)
                        self.list.insert(item, i)
                

        return self.list



class LongestEvenWord:
    '''Return Longest word in the sentence witch has even length
    if there id no even words returns '00'
    '''

    def __init__(self, sentence:str):
        self.words:list= sentence.split(' ')
        self.longest = "00"

    def __repr__(self) -> str:
        for word in self.words:
            if len(word)%2 ==0 and len(word)>len(self.longest):
                self.longest = word
            
        return self.longest
