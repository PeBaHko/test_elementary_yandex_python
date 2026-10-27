class Counter:

    @classmethod
    def print(cls):
        print('класс счётчик - print from counter')

    def __init__(self):
        self.__capital_of_company = []
        self.__prediction = []
        self.__count_of_company = 0

    def print_count_of_company(self):
        print('print counter of company - ' + str(self.__count_of_company))

    def print_of_capital(self):
        print('print capital:  ', end='')
        for numb in self.__capital_of_company:
            print(' ' + str(numb), end='')
        print()

    def set_count_of_company(self, size = 0):
        self.__count_of_company = size

    def set_capital_of_company(self, capital = None):
        if capital is None:
            self.__capital_of_company = []
        else:
            self.__capital_of_company = capital

    def print_predict(self):
        for numb in self.__prediction:
            print(' - ' + str(numb))

    def calculation(self):
        self.__prediction = []
        win  = True
        j = 0
        for i in range(len(self.__capital_of_company)):
            if self.__capital_of_company[i] == 1:
                self.__prediction.append(0)
            else:
                sum = 0
                j = 0
                for j in range(j, i):
                    sum += self.__capital_of_company[j]
                j += 1
                sum += self.__capital_of_company[j]
                win = True
                j += 1
                for j in range(j, len(self.__capital_of_company)):
                    if self.__capital_of_company[j] < sum:
                        sum += self.__capital_of_company[j]
                    else:
                        self.__prediction.append(0)
                        win = False
                        break
                if win:
                    self.__prediction.append(1)
