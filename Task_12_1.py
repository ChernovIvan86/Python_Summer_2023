            # Task_12_1
# создайте функцию, которая принимает на вход список X и возвращает два:
    # список индексов элементов равных минимальному значению списка X;
    # список индексов элементов равных максимальному значению списка X;
# Например: Ввод X=[1,2,3,4,5,1,5], Вывод [0,5], [4,6]
#
def max_min_in_list(list):
#    X=[1,2,3,4,5,1,5]
    ma=max(X)
    mi=min(X)

    out_ma=[]
    out_mi=[]

    for i in range(0, len(X)):
        if X[i] == ma : out_ma.append(i)
        elif X[i] == mi : out_mi.append(i)
    return print(' max знач. списка ', ma, '\n',
                 'min знач. списка ',mi,'\n',
                 'список инд. max эл. ', out_ma,'\n',
                 'список инд. min эл. ',out_mi)

X=(input('Введите СПИСОК в формате 1,2,3,4,5,1,5: ').split(','))

max_min=max_min_in_list(X)

