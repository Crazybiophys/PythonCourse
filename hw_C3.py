your_string=input('Напишите любую строчку... \n')
your_string=your_string+'.'
slova=[]
slovo=''
for i in range(len(your_string)):
    if your_string[i]!=' ' and your_string[i]!=',' and your_string[i]!='.' and your_string[i]!=';'and your_string[i]!=':'and your_string[i]!='!' and your_string[i]!='?':
        slovo+=your_string[i]
        continue
    else:
        if slovo!='':
            slova.append(slovo)
        slovo=''
        continue
  
    
min_dlina=len(slova[0])
min_slovo=[slova[0]]
for sl in slova[1:]:
    if len(sl)<min_dlina:
        min_dlina=len(sl)
        min_slovo=[sl]
    elif len(sl)==min_dlina:
        min_slovo.append(sl)
        
print('Слово с наименьшей длиной содержит ',min_dlina,' символов. Это словa/слово ',min_slovo)

        



        
