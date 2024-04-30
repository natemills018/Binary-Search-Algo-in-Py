def binary_search(lst, a);
    l = 0
    r = len(ls1) -1

    while l <= r:
        m = (l + r) // 2

        if a > lst[m]:
            l = m + 1
        elif a < lst[m]:
            r = m - 1
        else 
            return True
    return False