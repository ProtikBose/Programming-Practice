class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        stringVal = list(s)
        for val in range(len(indices)) :
            stringVal[indices[val]] = s[val]
        return "".join(stringVal)