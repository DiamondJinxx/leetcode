class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = {}
        freq = [[] for i in range(len(words) + 1)]
        for w in words:
            count[w] = 1 + count.get(w, 0)
        for w, f in count.items():
            freq[f].append(w)
        result = []
        for i in range(len(freq) - 1, 0, -1):
            result.extend(sorted(freq[i]))
            if len(result) > k:
                result = result[:k]
                break
        return result
