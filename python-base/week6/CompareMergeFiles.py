#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#利用字符串和列表将两个通讯录文本合并为一个文本
def main():
    
    fileTele = open('TeleAddressBook.txt','rb') # 因为包含中文字符,所以使用 rb 模式读取
    fileEmail = open('EmailAddressBook.txt','rb')


    fileTele.readline() # 跳过第一行
    fileEmail.readline()
    lines1 = fileTele.readlines()
    lines2 = fileEmail.readlines()

    list1_name = []
    list1_tele = []
    list2_name = []
    list2_email = []

    for line in lines1: #获取第一个文本中的姓名和电话信息
        e = line.split()
        list1_name.append(str(e[0].decode('utf-8'))) #将文本读出的 bytes 转换为 str
        list1_tele.append(str(e[1].decode('utf-8')))
    for line in lines2: #获取第一个文本中的姓名和电话信息
        e = line.split()
        list2_name.append(str(e[0].decode('utf-8'))) #将文本读出的 bytes 转换为 str
        list2_email.append(str(e[1].decode('utf-8')))

    # 开始处理

    # 1.初始化一个空的列表
    lines = []
    lines.append('姓名\t\t    电话    \t\t  邮箱\n')
    # 2.按索引方式遍历姓名列表1
    for i in range(len(list1_name)):
        s = ""
        if list1_name[i] in list2_name:
            j = list2_name.index(list1_name[i]) #找到姓名 列表1 对应 列表2 中的姓名索引位置
            s = "\t".join([list1_name[i], list1_tele[i], list2_email[j]])
            s += "\n"
        else:
            s = "\t".join([list1_name[i], list1_tele[i], str("   -----   ")])
            s += "\n"
        lines.append(s)

    # 3.处理列表2 中剩余的姓名
    for i in range(len(list2_name)):
        s = ""
        if list2_name[i] not in list1_name:
            s = "\t".join([list2_name[i], str("   -----   "), list2_email[i]])
            s += "\n"
        lines.append(s)


    # 4.写入文件

    # 这种写入方式,打开会出现乱码情况
    # outfile = open('AddressBook.txt', 'w')
    # outfile.writelines(lines)

    outfile = open('AddressBook.txt', 'bw')
    for line in lines:
        line = line.encode('utf-8')
        outfile.write(line)

    # 5.关闭文件并输出提示信息
    fileEmail.close()
    fileTele.close()
    outfile.close()

    print("The addressBooks are merged!")

if __name__ == '__main__':
    main()