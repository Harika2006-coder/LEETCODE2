class Solution(object):
    def minNumber(self, nums1, nums2):
        arr=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    arr.append(nums1[i])
        if len(arr)>0:
            return min(arr)
             
            
        else:
                    s=" "
                    min1=min(nums1)
                    min2=min(nums2)
                    s+=str(min1)
                    s+=str(min2)
                    if int(s)<int(s[::-1]):
                        return int(s)
                    else:
                        return int(s[::-1])

        
        
