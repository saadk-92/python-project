#print prime numbers upto 100
p = 2
while p<=100:
    is_prime=True
    for i in range(2,p):
     if p%i == 0:
         is_prime = False
         continue
    if is_prime==True:
        print(p)
    p=p+1
