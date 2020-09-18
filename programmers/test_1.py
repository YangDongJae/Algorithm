#type 1
# def solution(participant, completion):
#     """    
#     1. 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
#     2. completion의 길이는 participant의 길이보다 1 작습니다.
#     3. 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
#     4. 참가자 중에는 동명이인이 있을 수 있습니다.
#     """
#     if len(participant) < 1 or len(participant) > 100000:
#         print("error! please check your runner list!")
    
#     elif len(participant) - len(completion) != 1:
#         print("error! please check your runner list!")

#     else:
#         for i in participant:
#             if len(i) < 1 or len(i) > 20:
#                 print("error! please check your runner list!")
#                 break

#             for j in completion:
#                 if i == j:
#                     participant.remove(j)

#     answer = participant
#     print(answer)
#     return answer



# type 2
#solution(participant , completion)

# if len(participant) < 1 or len(participant) > 100000:
#     print("error! please check your runner list!")

# elif len(participant) - len(completion) != 1:
#     print("error! please check your runner list!")

# else:
#     for i in participant:
#         if len(i) < 1 or len(i) > 20:
#             print("error! please check your runner list")
#             break
    
#         for j in completion:
#             if i == j:
#                 print(j)

#                 # python search index number use by element
#                 # <List>.index("element")
#                 participant.pop(participant.index(i))

# print(participant)


#type 3
# participant = ['leo', 'kiki', 'eden']
# completion = ['eden', 'kiki']

# result = []
# for i in participant:
#     print("[" , i , "]" )
#     for j in completion:
#         print( i , j)
#         if i == j:
#             result.append(i)
#             participant.remove(i)
#             completion.remove(i)
#             print('reuslt = ' , result)
#             print('participant' , participant)
#     print('----')
    
# print(participant , completion)


#type 4
# participant = ['leo', 'kiki', 'eden']
# completion = ['eden', 'kiki']

# import copy
# participant = ['leo', 'kiki', 'eden']
# completion = ['eden', 'kiki']

# participant_copy = copy.copy(participant)
# completion_copy = copy.copy(completion)
# for i in participant:
#     for j in completion:
#         if i == j:
#             participant_copy.remove(i)
#             completion_copy.remove(j)

# print(participant_copy)

#type 5
# participant = ['leo', 'kiki', 'eden']
# completion = ['eden', 'kiki']

# for i in participant[:]:
#   if i in completion:
#     participant.remove(i)
#     completion.remove(i)

# print(participant)

#result Function

def solution(participant, completion):
    """    
    1. 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
    2. completion의 길이는 participant의 길이보다 1 작습니다.
    3. 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
    4. 참가자 중에는 동명이인이 있을 수 있습니다.
    """
    if len(participant) < 1 or len(participant) > 100000:
        print("error! please check your runner list!")
    
    elif len(participant) - len(completion) != 1:
        print("error! please check your runner list!")

    else:
        for i in participant:
            if len(i) < 1 or len(i) > 20:
                print("error! please check your runner list!")
                break

            for i in participant[:]:
                if i in completion:
                    participant.remove(i)
    
    return participant

participant = ['leo', 'kiki', 'eden']
completion = ['eden', 'kiki']
print(solution(participant , completion))