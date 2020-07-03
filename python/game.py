a1_name = 'A'
a2_name = 'B'
a3_name = 'C'

b1_name = 'D'
b2_name = 'C'
b3_name = 'E'

sum = 100

def limit_1(name):
    global sum
    data = int(input("请 " + str(name) + " 输入你想取的硬币数量："))
    while data < 0 or data >30:
        print("数量错误，仅可输入1~30之间的数!")
        data = int(input("请重新输入："))
    sum = sum - data    #更新剩余硬币总数
    print("剩余硬币数为：" + repr(sum))
    return sum


#第一人
limit_1(a1_name)

#第二人
limit_1(a2_name)

#第三人
limit_1(a3_name)

def limit_2(name):
    global sum
    data = int(input("请 " + str(name) + " 输入你想取的硬币数量："))
    while data < 0 or data >30:
        print("数量错误，仅可输入1~30之间的数!")
        data = int(input("请重新输入："))
    while sum < data:
        print("数量错误，剩余硬币数不足!")
        data = int(input("请重新输入："))
    sum = sum - data
    print("剩余硬币数为：" + repr(sum))

#第四人
limit_2(b1_name)

#第五人
limit_2(b2_name)

#第六人
limit_2(b3_name)
