class Solution:
    def twoOutOfThree(self, nums1, nums2, nums3):
        s1, s2, s3 = set(nums1), set(nums2), set(nums3)
        result = []
        
        for num in s1 | s2 | s3:
            count = (num in s1) + (num in s2) + (num in s3)
            if count >= 2:
                result.append(num)
                
        return result
