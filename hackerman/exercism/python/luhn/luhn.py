class Luhn:
    def __init__(self, card_num):
        self.__card_num = str(card_num).strip()

    def valid(self):
        try:
            card_num = self.__card_num.replace(' ', '')
            if card_num.__len__() > 1:
                card_num = [int(x) for x in card_num[::-1]]
                for x in range(1, card_num.__len__(), 2):
                    doubled = int(card_num[x]) * 2
                    if doubled > 9:
                        card_num[x] = doubled - 9
                    else:
                        card_num[x] = doubled
                if sum(card_num) % 10 == 0:
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            print(e)
            return False
