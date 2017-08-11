#!/sur/bin/python
#coding=utf-8
#错误类型
def div(a, b):
    try:
        c = a / b
        print c


    except ZeroDivisionError:
        return "zero can not be division"
    except TypeError:
        return "Please input the right num"
#


# def div(a, b):
#     try:
#         return a / b
    # except (ZeroDivisionError, TypeError):      #不加括号只能识别第一个错误类型
    #     return "division error or type error"

    else:
        print "else~~~~~~~~~~~~~~~"

    finally:
        print "finally>>>>>>>>>>>>>>>"
    return c



result2 = div(3, 1)
print result2
result = div(3, 'a')
print result
result1 = div(3, 0)
print result1
