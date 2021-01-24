def recur(n, cur=0):
    if not isinstance(n, int) or n < 2:
        raise ValueError('Invalid input')
    return cur+1-1/n
    
    
'''

    this func add something to cur.

    Something means:
    Σ[i(i-1)]^(-1) for i=2 to n

    and it equals:

        1-n^(-1)

''''
