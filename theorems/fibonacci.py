
class Finbonacci:

    cache = dict()

    def common(self, n):

        if n <= 2:
            return 1
        else:
            return self.common(n-1) + self.common(n-2)

    def dynamic_memory(self, n):

        if n <= 1:
            return n

        if n not in self.cache:
            self.cache.__setitem__(n , self.dynamic_memory(n-1) + self.dynamic_memory(n-2))

        return self.cache.get(n)
