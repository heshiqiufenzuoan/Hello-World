def select_sort(a_list):
    """选择排序"""
    n = len(a_list)
    for j in range(n-1):
        min_index = j
        for i in range(j+1, n):
            if a_list[i] < a_list[min_index]:
                min_index = i
        if j != min_index:
            a_list[j], a_list[min_index] = a_list[min_index], a_list[j]
 
 
if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print('排序前:%s' % li)
    select_sort(li)
    print('排序后:%s' % li)
