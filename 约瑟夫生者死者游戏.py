people={} #创建空字典
for x in range(1,31): #通过遍历装载KEY，并将所有的VALUE赋值为1
    people[x]=1
check=0 #报数变量
i=1 #KEY循环变量
j=0 #下船计数
while i<=31: #定义循环区间
    if i == 31: #当i累加到31，即循环重新开始，重置该变量为1
        i=1
    elif j == 15: #当下船人数累加到15人，终止
        break
    else:
        if people[i] == 0: #KEY对应的值为0，即已下船，计数并继续下一循环
            i+=1
            continue
        else: #在未下船的人员中判断
            check+=1 #报数开始并累加
            if check == 9: #当第9个出现
                people[i]=0 #将对应KEY的VALUE赋值为0
                check = 0 #重置报数
                print("{}号被扔下船了".format(i))
                j+=1 #下船计数
            else: #下船计数不为9时计数并继续循环判断
                i+=1
                continue

# 方法2
lst = list(range(1,31))  #创建30人的列表
j=1  #报数，从1-9循环
k=0  #被丢下的人的号数，从1-30循环，如果一轮报完人数还是大于15人，号数归零进行第二轮
while True:
    if len(lst) > 15:  #如果人数大于15人，进行下面判断
        if j == 9:    #如果报到9 ，则从队伍（列表）中移除，被扔下船
            print('{:<2d}号被抛下船了'.format(lst[k]))
            lst.remove(lst[k])
            j = 1  #后面一位从1开始重新报
        else:  #如果没有报到9，继续报
            j += 1
            k += 1
        if len(lst) == k:  #如果一轮报完人数还是大于15人，号数归零进行第二轮
            k = 0
    else:    #如果人数小于等于15人，游戏结束
        break