#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Draw Tree

from turtle import Turtle, mainloop

# 递归画树
def tree(plist, l, a, f):
    '''
    plist is list of pens
    a is half of the angle between 2 branches
    f is factor by which branch is shortened
    from level to level '''

    if l>5:
        lst = []
        for p in plist:
            p.forward(l) #沿着当前方向画画
            q = p.clone()
            p.left(a)
            q.right(a)
            lst.append(p)# 将元素追加到列表最后
            lst.append(q)
        tree(lst, l*f, a, f)

def main():
    p = Turtle()
    p.color('green')
    p.pensize(5)

    p.hideturtle()

    p.speed(30)

    p.left(90)

    p.penup()

    p.goto(0, -200)

    p.pendown()

    t = tree([p], 200, 65, 0.6375)

main()