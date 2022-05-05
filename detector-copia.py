import re


def n_palavras_unicas(lista_palavras):
    # Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    # Recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def separa_sentencas(texto):
    # A funcao recebe um texto e devolve uma lista das sentencas dentro do texto
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]

    return sentencas


def separa_frases(sentenca):
    # A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    # A funcao recebe uma frase e devolve uma lista das palavras dentro da frase
    return frase.split()


def retira_frases(texto):
    # Retira frases de um texto

    # Transforma as setenças em frases
    setencas = separa_sentencas(texto)
    frases = []
    for i in range(len(setencas)):

        if len(separa_frases(setencas[i])) == 1:
            frases.append(separa_frases(setencas[i]))
        else:
            for item in separa_frases(setencas[i]):
                frases.append(item)

    # Tratamento para retirar as listas que sao geradas acima
    for i in range(len(frases)):

        if not frases[i][0] == ' ':
            frases[i] = frases[i][0]

    return frases


def retira_palavras(texto):
    # Retira as palavras de um texto

    frases = retira_frases(texto)

    # Transforma as frases em palavras
    palavras = []
    for i in range(len(frases)):
        for item in separa_palavras(frases[i]):
            palavras.append(item)

    return palavras


def tmn_md_palavra(texto):
    palavras = retira_palavras(texto)

    # Calcula o tamanho medio das palavras
    media = 0

    for i in range(len(palavras)):
        media = media + len(palavras[i])

    media = media / len(palavras)

    return media


def tmn_md_setenca(texto):
    # Média simples do número de caracteres por sentença.

    qtd_sentecas = len(separa_sentencas(texto))

    setencas = separa_sentencas(texto)
    count = 0

    for i in setencas:
        count = count + len(i)

    media = count / qtd_sentecas

    return media


def tmn_md_frase(texto):
    # Média simples do número de caracteres por frase.
    setencas = separa_sentencas(texto)

    # Retira as frases do texto
    frases = []
    for i in setencas:
        frases.append(retira_frases(i))

    # Calcula a quantidade de caracteres
    caracteres = 0

    for i in range(len(frases)):
        aux = len(frases[i])

        for item in range(aux):
            caracteres = caracteres + len(frases[i][item])

    # Calcula a quantidade de frases
    qtd_frases = 0
    for i in range(len(frases)):
        qtd_frases = qtd_frases + len(frases[i])

    media = caracteres / qtd_frases

    return media


def complexidade_setenca(texto):
    # Média simples do número de frases por sentença.

    tamanho_sentenca = len(separa_sentencas(texto))

    frases = []
    setencas = separa_sentencas(texto)

    for i in range(len(setencas)):
        frases.append(separa_frases(setencas[i]))

    tamanho_frase = len(retira_frases(texto))

    complexidade = tamanho_frase / tamanho_sentenca

    return complexidade


def hapax_leogama(texto):
    #Número de palavras utilizadas uma única vez dividido pelo número total de palavras.

    lista_palavras = retira_palavras(texto)

    total_palavras = len(lista_palavras)

    palavras_diferentes = n_palavras_unicas(lista_palavras)

    typetoken = palavras_diferentes / total_palavras

    return typetoken


def type_token(texto):
    #  Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras.

    lista_palavras = retira_palavras(texto)

    total_palavras = len(lista_palavras)

    palavras_unicas = n_palavras_diferentes(lista_palavras)

    hapaxleogama = palavras_unicas / total_palavras

    return hapaxleogama


def calcula_assinatura(texto):
    # Essa funcao recebe um texto e deve devolver a assinatura do texto.

    assinatura = [tmn_md_palavra(texto), type_token(texto), hapax_leogama(texto),
                  tmn_md_setenca(texto), complexidade_setenca(texto), tmn_md_frase(texto)]

    return assinatura


def le_assinatura():
    # A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos
    # fornecidos
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:", end="\n \n")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))
    print("\n")

    return [wal, ttr, hlr, sal, sac, pal]


def compara_assinatura(as_a, as_b):
    # Recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.

    aux = []

    for i in range(5):
        aux.append(as_a[i] - as_b[i])

    for i in range(5):
        aux[i] = abs(aux[i])

    x = 0

    for i in range(5):
        x = x + aux[i]

    similaridade = x / 6

    return similaridade


def avalia_textos(textos, ass_cp):
    # Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do
    # texto com maior probabilidade de ter sido infectado por COH-PIAH.

    texto = 0
    provavel = compara_assinatura(ass_cp, calcula_assinatura(textos[0]))

    for i in range(len(textos)):
        assinatura = calcula_assinatura(textos[i])
        aux = compara_assinatura(ass_cp, assinatura)

        if aux <= provavel:
            provavel = aux
            texto = i

    texto = texto + 1

    return texto
