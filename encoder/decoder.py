class Decoder:
    def __init__(self):
        self.__source = ''

    def __encode(self, sin = ''):
        sout = ''
        number = 0
        if len(sin) == 1:
            number = int(sin)
        elif len(sin) == 3:
            number = int(sin[0:2])
        match number:
            case  1: sout = 'a'
            case  2: sout = 'b'
            case  3: sout = 'c'
            case  4: sout = 'd'
            case  5: sout = 'e'
            case  6: sout = 'f'
            case  7: sout = 'g'
            case  8: sout = 'h'
            case  9: sout = 'i'
            case 10: sout = 'j'
            case 11: sout = 'k'
            case 12: sout = 'l'
            case 13: sout = 'm'
            case 14: sout = 'n'
            case 15: sout = 'o'
            case 16: sout = 'p'
            case 17: sout = 'q'
            case 18: sout = 'r'
            case 19: sout = 's'
            case 20: sout = 't'
            case 21: sout = 'u'
            case 22: sout = 'v'
            case 23: sout = 'w'
            case 24: sout = 'x'
            case 25: sout = 'y'
            case 26: sout = 'z'
            case _:  raise Exception('Incorrect code')
        return sout

    def __other(self, sin = ''):
        sout = ''
        number = 0
        if sin.find('#') == -1:
            for i in range(len(sin)):
                sout += self.__encode(sin[i:i+1])
        elif sin[0] == '0' or sin[0] == '#' or sin[1] == '0' or sin[1] == '#':
            raise Exception('Invalid code')
        else:
            number = sin.find('#')
            if (number - 2) > 0:
                for i in range(number - 2):
                    sout += self.__encode(sin[i:i+1])
            sout += self.__encode(sin[number-2:number+1])
            if len(sin)-1 > number:
                sout += self.__other(sin[number+1:])
        return sout

    def decoding(self, sin = ''):
        return self.__other(sin)
