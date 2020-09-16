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
            print(i)

            for j in completion:
                print(j)
                if i == j:
                    participant.remove(j)

    answer = participant
    print(answer)
    return answer

participant = ['leo', 'kiki', 'eden']
completion = ['eden', 'kiki']

solution(participant , completion)

