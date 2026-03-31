class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        For each day, build a stack which keeps track of how many days until we hit a warmer one
        """
        result = [0] * len(temperatures)
        stack = [] # stores indices

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_day = stack.pop()
                result[prev_day] = i - prev_day
            stack.append(i)
            
        return result