class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        max_candies = max(candies)
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
        result = []

        for candy in candies:
            if candy + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)

        return result

