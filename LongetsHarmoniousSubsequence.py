class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        i,j,n,ans=0,0,len(nums),0
        while j<n: 
            while nums[j]-nums[i]>1: 
                i+=1
            if nums[j]-nums[i]==1: ans=max(ans,j-i+1)
            j+=1
        return ans