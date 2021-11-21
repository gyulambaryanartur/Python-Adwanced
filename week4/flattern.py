class Array:
    def __init__(self, arr: list):
        self.flatlist = []
        self.arr = arr

    def flattens(self):
        return self.flatten(self.arr)

    def flatten(self, arrays: list):
        
        # create empty list
        while True:
            i = 0
            for i in arrays:
                if isinstance(i, list):

                    self.flatten(i)
                else:
                    self.flatlist.append(i)

            else:
                break
        return self.flatlist


if __name__ == "__main__":
    inplist = [1, [1, 2], [[1, 2], 1], [3, [3, [43, 5]]]]

    flatten = Array(inplist)
    inplist = [1, [1, 2], [[1, 2], 1], [3, [3, [43, 5]]]]

    print(flatten.flattens())
