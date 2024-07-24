#//Armstrong 
n=int(input())
t=n
sum=0
a=len(n)
n=int(n)
while n!=0:
  d=d%10
  sum+=d**a
  n=n/10
if sum==t:
  print("Armstrong")
else:
  print("not a Armstrong")
 
#//sum of n natural numbers
n=int(input())
sum=0
for i in range (0,n+1):
  sum+=i
print(sum)

