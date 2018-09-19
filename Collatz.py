#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------


def collatz_read(s):
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------


def collatz_eval(i, j):
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """


    assert 0 < i < 1000000
    assert 0 < j < 1000000

    a = min(i,j)
    b = max(i,j)

    max_val = 0
    cache = {}
    #create initial cache
    for num in range(1,b+1):
	    c = 1
	    n = num
	    if num in cache.keys():
	        	continue
	    while n > 1:
	        if (n % 2) == 0 :
	            n = (n // 2)
	        else :
	            n = (3 * n) + 1
	        c += 1
	        if n in cache.keys():
	        	c += cache[n] - 1
	        	break
	    cache[num] = c
    
    
    #find actual
    max_val = 0
    for i in range(a,b+1):
    	if cache[i] > max_val:
    		max_val = cache[i]
    return max_val
    	

# -------------
# collatz_print
# -------------


def collatz_print(w, i, j, v):
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------


def collatz_solve(r, w):
    """
    r a reader
    w a writer
    """
    for s in r:
        i, j = collatz_read(s)
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)
