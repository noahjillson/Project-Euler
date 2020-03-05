# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

class Problem_5:
    def __init__(self, max_divisor: int):
        self.max_divisor = max_divisor

    def calculate_largest_divisible_num(self):
        i = 10
        while True:
            isdivisible: bool = True
            for x in range(1, 21):
                if i % x != 0:
                    i += 10
                    isdivisible = False
                    break
            if isdivisible:
                return i


if __name__ == "__main__":
    p5 = Problem_5(20)
    print(p5.calculate_largest_divisible_num())
