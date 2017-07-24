#！/usr/bin/env python3
# -*- coding:utf-8 -*-

def main():
    try:
        n1, n2 = eval(input("Enter two numbers, separated by a comma: "))
        result = n1/n2
    except ZeroDivisionError:
        print('Division by zero!')
    except SyntaxError:
        print('A comma may be missing in the input')
    except:
        print('something wrong in the input')
    else:
        print('No exceptions, the result is ', result)
    finally:
        print('excuting the final clause')

# program entry
main()