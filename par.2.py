s=0
ctd=0
for x in range (1,7,):
    n=int(input('digite um valor  '))
    if x%2==0:
        s+=n
        ctd+=1
print('{} números são pares e a soma deles é: {}'.format(ctd, s))

        