class Fibonacci:
    def __init__(self):
        self.sequence = [0, 1]

    def generate_sequence(self, n):
     

        if n <= 2:
            return self.sequence[:n]


        for i in range(2, n):
            next_number = self.sequence[-1] + self.sequence[-2]
            self.sequence.append(next_number)

        return self.sequence


fibonacci_generator = Fibonacci()
n = int(input("Enter a positive integer greater than 2: "))

sequence = fibonacci_generator.generate_sequence(n)
print(f"The Fibonacci sequence of the first {n} numbers is: {', '.join(map(str, sequence))}")
