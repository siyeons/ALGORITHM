# def solution(s):
#     answer = True
#     print(len(s))
#     if (len(s)==4 or len(s)==6):
#         if(s.isdigit()):
#             answer = True
#         else:
#             answer = False
#     else:
#         answer = False
#     print(answer)
# solution('a23456')


def alpha_string46(s):
    return s.isdigit() and (len(s) == 4 or len(s) == 6)