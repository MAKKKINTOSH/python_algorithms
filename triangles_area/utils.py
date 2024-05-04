def combinations(n, k):
    comb_ls = []
    for i in range(k):
        comb_ls.append(i)
    comb_ls.append(n)
    comb_ls.append(0)
    while True:
        yield comb_ls[0:k]
        for j in range(len(comb_ls) - 1):
            if comb_ls[j] + 1 == comb_ls[j + 1]:
                comb_ls[j] = j
            else:
                break
        if j < k:
            comb_ls[j] += 1
        else:
            break
