import collections

class Solution(object):
    def recoverArray(self, n, sums):
        """
        :type n: int
        :type sums: List[int]
        :rtype: List[int]
        """
      
        sums.sort()
        
        ans = []
        
       
        for _ in range(n):
          
            d = sums[1] - sums[0]
            
           
            s_next = []
            
     
            counts = collections.Counter(sums)
            
        
            for s in sums:
                if counts[s] > 0:
                
                    if counts[s + d] > 0:
                        s_next.append(s)
                        counts[s] -= 1
                        counts[s + d] -= 1
            
           
            s_next_set = set(s_next)
            
           
            if 0 in s_next_set:
                ans.append(d)
                sums = s_next
            else:
               
                ans.append(-d)
               
                sums = [s + d for s in s_next]
                
        return ans
    

    import collections

import collections
