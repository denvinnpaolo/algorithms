class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        combined = collections.deque()
        
        p1, p2 = len(nums1) - 1, len(nums2) - 1
        
        while len(nums1) > 0 or len(nums2) > 0:
            n1 = nums1.pop() if len(nums1) > 0 else -1000001
            n2 = nums2.pop() if len(nums2) > 0 else -1000001
            
            
            if n1 >= n2:
                if n1 != -1000001:
                    combined.appendleft(n1)
                if n2 != -1000001:
                    nums2.append(n2)
            else:
                if n2 != -1000001:
                    combined.appendleft(n2)
                if n1 != -1000001:
                    nums1.append(n1)
                    
                
      
        print(combined)      
        if len(combined) % 2 == 0:
            return (combined[len(combined)//2 ] + combined[len(combined)//2 - 1]) / 2

        
        else: return combined[len(combined)//2]