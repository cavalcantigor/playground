class Luhn:
    def __init__(self, card_num):
        self.__card_num = card_num

    def valid(self):
        try:
            if self.__card_num.__len__() > 1:
                luhn = [int(x) for x in self.__card_num.strip()]
                for x in range(luhn.__len__() - 2, 0, -2):
                    print('X: ' + str(luhn[x]))
                print(luhn)
                self.__card_num = self.__card_num.strip()
            else:
                return False
        except Exception as e:
            print(e)
            return False

if __name__ == "__main__":
    print(Luhn("0591 1234").valid())

