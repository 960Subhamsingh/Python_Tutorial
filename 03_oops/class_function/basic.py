class calculation:
    def __init__(self, num, num1) -> None:
        self.num = num =12
        self.num1 = num1=12
    def __str__(self):
        if(self.num==0):
            return f"{self.num}"
        elif(self.num1<=2):
            return f"{self.num1}"
        else:
            s = f"{self.num} {self.num1}"
        return s
    def __add__(self, other):
        total = 0
        total = self.num + self.num1
        total1 = calculation(total)
        return total1

f = calculation(12,34)
g = calculation(12.5)

print(f,g)










# import random

# class ran:
#     def __init__(self, item):
#         self._items = list(self._items) 
#         random.shuffle(self._items)
#     def main(self):
#         try:
#             return self._items.pop()
#         except IndexError:
#             raise LookupError('pick from emptyran')
#     def _call__(self):
#         return self.pick()

# obj = ran(12)
# obj.main()