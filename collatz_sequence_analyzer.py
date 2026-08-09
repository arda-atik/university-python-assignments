# Read inputs
n = int(input())
k = int(input())

X = -1
Y = 0
Z = -1

if n >= 1:
    while True:
        # Update the largest odd number
        if n % 2 == 1 and n > X:
            X = n
            
        # Count terms in interval [10, 100)
        if 10 <= n < 100:
            Y = Y + 1
            
        # Find the k-th even number
        if n % 2 == 0 and Z == -1:
            if k > 0:
                k = k - 1
                if k == 0:
                    Z = n
                    
        # Terminate if the sequence reaches 1
        if n == 1:
            break
            
        # DÜZELTME: Sonsuz döngüyü engellemek için n = n // 2 yapıldı.
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
            
print(X, Y, Z)
