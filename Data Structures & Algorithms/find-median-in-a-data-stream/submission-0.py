class MedianFinder:

    def __init__(self):
        self.arr = []
        

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()

    def findMedian(self) -> float:
        l = len(self.arr)
        if not l: return 0

        if l == 1: return self.arr[0]

        m = len(self.arr) % 2
        m2 = len(self.arr) // 2

        print(m)
        print(m2)
        print(self.arr)

        if m != 0:
            return self.arr[m2]
        else:
            return (self.arr[m2] + self.arr[m2-1])/2
        
        