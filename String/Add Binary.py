class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        result = ""
        carry = 0

        loopLen = max(len(a),len(b))
        a = a.zfill(loopLen)
        b = b.zfill(loopLen)
        #loopLen -= 1

        while(loopLen):
            tempVal = carry
            tempVal += int(a[loopLen-1])
            tempVal += int(b[loopLen-1])

            result = ("1" if tempVal%2==1 else "0") + result
            #print(result)
            carry = 1 if tempVal>=2 else 0
            #print(carry)
            #print()
            loopLen -= 1
        
        if carry is 1:
            result = "1"+result
        
        return result

sol = Solution()
print(sol.addBinary("11","1"))