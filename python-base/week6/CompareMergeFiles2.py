#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def toDic(_lines):
    dic = {}
    for line in _lines: #获取第一个文本中的 姓名和邮箱 信息
        e = line.split()
        #将文本读出来的 bytes 转换为 str 类型
        dic[e[0]] = str(e[1].decode('utf-8'))
    return dic

def main():
    file1 = open('EmailAddressBook.txt', 'rb')
    file2 = open('TeleAddressBook.txt', 'rb')

    file1.readline()#跳过第一行
    file2.readline()
    lines1 = file1.readlines()
    lines2 = file2.readlines()

    dic1 = toDic(lines1) #字典方式保存
    dic2 = toDic(lines2)

    ###开始处理
    lines = []
    lines.append('姓名\t    电话   \t  邮箱\r\n')

    for key in dic1:
        s = ''
        if key in dic2.keys():
            s = '\t'.join([str(key.decode('utf-8')), dic1[key], dic2[key]])
            s += '\r\n'
        else:
            s = '\t'.join([str(key.decode('utf-8')), dic1[key], str('   -----   ')])
            s += '\r\n'
        lines.append(s)

    for key in dic2:
        s = ''
        if key not in dic1.keys():
            s = '\t'.join([str(key.decode('utf-8')), str('   -----   '), dic2[key]])
            s += '\r\n'
        lines.append(s)

    #防止出现乱码
    file3 = open('AddressBook.txt','bw')
    for line in lines:
        line = line.encode('utf-8')
        file3.write(line)

    file3.close()
    file2.close()
    file1.close()
    print('The addressBook are merged!')

if __name__ == '__main__':
    main()