import random
def guessNumber():
    number = random.randint(1, 100)
    print('我已经想好了1-100之间的数字，你能猜到吗？')
    while True:
        guessNumber = int(input("请输入你的猜测数字:"))
        if guessNumber > number:
            print('大了，再小一点')
        elif guessNumber < number:
            print('小了，再大一点')
        else:
            print('恭喜你，猜对了，数字是：{}'.format(number))
            break


if __name__ == '__main__':
    guessNumber()