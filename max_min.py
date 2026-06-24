class max_min:
    def max_i(self,n1,n2):
        if n1>n2:
            print(f"{n1} is max")
        elif n2>n1:
            print(f"{n2} is max")
    def min_i(self,n1,n2):
        if n2>n1:
            print(f"{n1} is min")
        elif n2<n1:
            print(f"{self.n2} is min")
m=max_min()
m.max_i(1,2)
m.min_i(1,2)
