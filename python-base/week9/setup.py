from distutils.core import setup
import py2exe

# 将 9.sched.py 打包成 .exe文件
setup(console=['test.py'])
# 执行后当前目录下会生成 __pycache__ 和 dist 两个目录
# __pycache__ 为临时文件,可删去
# dist 为test.py 的exe文件, 可运行在 其它不包含python运行环境的操作系统上