def solution(babbling):
    answer = 0
    says = ["aya", "ye", "woo", "ma"]
    for cur_str in babbling:
        cut_str = cur_str

        for say_word in says:
            if say_word in cur_str:
                cut_str = cut_str.replace(say_word, " ")

        if len(cut_str.strip()) == 0 :
            answer += 1

    return answer