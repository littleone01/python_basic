def fib_generator(number):
    # todo: 构造一个返回斐波那契数的生成器
    pass


if __name__ == '__main__':
    fg = fib_generator(5)
    for i in range(5):
        print(next(fg))
    # output: 1 1 2 3 5