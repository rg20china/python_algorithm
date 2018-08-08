#!/usr/bin/python
#coding:utf-8
from __future__ import print_function
import datetime

print("插入排序算法")

#原始的未排序序列
A = [5,7,9,2,4,1,8,0,3,41,53,74,98,12,45,75]

starttime = datetime.datetime.now()
# i从 第二位数字（第一位序号是0，作为第一次比较时被key比较的值）至序列最后一位之间进行循环。
for i in  range(1,len(A)):
    # key为当前i循环到所指向的值
    key = A[i]
    j = i - 1

    #  前一个的值比后一个值（当前指向到的key的值）大的时候， 把前面的值赋给后一个值 ,这时候继续向前反推，直到到了第二位数字完成比较。
    while j >=0 and A[j] > key:
        A[j+1] = A[j]
        j = j - 1

    #  如果j=-1的时候，A[j+1]=A[0]所赋给的值已经是序列中比较下来之后，最小的一个值了。
    A[j+1] = key
endtime = datetime.datetime.now()
print ((endtime - starttime).microseconds,end="微秒\n" )
print(A)