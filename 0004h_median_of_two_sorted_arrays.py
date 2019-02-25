class Solution:
    def findMedianSortedArrays(self, A, B):
        M, N = len(A), len(B)
        index = 0
        curr, med1, med2 = 0, 0, 0 

        i, j = 0, 0

        while i < M or j < N:
            if j >= N or (i < M and A[i] <= B[j]):
                curr = A[i]
                i += 1
            elif i >= M or (j < N and A[i] >= B[j]):
                curr = B[j]
                j += 1

            if index == (M + N) // 2 - 1:
                med1 = curr
            elif index == (M + N) // 2:
                med2 = curr
                break

            index += 1

        if (M + N) % 2 == 0:
            return (med1 + med2)/2.0
        else:
            return med2
