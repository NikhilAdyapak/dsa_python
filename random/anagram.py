# from collections import defaultdict

# def groupAnagrams(strs):
#     # Defaultdict automatically handles missing keys by creating an empty list
#     anagram_map = defaultdict(list)
    
#     for s in strs:
#         # Sort the string to use as a universal key for all its anagrams
#         sorted_s = "".join(sorted(s))
#         anagram_map[sorted_s].append(s)
        
#     return list(anagram_map.values())

# print(groupAnagrams(["eat","tea","tan","ate","nat","bat"])) 
# # -> [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

from collections import defaultdict

def group(arr):
    anagram_map = defaultdict(list)

    for s in arr:
        sorted_s = "".join(sorted(s))
        anagram_map[sorted_s].append(s)
    
    print(list(anagram_map.values()))

arr = ["eat","tea","tan","ate","nat","bat"]
group(arr)


# from collections import defaultdict

# def group(arr):
#     anagram_map = defaultdict(list)

#     for s in arr:
#         sorted_s = "".join(sorted(s))
#         anagram_map[sorted_s].append(s)
    
#     print(list(anagram_map.values()))