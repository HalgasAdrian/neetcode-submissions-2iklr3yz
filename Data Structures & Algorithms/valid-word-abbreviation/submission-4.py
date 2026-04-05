class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """
        Use two pointers here
        
        Check if the index at for each string is the same char

        If they are not the same we check if its a number

        IF yes to number, move the pointer in word as forward by 
        whatever the number is, if not we return false

        """
        words = 0
        abbrs = 0

        if word == abbr:
            return True
        
        while words < len(word) and abbrs < len(abbr):
            if word[words] == abbr[abbrs]:
                words += 1
                abbrs += 1
            elif abbr[abbrs].isdigit() and abbr[abbrs] != '0':
                jump_str = ""
                while abbrs < len(abbr) and abbr[abbrs].isdigit():
                    jump_str += abbr[abbrs]
                    abbrs += 1
                jump = int(jump_str)
                words = words + jump
            else:
                return False
        return words == len(word) and abbrs == len(abbr)