
class Finbonacci:

    cache = dict()

    def recursive(self, n):

        if n <= 2:
            return 1
        else:
            return self.recursive(n-1) + self.recursive(n-2)

    def memoize(self, n):

        if n <= 1:
            return n

        if n not in self.cache:
            self.cache.__setitem__(n , self.memoize(n-1) + self.memoize(n-2))

        return self.cache.get(n)

    def buttom_up(self, n):
        fib = dict()

        for k in range(1, n+1):
            if k <= 2:
                f = 1
            else:
                f = fib.get(k-1) + fib.get(k-2)
            fib.__setitem__(k,f)

        return fib.get(n)
