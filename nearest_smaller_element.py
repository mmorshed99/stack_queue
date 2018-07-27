#Given an array, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than i.
#
#More formally,
#
#G[i] for an element A[i] = an element A[j] such that 
#    j is maximum possible AND 
#    j < i AND
#    A[j] < A[i]
#Elements for which no smaller element exist, consider next smaller element as -1.
#
#Example:
#
#Input : A : [4, 5, 2, 10, 8]
#Return : [-1, 4, -1, 2, 2]
#
#Example 2:
#
#Input : A : [3, 2, 1]
#Return : [-1, -1, -1]
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        stack = []
        return_arr = []
        if len(A) == 0:
            return []
        i = 1
        stack.append(A[0])
        return_arr.append(-1)
        if len(A) > 1:
            j = len(stack) - 1
            while(i<len(A)):
                if j < 0:
                    return_arr.append(-1)
                    stack.append(A[i])
                    j = len(stack) - 1
                    i = i + 1
                elif stack[j] > A[i] or stack[j] == A[i]:
                    del stack[j]
                    j = len(stack) - 1
                elif stack[j] < A[i]:
                    return_arr.append(stack[j])
                    stack.append(A[i])
                    i = i + 1
                    j = len(stack) - 1
        return return_arr
    #########Alternate###
    def prevSmaller(self, A):
        my_stack = []
        my_ret = []
        if len(A) == 0:
            return []
        for index in range(len(A)):
            if len(my_stack) == 0:
                my_ret.append(-1)
                my_stack.append(A[index])
                continue
            if A[index] > my_stack[-1]:
                my_ret.append(my_stack[-1])
                my_stack.append(A[index])
            else:
                while A[index] <= my_stack[-1]:
                    del my_stack[-1]
                    if len(my_stack) == 0:
                        my_stack.append(A[index])
                        break
                if A[index] > my_stack[-1]:
                    my_ret.append(my_stack[-1])
                    my_stack.append(A[index])
                else:
                    my_ret.append(-1)
        return my_ret
