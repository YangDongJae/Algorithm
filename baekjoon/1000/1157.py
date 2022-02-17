import string

input_word = input()

data = list(map(str, input_word))
check_data = list()

for i in data:
    check_data.append(ord(i))

for j in check_data:
    if j - 32 in check_data:
        check_data[check_data.index(j-32)] = check_data[check_data.index(j-32)] + 32

value_dict = dict.fromkeys(string.ascii_lowercase,0)

for k in check_data:
    value_dict[chr(k)] += 1

max_value = max(value_dict.values())
result_list = list()

for key,value in value_dict.items():
    if value == max_value:
        result_list.append(key)

if len(result_list) >= 2:
    print("?")
else:
    print(chr(ord(result_list[0])- 32))


# words = input().upper()
# unique_words = list(set(words))  # 입력받은 문자열에서 중복값을 제거
# print(unique_words)

# cnt_list = []
# for x in unique_words :
#     cnt = words.count(x)
#     cnt_list.append(cnt)  # count 숫자를 리스트에 append
#     print(cnt_list)

# if cnt_list.count(max(cnt_list)) > 1 :  # count 숫자 최대값이 중복되면
#     print('?')
# else :
#     max_index = cnt_list.index(max(cnt_list))  # count 숫자 최대값 인덱스(위치)
#     print(unique_words[max_index])