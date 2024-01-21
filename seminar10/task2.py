class LotteryGame:
    def __init__(self, list1: list, list2: list):
        self.list1 = list1
        self.list2 = list2

    def compare_lists(self):
        out_list = [i for i in self.list1 if i in self.list2]
        if out_list:
            print(f'Совпадающие числа: {out_list}\nКоличество совпадающих чисел: {len(out_list)}')
        else:
            print('Совпадающих чисел нет.')


if __name__ == '__main__':
    list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
    list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]
    game = LotteryGame(list1, list2)
    matching_numbers = game.compare_lists()
