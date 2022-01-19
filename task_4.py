def func(*args):
        sum_ = 0
        for i in args:
            if type(i) == int or type(i) == float:
                sum_ += i
        return sum_
