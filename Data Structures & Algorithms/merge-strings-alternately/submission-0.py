class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Create a return string 

        Using 1 pointer for each word, starting with word 1, append the character to return 

        """
        result = []
        word1Pointer = 0
        word2Pointer = 0
        word1List = list(word1) 
        word2List = list(word2)

        if len(word1List) == len(word2List):
            while word1Pointer < len(word1List) and word2Pointer < len(word2List):
                result.append(word1List[word1Pointer])
                word1Pointer += 1

                result.append(word2List[word2Pointer])
                word2Pointer += 1
        elif len(word1List) > len(word2List):
            while word2Pointer < len(word2List):
                result.append(word1List[word1Pointer])
                word1Pointer += 1

                result.append(word2List[word2Pointer])
                word2Pointer += 1
            result.extend(word1List[word1Pointer:])
        elif len(word1List) < len(word2List):
            while word1Pointer < len(word1List):
                result.append(word1List[word1Pointer])
                word1Pointer += 1

                result.append(word2List[word2Pointer])
                word2Pointer += 1
            result.extend(word2List[word2Pointer:])
        else:
            pass
        
        return "".join(result)

        