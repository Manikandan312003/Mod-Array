def modArray(arr,mod):
    sum,po=0,1
    arr=arr[::-1]
    for i in range(len(arr)):
        sum=(sum+arr[i]%mod*(po))%mod
        po=po*10%mod
    return sum

arr=list(map(int,input().split()))
mod=input()
print(modArray(arr,int(mod)))