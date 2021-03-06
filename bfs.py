queue = []

# boat = 1 esquerda
# boat = -1 direita

condicao1 = None
condicao2 = None
condicao3 = None
condicao4 = None


class Node:
    def __init__(self, key, parent): #key é uma lista com fze, afe, cre, lbe, fzd, afd, crd, lbd, boat
                                    # fazendeiro no lado esquerdo
                                    #alface no lado esquerdo
                                    #carneiro no lado esquerdo
                                    #lobo no lado esquerdo
                                    #fazendeiro no lado direito
                                    #alface no lado direito
                                    #carneiro no lado direito
                                    #lobo no lado direito
                                    #barco
        self.key = key
        self.parent = parent


def expand(s, fze, afe, cre, lbe, fzd, afd, crd, lbd, boat): #todos os casos "possiveis"
    list = []
    key = s.key
    condicao1 = solve(fze - boat, afe, cre, lbe, fzd + boat, afd, crd, lbd, -boat) #fazendeiro na direita
    if(condicao1 == True):
        child1 = Node([fze - boat, afe, cre, lbe, fzd + boat, afd, crd, lbd, -boat], s)
        list.append(child1)
    condicao2 = solve(fze - boat, afe - boat, cre, lbe, fzd + boat, afd + boat, crd, lbd, -boat) #alface e fazendeiro na direita
    if(condicao2 == True):
        child2 = Node([fze - boat, afe - boat, cre, lbe, fzd + boat, afd + boat, crd, lbd, -boat], s)
        list.append(child2)
    condicao3 = solve(fze - boat, afe, cre - boat, lbe, fzd + boat, afd, crd + boat, lbd, -boat) #fazendeiro e carneiro na direita
    if(condicao3 == True):
        child3 = Node([fze - boat, afe, cre - boat, lbe, fzd + boat, afd, crd + boat, lbd, -boat], s)
        list.append(child3)
    condicao4 = solve(fze - boat, afe, cre, lbe - boat, fzd + boat, afd, crd, lbd + boat, -boat) #lobo e fazendeiro na direita
    if(condicao4 == True):
        child4 = Node([fze - boat, afe, cre, lbe - boat, fzd + boat, afd, crd, lbd + boat, -boat], s)
        list.append(child4)

    return list


def solve(fze, afe, cre, lbe,fzd, afd, crd, lbd, boat): #encontrar solução
    if (fze < 0 or afe < 0 or cre < 0 or lbe < 0 or fzd < 0 or afd < 0 or crd < 0 or lbd < 0 or
        (cre == 1 and lbe == 0 and afe == 1 and fze == 0) or (crd == 1 and lbd == 0 and afd == 1 and fzd == 0)):
        return False #falso caso carneiro e o alface estiverem sozinhos
    else:
        if (fze < 0 or afe < 0 or cre < 0 or lbe < 0 or fzd < 0 or afd < 0 or crd < 0 or lbd < 0 or
            (lbe == 1 and cre == 1 and afe == 0 and fze == 0)or(lbd == 1 and crd == 1 and afd == 0 and fzd == 0)):
            return False #falso caso o lobo e o carneiro estiverem sozinhos
        else:
            return True


def initial_state(): #estado inicial. Fazendeiro, lobo, carneiro, alface e o barco do lado esquerdo
    return Node([1, 1, 1, 1, 0, 0, 0, 0, 1], None)


def enqueue(s): #empilhar
    global queue
    queue.append(s)


def empty_queue(): #pilha vazia
    if len(queue) == 0:
        return True
    return False


def dequeue(): #desemppilhar
    global queue
    ret = queue[0]
    del queue[0]
    return ret


def goal(s): #estado final. Fazendeiro, lobo, alface, carneiro e o barco do outro lado do rio
    if s.key == [0, 0, 0, 0, 1, 1, 1, 1, -1]:
        return True
    return False


def show_path(s): #função para apresentar o nó
    if s == None:
        return

    show_path(s.parent)
    print('%d' % (s.key[0]) ,'-', '%d' % (s.key[1]) ,'-', '%d' % (s.key[2]) ,'-', '%d' % (s.key[3]) ,'-',
        '%d' % (s.key[4]) ,'-', '%d' % (s.key[5]) ,'-', '%d' % (s.key[6]),'-', '%d' % (s.key[7]),'-',
        '%d' % (s.key[8]))


def bfs():


    s = initial_state()

    enqueue(s)

    while not empty_queue():
        s = dequeue()

        #para ver todos os estados visitados basta tirar o comentario abaixo

        '''print('Estado visitado: %d' % (s.key[0]) ,'-', '%d' % (s.key[1]) ,'-', '%d' % (s.key[2]) ,'-', '%d' % (s.key[3]) ,'-', 
        '%d' % (s.key[4]) ,'-', '%d' % (s.key[5]) ,'-', '%d' % (s.key[6]),'-', '%d' % (s.key[7]),'-', 
        '%d' % (s.key[8]))'''

        if goal(s):
            show_path(s)
            return True

        children = expand(s, s.key[0], s.key[1], s.key[2], s.key[3], s.key[4], s.key[5], s.key[6], s.key[7],
                          s.key[8])

        for child in children:
            enqueue(child)

    return False


bfs()
