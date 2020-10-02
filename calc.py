from symbol import power
import random

class Calculator:

    def __init__(self, init_value=0):
        self.value = init_value


    def limit(self, args):
        max_args = 10
        new_args = args
        if(len(args) > max_args):
            new_args = []
            for i in range(max_args):
                new_args.append(args[i])
        for i in range(len(new_args)):
            print(new_args[i], end = ' ')
        return new_args

    def add(self, *args):
        args = self.limit(args)
        self.value += sum(args)
        return self

    def multiply(self, *args):
        args = self.limit(args)
        for x in args:
            self.value *= x
        return self

    def divide(self, *args, integer_divide=False):
        args = self.limit(args)
        for x in args:
            if(x==0):
                print('Incorrect argument')
                exit(0)
            else:
                if integer_divide:
                    self.value //= x
                else:
                    self.value /= x
            return self

    def subtract(self, *args):
        args = self.limit(args)
        self.value -= sum(args)
        return self

    def power(self, *args):
        args = self.limit(args)
        const = self.value
        for i in args:
            for x in range(i - 1):
                self.value *= const
        return self

    def __repr__(self):
        return self.value

    def __str__(self):
        return str(self.value)

def fun(x):
    return x[::-1]


if __name__ == '__main__':
    calculator = Calculator(random.randint(0,100))
    print('Your int:',calculator)
    print('Result:', calculator.power(2,3).add(1, 2, 3, 5.1).multiply(4, 0.123).subtract(4, 1, -100).divide(5, integer_divide=True))