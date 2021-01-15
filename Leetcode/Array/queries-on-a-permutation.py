class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = [i for i in range(1, m+1)]
        result = []
        for i in queries:
            idx = p.index(i)
            result.append(idx)
            p.pop(idx)
            p.insert(0, i)
        return result