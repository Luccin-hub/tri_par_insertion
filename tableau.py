def tri(A):
    n=len(A)
    for i in range (n):
        for j in range (n):
            if A[i] >= A[j] and i <= j:
                A[i] , A[j] = A[j] , A[i]
    return A
B = [ 3, 2, 5, 4, 1]
print(tri(B))

# https://www.loom.com/share/0f8d453a92d34b8f8300da79edadcc50
#video
