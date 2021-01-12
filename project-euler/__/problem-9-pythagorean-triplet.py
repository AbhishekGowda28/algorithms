def problem9():
    limit = 1000
    c = 0
    m = 2
    while c < limit:
        for n in range(1, m):
            a = m*m-n*n
            b = 2*m*n
            c = m*m+n*n
            if c > limit:
                break
            if a + b + c == 1000:
                return a*b*c
        m += 1


print(problem9())
