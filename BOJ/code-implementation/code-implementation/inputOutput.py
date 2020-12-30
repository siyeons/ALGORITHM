# 백준 2557, 1000, 2558, 10950, 10951, 10952, 10953, 11021, 11022, 11718, 
# 11719, 11720, 11721, 2741, 2742, 2739, 1924, 8393, 10818, 2438, 2439, 
# 2440, 2441, 2442, 2445, 2522, 2446, 10991, 10992


# num = int(input())
# for i in range(num):
#     a, b = map(int, input().split())
#     print(a+b)

# while True:
#     try:
#         a, b = map(int, input().split())
#         print(a+b)
#     except:
#         break

# flag = True
# while flag:
#     a, b = map(int, input().split())
#     if (a != 0 and b != 0):
#         print(a+b)
#     if (a == 0 and b == 0): 
#         flag = False
## 위의 방법보다는 아래처럼!
# while(True):
#     A, B = list(map(int, input().split()))
#     if(A == 0 and B == 0):
#         break
#     else:
#         print(A + B)

# num = int(input())
# for i in range(num):
#     a, b = map(int, input().split(','))
#     print(a+b)

# num = int(input())
# for i in range(num):
#     a, b = map(int, input().split())
#     print('Case #%s: %s' %(i+1, a+b))

# num = int(input())
# for i in range(num):
#     a, b = map(int, input().split())
#     print('Case #%d: %d + %d = %d' %(i+1, a, b, a+b))

# while True:
#     try:
#         print(input())   -> input을 변수로 쓰지 말기!! input = input() 이런거 x
#     except EOFError:
#         break

# num = int(input())
# numForSum = list(input())
# sum = 0
# for i in range(num):
#     sum += int(numForSum[i])
# print(sum)

# a = input()
# for b in range (0,len(a),10):
#     print(a[b:b+10]) 

# n = int(input())
# for i in range(1, n+1):
#     print(i)

# n = int(input())
# for i in range(n, 0, -1):
#     print(i)

# n = int(input())
# for i in range(1, 10):
#     print('%d * %d = %d' %(n, i, n*i))

## 달력 다시보기 ㅜ ㅜ 
# month, day = map(int, input().split())
# weekday = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
# lastday = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# totalDay = 0
# for i in range(0, month - 1):
#     totalDay = totalDay + lastday[i]
# print(weekday[(totalDay + day) % 7])        

# sum = 0
# num = int(input())
# for i in range(1, num + 1):
#     sum += i
# print(sum)

# num = int(input())
# numInput = map(int, input().split())
# numArray = list(numInput)
# print('%d %d'%(min(numArray), max(numArray)))

# num = int(input())
# for i in range(1, num+1):
#     print('*'*i)

# num = int(input())
# for i in range(1, num+1):
#     print(' '*(num-i) + '*'*i)

# num = int(input())
# for i in range(num, 0, -1):
#     print(' '* (num - i) + '*'*i)

# num = int(input())
# for i in range(1, num+1):
#     print(' ' *(num-i) + '*' * (2*i -1))

# num = int(input())
# num2 = num
# for i in range(1, num+1):
#     print('*'*i+' '*(2*(num-i))+'*'*i)
# for j in range(num2-1, 0, -1):
#     print('*'*j + ' '*(2*(num-j)) + '*'*j)

# num = int(input())
# for i in range(1, num+1):
#     print(' '*(num - i)+'*'*i)
# for j in range(num-1, 0, -1):
#     print(' '*(num - j)+'*'*j)

# num = int(input())
# for i in range(num, 1, -1):
#     print(' '*(num - i) + '*'*(2*i-1))
# for i in range(1, num+1):
#     print(' '*(num - i) + '*'*(2*i -1))

# num = int(input())
# for i in range(1, num+1):
#     print(' '*(num - i)+'* '*i)

# num = int(input())

# for i in range(1, num+1):
#     if (i == 1):
#         print(' '*(num-i)+'*')
#     elif i == num:
#         print('*'*(2*num-1))
#     else:
#         print(' '*(num - i)+ '*'+' '*(2*i-3)+'*')