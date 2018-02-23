#!/usr/bin/env python
def get_num():
    num_list = []
    num = ''
    while num !='!':
        num = input('input some numbers, end with "!":\n>>>').strip()
        if num !='!':
            try:
                num = float(num)
                if len(num_list) == 0:
                    num_list.append(num)
                else:
                    for i in range(len(num_list),0,-1):
                        if num > num_list[i-1]:
                            num_list.insert(i,num)
                            break
                        elif i == 0:
                            if num < num_list[0]:
                                num_list.insert(0,num)
            except:
                print('wrong number,try again')
            
                
        else:
            break
    return num_list


print(get_num())
    