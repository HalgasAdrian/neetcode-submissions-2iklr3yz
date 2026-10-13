class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        key = { ")" : "(", "]" : "[", "}" : "{"}

        for character in s:
            if character in key:
                if stack and stack[-1] == key[character]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(character)
        
        return True if len(stack) == 0 else False


        