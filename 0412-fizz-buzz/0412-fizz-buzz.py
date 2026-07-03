class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        sample = [""]*n
        for i in range(1, n+1):
            sample[i-1] = f"{i}"

            if i%3 == 0 and i%5 == 0:
                sample[i-1] = "FizzBuzz"
            elif i%3 == 0:
                sample[i-1] = "Fizz"
            elif i%5 == 0:
                sample[i-1] = "Buzz"
                
        return sample