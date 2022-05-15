"""
로그를 재정렬하라. 기준은 다음과 같다.
1. 로그의 가장 앞 부분은 식별자다.
2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
4. 숫자 로그는 입력 순서대로 한다.

- 입력
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
- 출력
["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
"""

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

from typing import List


def reorderLogFiles(logs: List[str]) -> List[str]:
    letters, digits = [], []
    for log in logs:
                    # 식별자 이외의 로그가 숫자인지 판별해서 digit과 letters로 분류
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    # 두 개의 키를 람다 표현식으로 정렬
    # 문자가 동일할 경우 식별자로 정렬하기 위해 정렬 키를 x.split()[0]를 후순위로 지정
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits

print(reorderLogFiles(logs))