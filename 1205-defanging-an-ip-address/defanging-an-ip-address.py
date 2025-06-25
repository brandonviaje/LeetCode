class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        """
        how to solve: iterate through the address, check whether each index is a period, if so, append [ to the previous index and ] to
        the following index.
        """
        
        my_list = address.split('.')
        
        length = len(my_list)
        
        defanged = ""
        
        for i in range(length - 1):
            defanged += my_list[i] + '[.]'
        
        defanged += my_list[-1]
        
        return defanged