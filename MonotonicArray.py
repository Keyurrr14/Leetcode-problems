class Solution:
  def is_inc(self, A: List[int]) -> bool:
    for i in range(1, len(A)):
      if A[i] < A[i - 1]:
        return False
    
    return True
  
  def is_dec(self, A: List[int]) -> bool:
    for i in range(1, len(A)):
      if A[i] > A[i - 1]:
        return False
    
    return True
    
  def isMonotonic(self, A: List[int]) -> bool:
    return self.is_inc(A) or self.is_dec(A)