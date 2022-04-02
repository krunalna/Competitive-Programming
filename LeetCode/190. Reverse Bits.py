#190. Reverse Bits


#method1 : bitwise

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        
        rev , power = 0, 31
        
        while n:
            rev += (n&1) << power     # (n&1) gets the last bit of n and  << power left shifts that last bit by power
                                        # add the power shifted bit to rev
            n = n >>1                   #right shift n by 1
            power -=1                   # decrease power by 1
            
        return rev

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        
        binary_number = bin(n)[2:]
        
        binary_string = "0"*(32-len(binary_number))+binary_number
        
        reverse_binary_string = binary_string[::-1]
        
        return int(reverse_binary_string,2)




