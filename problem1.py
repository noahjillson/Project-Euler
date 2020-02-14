# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. 
# Find the sum of all the multiples of 3 or 5 below 1000.

class problem_1:
    def __init__(self, max:int, multiples:list):
        self.max_num = max
        self.multiples = multiples

    def calculate_multpiples_sum(self):
        sum = 0
        for x in range(self.max_num):
            if x % self.multiples[0] == 0 or x % self.multiples[1] == 0:
                sum += x
        print(sum)

        
if __name__ == "__main__":
    p1 = problem_1(1000, [3, 5])
    p1.calculate_multpiples_sum()

