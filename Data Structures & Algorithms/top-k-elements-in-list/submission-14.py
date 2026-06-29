# do another hash map
# find out which value is the most frequent
# put the numbers into an array with length k


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = [0] * k
        for i in range(k):
            freq = Counter(nums)
            res = max(freq, key=freq.get)
            print(res)
            a[i] = res
            while res in nums:
                nums.remove(res)
        return a