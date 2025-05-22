class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            signature = ''.join(sorted(word)) # signature is the sorted string
            if signature not in groups:
                groups[signature] = [] # create a new dictionary entry, no value
            groups[signature].append(word) # appends value 'word' to key 'signature'
        return list(groups.values())