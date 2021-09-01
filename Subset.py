def make_subset(A, sbst, idx):
    print(sbst) 
    lea = len(A)
    for i in range(idx, lea):
        sbst += [A[i]]
        make_subset(A, sbst, i + 1)
        sbst.pop(-1)
    return
# End make_subset

def subset(A):
    sbst = []
    idx = 0
    make_subset(A, sbst, idx)
# End subset

# Driver Code
Array = [1, 2, 3, 4]
subset(Array)
