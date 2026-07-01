class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)
        l=0
        ans=[]
        temp=[]
        for r in range(n):
            temp.append(nums[r])
            if (r-l==k):
                temp.pop(0)
                l+=1
            if(r-l+1==k):
                ans.append(temp[-1] - temp[0])
        return min(ans)
               

