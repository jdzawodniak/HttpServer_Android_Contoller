################################
##Generated with a lot of love##
##    with   EasyPython       ##
##Web site: easycoding.tn     ##
################################

x = None
y = None
list2 = None
i = None


x = 'item1=1,item2=2,item3=33,item4=444,item5=done'
y = x.split(',')
list2 = x.split(',')
for i in range(1, 6):
  print(i)
  print(list2[int(i - 1)])
