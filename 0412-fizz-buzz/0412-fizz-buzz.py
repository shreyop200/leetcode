class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        sample = []
        for i in range(1, n+1):
            if i%3 == 0 and i%5 == 0:
                sample.append("FizzBuzz")
            elif i%3 == 0:
                sample.append("Fizz")
            elif i%5 == 0:
                sample.append("Buzz")
            else:
                sample.append(str(i))
                
        return sample