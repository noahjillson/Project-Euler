# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

class problem_2:
    def __init__(self, max:int, divisor:int):
        self.max_num = max
        self.divisor = divisor

    def calculate_fibonacci_sum(self):
        sum = 0
        num1 = 1
        num2 = 2
        while(num2 < self.max_num):
            if num2 % 2 == 0:
                sum = sum + num2
            saved = num2
            num2 = num1 + num2
            num1 = saved
            # print(str(num1) + " " + str(num2))
        print(sum)

        
if __name__ == "__main__":
    p1 = problem_2(4000000, 2)
    p1.calculate_fibonacci_sum()
    print("hello world")

