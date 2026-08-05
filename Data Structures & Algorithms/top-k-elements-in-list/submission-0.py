class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        cnt = {}
        occurrence = [[] for i in range(len(nums)+1)]
        res = []

        for j in nums:
             cnt[j] = 1+ cnt.get(j,0)
        
        for j, c in cnt.items():
            occurrence[c].append(j)

        for i in range(len(occurrence)-1, 0, -1):
            for j in occurrence[i]:
                res.append(j)
                if len(res) == k:
                    return res


        