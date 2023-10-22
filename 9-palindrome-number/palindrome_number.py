class Solution(object):
    def isPalindrome_1(self, x):
        """
        brute force solution
        :type x: int
        :rtype: bool
        """
        x_string = str(x)
        if len(x_string)%2==0:
            for i in range((len(x_string)/2)):
                if x_string[i] != x_string[len(x_string)-i-1]:
                    return False
            return True
        elif len(x_string)%2==1:
            for i in range((len(x_string)-1)/2):
                if x_string[i]!= x_string[len(x_string)-i-1]:
                    return False
            return True

    def isPalindrome_2(self, x):
        """
        optimized solution 1
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        return str(x) ==str(x)[::-1]