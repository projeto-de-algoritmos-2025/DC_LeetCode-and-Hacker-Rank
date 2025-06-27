class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
  
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        
        low = 0
        high = m
        
        half_len = (m + n + 1) / 2 

        while low <= high:
            partition1 = (low + high) / 2
            partition2 = half_len - partition1

            
            max_left1 = nums1[partition1 - 1] if partition1 > 0 else float('-inf')
           
            min_right1 = nums1[partition1] if partition1 < m else float('inf')

           
            max_left2 = nums2[partition2 - 1] if partition2 > 0 else float('-inf')
           
            min_right2 = nums2[partition2] if partition2 < n else float('inf')

            if max_left1 <= min_right2 and max_left2 <= min_right1:
                
                total_len = m + n
                
                if total_len % 2 == 0:
                    
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2.0
                else:
                    
                    return float(max(max_left1, max_left2))
            
            elif max_left1 > min_right2:
                
                high = partition1 - 1
            else:
                
                low = partition1 + 1



