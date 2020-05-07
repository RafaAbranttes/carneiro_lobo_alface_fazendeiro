limit = 0
#Levar o fazendeiro, carneiro, alface e o lobo para o outro lado do rio, porém,
#lobo e carneiro nao podem ficar sozinhos e o carneiro e o alface juntos
#boat == -1 means boat on the right
#boat == 1 means boat on the left
def solve(fze, afe, cre, lbe, fzd, afd, crd, lbd, boat, depth):
    if (                                                    #caso 1 carneiro e alface juntos (sozinhos)
        lbe < 0 or
        lbd < 0 or
        afe < 0 or
        afd < 0 or
        fze < 0 or
        fzd < 0 or
        cre < 0 or
        crd < 0 or
        (cre == 1 and lbe == 0 and afe == 1 and fze == 0) or
        (crd == 1 and lbd == 0 and afd == 1 and fzd == 0) or
        depth > limit
    ):
        return False

    if(                                             #caso lobo e carneiro nao podem ficar sozinhos
        lbe < 0 or
        lbd < 0 or
        afe < 0 or
        afd < 0 or
        fze < 0 or
        fzd < 0 or
        cre < 0 or
        crd < 0 or
        (lbe == 1 and cre == 1 and afe == 0 and fze == 0)or
        (lbd == 1 and crd == 1 and afd == 0 and fzd == 0) or
        depth > limit
    ):
        return False

    if(
        fze == 0 and
        afe == 0 and
        cre == 0 and
        lbe == 0 and
        fzd == 1 and
        afd == 1 and
        crd == 1 and
        lbd == 1
    ):
        print (fze, '-', afe, '-', cre, '-', lbe, '-', fzd, '-', afd, '-', crd, '-', lbd, '-', boat) #mostrar estado
        return True

    if(
        solve(fze - boat, afe, cre, lbe, fzd + boat, afd, crd, lbd, -boat ,depth + 1) or
        solve(fze - boat, afe - boat, cre, lbe, fzd + boat, afd + boat, crd, lbd, -boat, depth + 1) or
        solve(fze - boat, afe, cre - boat, lbe, fzd + boat, afd, crd + boat, lbd, -boat, depth + 1) or
        solve(fze - boat, afe, cre, lbe - boat, fzd + boat, afd, crd, lbd + boat, -boat, depth + 1)
    ):
        print (fze, '-', afe, '-', cre, '-', lbe, '-', fzd, '-', afd, '-', crd, '-', lbd, '-', boat)
        return True

    return False

while True:
    result = solve(1, 1, 1, 1, 0, 0, 0, 0, 1, 0)
    if result: break
    limit = limit + 1
