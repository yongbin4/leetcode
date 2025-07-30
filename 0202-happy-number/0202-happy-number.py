class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # to get the digit of a number we will use modulo 
        # we start with the smaller modulo and increase the digit for modulo

        str_n = str(n)
        result = 0
        seen = set()  # ADD THIS: Track seen numbers to detect cycles
        
        while result != 1:
            # ADD THIS: Check for cycle before processing
            if int(str_n) in seen:
                return False  # Cycle detected, not happy
            seen.add(int(str_n))
            
            result = 0  # ADD THIS: Reset result for each iteration
            
            for i in range(len(str_n)):
                result += pow(int(str_n[i]), 2)
            str_n = str(result)
            
        return True if result == 1 else False