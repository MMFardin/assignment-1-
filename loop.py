n=int(input("Any integer number:"))
if n%2==0 :
   m=print("It is even number")
else:
    print("It is odd number")

sum=0
for i in range(1,n+1):
    if i%2==0:
        sum+=i
print(f"Sum of even number is {sum}")
