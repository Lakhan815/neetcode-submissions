# my idea for it:
# go through the inital array, make a temp array where you turn each string into a char array and sort it
# then go through the array again, see if any arrays have the same chars, if they do take the index from the
# og array and put it into a new array with similar chars



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i,j in enumerate(strs):
            word = j
            sorted_chars = sorted(word)
            key = "".join(sorted_chars)
            d[key].append(j)
        return list(d.values())