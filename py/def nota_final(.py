def nota_final(
        cp11, cp21, cp31, sp1, sp2, gs1,
        cp12, cp22, cp32, sp3, sp4, gs2):
    
    cp1 = [cp11, cp21, cp31]
    cp2 = [cp12, cp22, cp32]

    cp1.sort(reverse=True)
    cp2.sort(reverse=True)

    s1 = cp1[0] * .1 + cp1[1] * .1 + sp1 * .1 + sp2 * .1 + gs1 * .6
    s2 = cp2[0] * .1 + cp1[1] * .1 + sp1 * .1 + sp2 * .1 + gs1 * .6

    return s1 * .4 + s2 * .6