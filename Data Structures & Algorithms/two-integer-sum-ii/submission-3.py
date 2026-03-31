class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i: int = 0
        j: int = len(numbers) - 1
        currSum = numbers[i] + numbers[j]

        while currSum != target:
            if currSum > target:
                j -= 1
            else:
                i += 1
            currSum = numbers[i] + numbers[j]

        return [i + 1, j + 1]