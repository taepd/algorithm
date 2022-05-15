"""
문자열 배열을 받아 애너그램 단위로 그룹핑하라.
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

import collections
from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        # 정렬하여 딕셔너리에 추가
        # Delimiter.join(): 리스트를 구분자를 기준으로 string으로 반환. cf) split() : 리스트로 반환
        # ''.join(sorted(word))를 통해 정렬하여 애너그램끼리 같은 key로 그룹핑하고
        # list 형식의 value에 해당 word를 append하는 전략
        anagrams[''.join(sorted(word))].append(word)
    # dict.values()는 view객체에 해당하므로 정확성을 위해 list로 캐스팅 필요
    return list(anagrams.values())

print(groupAnagrams(strs))

anagrams = collections.defaultdict(list)



