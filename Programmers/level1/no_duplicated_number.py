# def solution(arr):
#     answer = []
#     for i in range(1, len(arr)):
#         if (arr[i-1] == arr[i]):
#             arr[i-1] = 'x'
#     while 'x' in arr:
#         arr.remove('x')
#     answer = arr
#     return answer

def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer