class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_length = len(a)
        b_length = len(b)
        max_length = max(a_length, b_length)

        i = 0
        carry_over = "0"
        result = ""
    
        # Pad str1 if needed
        if b_length < max_length:
            b = '0' * (max_length - b_length) + b
        
        # Pad str2 if needed
        if a_length < max_length:
            a = '0' * (max_length - a_length) + a


        for i in range(max_length - 1, -1, -1):
            print(i)
            if carry_over == "0":
                if a[i] == "1" and b[i] == "1":
                    carry_over = "1"
                    result = "0" + result
                elif (a[i] == "1" and b[i] == "0") or (a[i] == "0" and b[i] == "1"):
                    result = "1" + result
                else:
                    result = "0" + result
            else:
                if a[i] == "1" and b[i] == "1":
                    carry_over = "1"
                    result = "1" + result
                elif (a[i] == "1" and b[i] == "0") or (a[i] == "0" and b[i] == "1"):
                    carry_over = "1"
                    result = "0" + result
                else:
                    carry_over = "0"
                    result = "1" + result
        if carry_over == "1":
            result = "1" + result
        
        return result




