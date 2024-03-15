def solution(number):
    return_value = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            return_value += i

    return return_value


print(str(solution(10)))
