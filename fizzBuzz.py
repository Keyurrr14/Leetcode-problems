class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for x in range(1, n+1):
            temp = ''
            if x%3==0:
                temp+="Fizz"
            if x%5==0:
                temp+="Buzz"
            if x%3!=0 and x%5!=0:
                temp+=str(x)
            answer.append(temp)
        return answer
