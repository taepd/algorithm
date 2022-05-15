length = int(input())
test_case = list(map(int, input().split()))
num_dict = {}
index_dict = {}
for index, num in enumerate(test_case):
    num_dict[num] = {
        'index': index,
        'processed': False
    }
    index_dict[index] = {
        'num': num
    }

for _, num in enumerate(test_case):
    num_dash = num - 1
    if num_dash == 0:
        continue
    if num_dict[num_dash].get('processed'):
        continue
    if num_dict[num].get('processed'):
        continue
    num_dash_idx = num_dict[num_dash].get('index')
    num_idx = num_dict[num].get('index')

    if num_idx > num_dash_idx:
        continue

    num_dict[num_dash] = {
        'index': num_idx,
        'processed': True
    }
    index_dict[num_idx] = {
        'num': num_dash
    }
    num_dict[num] = {
        'index': num_dash_idx,
        'processed': True
    }
    index_dict[num_dash_idx] = {
        'num': num
    }

answers = []
for idx in range(length):
    answers.append(str(index_dict[idx]['num']))

print(" ".join(answers))