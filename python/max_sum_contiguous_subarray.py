A = [-2,1,-3,4,-1,2,1,-5,4]

def maxSubArray(A):
        max_sum = float('-inf')
        cache = {}
        for i in xrange(len(A)):
            if i > 0:
                curr_max_sum = max(A[i] + cache[i - 1], A[i])
            else:
                curr_max_sum = A[i]
            cache[i] = curr_max_sum
            max_sum = max(max_sum, curr_max_sum)
        return max_sum

print maxSubArray(A)