class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return 0

       
        all_numbers = set()
        for x in nums:
            all_numbers.add(x)
           
            all_numbers.add(2 * x)
        
        sorted_unique_numbers = sorted(list(all_numbers))
        ranks = {val: i + 1 for i, val in enumerate(sorted_unique_numbers)}
        
        
        bit_size = len(ranks) + 1
        bit = [0] * bit_size

        def update(index, delta):
            """Adiciona delta ao valor no índice e propaga para cima."""
            while index < bit_size:
                bit[index] += delta
                index += index & (-index)

        def query(index):
            """Retorna a soma dos valores de 1 até o índice."""
            s = 0
            while index > 0:
                s += bit[index]
                index -= index & (-index)
            return s


        reverse_pairs_count = 0
        
       
        for j in range(n):
         
            
           
            import bisect
            val_to_check = 2 * nums[j]
            
           
            rank_of_2x = bisect.bisect_right(sorted_unique_numbers, val_to_check)
            
            count_le = query(rank_of_2x) 
            

            total_processed = j
            count_gt = total_processed - count_le
            
            reverse_pairs_count += count_gt
            
            update(ranks[nums[j]], 1)
            
        return reverse_pairs_count
    

    