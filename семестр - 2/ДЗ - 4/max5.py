def max_sequence(seq):
    """
    Функция ищет пять соседних элементов списка, сумма значений которых максимальна.

    >>> max_sequence([1, 3, 1, 1, 4, 4, 3, 1, 4, 4, 4, 3, 4, 4, 1, 3, 2, 4, 4, 4])
    [4, 4, 4, 3, 4]

    >>> max_sequence([1, 5, 7, 2, 9, 2, 9, 2, 5, 3, 7, 6, 3, 3, 7, 4, 4, 1, 9, 5])
    [7, 2, 9, 2, 9]
    """

    list0fsums=[sum(seq[i-5:i]) for i in range(5,len(seq)+1)]
    i=list0fsums.index(max(list0fsums))
    return seq[i:i+5]
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()
