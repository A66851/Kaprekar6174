import sys


def kaprekar(n):
    chiffres = list(n)
    tri_croissant = sorted(chiffres, reverse=False)
    tri_decroissant = sorted(chiffres, reverse=True)
    plus_grand = int(''.join(tri_decroissant))
    plus_petit = int(''.join(tri_croissant))
    kaprekar_n = plus_grand - plus_petit
    print('%4s - %4s = %4s' % (plus_grand , plus_petit, kaprekar_n))
    return str(kaprekar_n)


if __name__ == '__main__':
    n = input('Saisir un nombre de 4 chiffres pas tous égaux : \n')
    while True:
        kaprekar_n = kaprekar(n)
        if (n == kaprekar_n):
            break
        n = kaprekar_n
