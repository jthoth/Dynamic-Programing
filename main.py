import time

from theorems import fibonacci


def main():
    fib = fibonacci.Finbonacci()
    fn = 30

    t = time.time()
    print(fib.common(fn))
    print(time.time() - t)

    t = time.time()
    print(fib.dynamic_memory(fn))
    print(time.time() - t)

if __name__ == '__main__':
    main()