def writter(funci):
    def wrapped(*args, **kwargs):
        result = funci(*args, **kwargs)
        result=str(result)
        way=f'C:\\for_python\\{funci.__name__}.txt'
        file=open(way,'w')
        file.write(result)
        file.close()
        print(f'Результат функции {funci.__name__} c аргументами: {args}, {kwargs} был записан по пути: {way}')
    return wrapped
    

