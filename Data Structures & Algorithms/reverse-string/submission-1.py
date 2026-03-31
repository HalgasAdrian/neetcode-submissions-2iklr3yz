class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        2 pointers and maybe a storage variabe
        Start one pointer in the back and one in the front
        """
        front = 0
        back = len(s) - 1
        storage = 0

        while front < back and back > 0:
            s[front], s[back] = s[back], s[front]
            storage = 0
            front +=1
            back -=1
                
        return s
        