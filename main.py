import time

from sequences import fibonacci


def main():
    fib = fibonacci.Finbonacci()
    fn = 30

    t = time.time()
    print(fib.recursive(fn))
    print(time.time() - t)

    t = time.time()
    print(fib.memoize(fn))
    print(time.time() - t)

    t = time.time()
    print(fib.buttom_up(fn))
    print(time.time() - t)

if __name__ == '__main__':
    main()