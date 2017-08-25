#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''python
### sched库(程序定时执行)-->用来进行任务调度
sched.scheduler() 用来创建一个 调度任务
scheduler.enter(delay, priority, action, argument=()) 创建一个调度事件, argument 中时action() 的 参数部分
scheduler.run() 运行调度任务中的全部调度事件
scheduler.cancel(event) 取消某个调度事件
'''
import sched, time
def printTime(msg = 'default'):
    print("当前时间", time.time(), msg)

s = sched.scheduler(time.time, time.sleep)
print(time.time())
s.enter(4, 1, printTime, argument=("延迟4秒, 优先级1",))
'''四个参数分别是:
1.间隔事件(具体值决定与delayfunc, 这里为秒);
2.优先级(两个事件在同一时间到达的情况);
3.触发的函数;
4.函数参数；'''
s.enter(2, 2, printTime, argument=("延迟2秒, 优先级2",))
s.enter(2, 1, printTime, argument=("延迟2秒, 优先级1",))
s.run()
print(time.time())