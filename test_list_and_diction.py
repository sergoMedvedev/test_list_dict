#                             ДЛЯ ЛЮБОГО ЧИСЛА n


list = []
a = 0
# while a<100:                      задание 1  [1, 1, 1, ...] в
#   list.append('1')
#  a+=1


# while a<100:                      задание 2  [1, 0, 1, 0, 1, ...]
#   list.append('1')
#   list.append('0')
#  a+=2


# mlist=[]                             зададние 3  [[1, 2], [3, 4], ...]
# for i in range(0,100,2):
#   print(i)
#  while a<100:
#    print(i)
#   mlist.append(i)
# mlist.append(i+1)
# list.append(mlist)
# mlist=[]
# a+=2
# break

# на 4 задание нет пока что идей  [[[[[..[1]...]]]







#                                      ИЗМЕНЕНИЕ СПИСКА

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#  Поменять местами соседние элементы

# for i in range(len(list1)):
#   if i != len(list1) - 1:
#      list1[i], list1[i + 1] = list1[i + 1], list1[i]
# else:
#    list1[i], list1[0] = list1[0], list1[i]


# Отразить список зеркально ( [n, n -1, n -2, ... 3, 2, 1] )

# out=[]
# for i in range(len(list1)-1,-1,-1):
#    out.append(list1[i])
# list1=out

# Оставить только элементы сумма индекса и значений которых делится на 5
#out=[]
#for i in range(len(list1)):
 #   if (i + list1[i]) == 0:
#     continue
#  elif ((i + list1[i]) // 5) == 0:
 #       out.append(list1[i])
#list1=out



# 4. Отсортировать по количеству делителей
#summ=0
#diction={}
#for i in list1:
#   summ=0
#   for m in range(1, i + 1):
#        if i % m == 0:
#            summ+=1
#            diction[i]=summ
#
#print(sorted(diction))

#Превратить в [[1], [2, 3], [4, 5, 6], ....]
# пока что не могу дойти


print(list1)

#                                         СЛОВАРИ
# Сгенерировать словарь { '1': 1, '2': 2, '3': 3, ... }
#n=100
#dictionary={}
#for i in range(1,n+1):
#    dictionary[i]=i
#print(dictionary)



#  Реализовать функцию, которая принимает на вход лист произвольных объектов. возвр {тип : количество этого типа }
#def transfotm(list):
#   out={}
#   for i in list:
#       if type(i) in out:
#           out[type(i)]+=1
#       else:
#           out[type(i)]=1
#   print(out)

#transfotm([1,2.5,'fg',7,18,[1,2]])

# Написать функцию, которая меняет ключи и значения для произвольного словаря местами.
#diction={'sam':3,
#         'mick':6,
#         'nike':12,
#         14:12,
#         'ret':3}
#out={}
#dont_append={}
#for i in diction.keys():
#    if i in out.keys():
#        dont_append[diction[i]]=i
#    else:
#        out[diction[i]]=i
#
#print(out)
#print(dont_append)

#Реализовать красивый вывод словаря в консоль
diction={'sam':3,
         'mick':6,
         'nike':12,
         14:12,
         'ret':3}




