"""
금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며 구두점(마침표, 쉼표 등)또한 무시한다.
- 입력
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
- 출력
"ball"
"""

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

# 리스트 컴프리헨션, Counter 객체 활용
import re

# 정규식: ^는 not, \w는 단어 문자(Word Character)를 의미
# paragraph에서 단어가 아닌 것은 공백으로 처리해서 list화
# split()을 적용하지 않으면 각 알파벳이 요소가 되어 리스트가 되는데,
# spilt()을 적용함으로써 공백을 기준으로 나눠서 리스트화. 즉, 단어별로 리스트가 됨
words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
         .lower().split() if word not in banned]

print(words)

# collections.defaultdict(), max(,key=) 활용
import collections

# collections.defaultdict(int)로 해주면 int값이 기본키로 설정됨(최초값 0)
counts = collections.defaultdict(int)
for word in words:
    counts[word] += 1

print(counts)

# dict에서 get(key)는 value를 리턴한다
# max 함수에 key로 get함수를 지정해서 카운트가 가장 큰 것을 반환하도록 함
print(max(counts, key=counts.get))

# Counter 객체 활용
counts = collections.Counter(words)
print(counts.most_common(1))

# 최종

import collections
import re
from typing import List

def mostCommonWord(paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
            .lower().split()
                 if word not in banned]

        counts = collections.Counter(words)
        # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
        return counts.most_common(1)[0][0]