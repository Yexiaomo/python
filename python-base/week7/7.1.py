#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''找到GPA最高的学生'''

class Student:
    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)
    def getName(self):
        return self.name
    def getHours(self):
        return self.hours
    def getQpoints(self):
        return self.qpoints
    def gpa(self):
        return self.qpoints / self.hours
def makeStudent(infoStr):
    name, hours, qpoints = infoStr.split('\t')
    return Student(name, hours, qpoints)
def main():
    # 打开数据文件

    infile = open('students.data', 'r')
    #设置文件中第一个学生的记录为 best
    best = makeStudent(infile.readline())
    #处理剩余行 数据
    for line in infile:
        s = makeStudent(line)
        if s.gpa() > best.gpa():
            best = s
    infile.close()

    #打印GPA成绩最高的学生信息
    print('The best syudent is:', best.name)
    print('hours:', best.getHours())
    print('GPA:', best.gpa())

if __name__ == '__main__':
    main()