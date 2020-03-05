class Problem_6:
    def __init__(self):
        n1 = self.sum_of_squares()
        n2 = self.square_of_sum()
        print(n2 - n1)

    def sum_of_squares(self):
        sum = 0
        for x in range(101):
            sum += x ** 2
        return sum

    def square_of_sum(self):
        sum = 0
        for x in range(101):
            sum += x
        return sum * sum


if __name__ == "__main__":
    p6 = Problem_6()
