import time


def time_function(function, *args, **kwargs):
    def timer(*args):
        start = time.time()  # Takes time at start
        f = (function(args))
        end = time.time()  # Takes time at end
        elapsed = end - start  # Takes difference
        print('Function: {} \nTime elapsed: {}'.format(function.__name__, elapsed))  #
        return f
    return timer


@time_function
def Hello_(word):
    print('Hello, {}!'.format(word))


print(Hello_('Dave'))
