# n = input()
# numbers = list(input())
# sum = 0

# for i in numbers:
#     sum = sum + int(i)

# print(sum)

# ==================================================

# n = int(input(':'))
# subject = list(map(int,input().split()))

# adjust = []
# adjustsum = 0
# max = max(subject)

# for i in subject:

#     adjust.append(i/max*100)
#     adjustsum = adjustsum + i/max*100

# print(adjustsum/n)
# print(adjust)

# ==========================================

# num,n = map(int,input(':').split())
# arr = list(map(int,input(':').split()))

# while n:
#     x,y = map(int,input(':').split())
#     print(sum(arr[x-1:y]))
#     n = n-1

# ==============================================

# n, num = map(int, input(':').split())


# arr = [[0 for j in range(n)] for i in range(n)]

# print(arr)

# for i in range(n):

#     arr[i] = list(map(int, input(':').split()))


# x1, y1, x2, y2 = map(int, input(':').split())


# sumz = 0
# for i in range(y1-1, y2):
#     sumz = sumz+sum(arr[i][x1-1:x2])


# print(sumz)

# =======================================================

# suNo, quizNo = map(int, input().split())
# numbers = list(map(int, input().split()))
# prefix_sum = [0]
# temp = 0

# for i in numbers:
#     temp = temp + i
#     prefix_sum.append(temp)

# for i in range(quizNo):
#     s, e = map(int, input().split())
#     print(prefix_sum[e] - prefix_sum[s-1])

# ======================================================

# n, m = map(int, input().split())
# A = [[0] * (n+1)]
# D = [[0] * (n+1) for _ in range(n+1)]

# print(A)
# print(D)

# for i in range(n):
#     A_row = [0] + [int(x) for x in input().split()]
#     A.append(A_row)
#     print(A)

# print(A)

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]


# for _ in range(m):
#     x1, y1, x2, y2 = map(int, input().split())

#     result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
#     print(result)

# ======================================

# n = int(input())
# count = 1
# start_index = 1
# end_index = 1
# sum = 1

# while end_index != n:
#     if sum == n:
#         count += 1
#         end_index += 1
#         sum += end_index
#     elif sum > n:
#         sum -= start_index
#         start_index += 1
#     else:
#         end_index += 1
#         sum += end_index

#     print("start_index :",start_index,"end index :", end_index)
#     print("count",count)
#     print('sum', sum)
#     print('')

# print(count)

# ============================================

# N = int(input())
# M = int(input())
# A = list(map(int, input().split()))
# A.sort()
# count = 0
# i = 0
# j = N - 1

# print(A)
# while i < j:
#     if A[i] + A[j] < M:
#         i += 1
#     elif A[i] + A[j] > M:
#         j -= 1
#     else:
#         count += 1
#         i += 1
#         j -= 1

#     print('i :', i, 'A[i]',A[i] )
#     print('j :', j, 'A[j]', A[j] )
#     print('count: ', count)

# print('답 :',count)

# ===========================================

# N = int(input())
# Result = 0
# A = list(map(int, input().split()))
# A.sort()

# for k in range(N):
#     find = A[k]

#     i = 0
#     j = N -1

#     while i < j:
#         print('find', find)
#         print('i', i, 'A[i]', A[i])
#         print('j', j, 'A[j]', A[j])

#         if A[i] + A[j] == find:
#             if i != k and j != k:
#                 Result += 1
#                 break

#             elif i == k:
#                 i += 1
#                 print('i == k')

#             elif j == k:
#                 j -= 1
#                 print('j == k')

#         elif A[i] + A[j] < find:
#             i += 1

#         else:
#             j -= 1

#         print('Result', Result)
#         print()
#     print()
# print(Result)

# =========================================

# checkList = [0] * 4
# myList = [0] * 4
# checkSecret = 0

# def myadd(c):
#     global checkList, myList, checkSecret
#     if c == 'A':
#         myList[0] += 1
#         if myList[0] == checkList[0]:
#             checkSecret += 1

#     elif c == 'C':
#         myList[1] += 1
#         if myList[1] == checkList[1]:
#             checkSecret += 1

#     elif c =='G':
#         myList[2] += 1
#         if myList[2] == checkList[2]:
#             checkSecret += 1

#     elif c =='T':
#         myList[3] += 1
#         if myList[3] == checkList[3]:
#             checkSecret += 1

# def myremove(c):
#     global checkList, myList, checkSecret
#     if c == 'A':

#         if myList[0] == checkList[0]:
#             checkSecret -= 1
#         myList[0] -= 1

#     elif c == 'C':

#         if myList[1] == checkList[1]:
#             checkSecret -= 1
#         myList[1] -= 19

#     elif c =='G':

#         if myList[2] == checkList[2]:
#             checkSecret -= 1
#         myList[2] -= 1

#     elif c =='T':

#         if myList[3] == checkList[3]:
#             checkSecret -= 1
#         myList[3] -= 1


# S, P = map(int, input().split()) #문자열의 길이, 부분문자열의 길이
# Result = 0
# A = list(input())
# checkList = list(map(int, input().split()))

# for i in range(4):
#     if checkList[i] == 0:
#         checkSecret += 1

# for i in range(P):
#     myadd(A[i])

# if checkSecret == 4:
#     Result += 1

# for i in range(P,S):#부분문자열의 길이~ 문자열의 길이,
#     print('P,S :',P,S)
#     j = i - P
#     print('i :', i)
#     print('j :', j)


#     print(A)

#     print('myadd :',A[i])

#     myadd(A[i])

#     print('myremove :',A[j])
#     myremove(A[j])
#     if checkSecret == 4:
#         Result += 1

# print(Result)

# (011)========================================

# N = int(input())
# inputNum = [0]*N

# for i in range(N):
#     inputNum[i] = int(input())

# stack = []
# count = 1
# result = True
# answer = ""

# for i in range(N):

#     if inputNum[i] >= count:
#         while inputNum[i] >= count:
#             stack.append(count)
#             count += 1
#             answer += "+\n"


#         stack.pop()
#         answer += "-\n"

#     else:

#         if stack[-1] != inputNum[i]:
#             print("NO")
#             result = False
#             break
#         else:
#             answer += "-\n"
#             stack.pop()

#     print('count',count)
#     print('i',i)
#     print('A[i]',inputNum[i])
#     print('answer\n',answer)
#     print('스택',stack)
#     print(i,'번째 루프')
#     print('===================')

# if result:

#     print(answer)

#(012)===================================================

# n = int(input())
# ans = [0] *n
# inputNum = list(map(int,input().split()))
# indexStack = []

# for i in range(n):
    
#     while indexStack and inputNum[indexStack[-1]] < inputNum[i]:

#         ans[indexStack.pop()] = inputNum[i]

        
#     indexStack.append(i)

    
# while indexStack:
#     ans[indexStack.pop()] = -1
    
# result = ""

# for i in range(n):
#     result += str(ans[i])+" "

# print(result)

#(013)======================================

# from collections import deque
# N = int(input())
# myQueue = deque()

# for i in range(1,N+1):
#     myQueue.append(i)

# while len(myQueue) > 1 :
#     myQueue.popleft()
#     myQueue.append(myQueue.popleft())

# print(myQueue[0])




