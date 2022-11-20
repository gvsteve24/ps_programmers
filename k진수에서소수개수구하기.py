import math
def solution(n, k):
    
    tmp=n

    n_string=''
    while tmp:
        tmp,new=divmod(tmp,k)
        n_string=str(new)+n_string
    num_list=sorted([int(num) for num in n_string.split('0') if not num==''],reverse=True)

#     arr=[False,False]
#     n=max(num_list[0],1)
#     arr=arr+[True]*(n+1-len(arr))

#     for i in range(2, n + 1):
#         if arr[i] == True:
#             j = 2
#             while (i * j) <= n:
#                 arr[i*j] = False
#                 j += 1
    

#     cnt=0
#     for num in num_list:
#         if arr[num]:
#             cnt+=1


    def is_prime(x):
        if x == 1:
            return False
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True
    
    cnt=0
    for num in num_list:
        if is_prime(num):
            cnt+=1

    return cnt
