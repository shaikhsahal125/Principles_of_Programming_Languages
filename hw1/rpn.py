def calculate(list, opr):

    if list is not None:
        if opr is "~":
            num = list.pop(0)
            result = (-num)
            list.insert(0, result)
            print(list[0])
            return
        if len(list) >= 2:
            if opr is "+":
                num1 = list.pop(0)
                num2 = list.pop(0)
                result = num2 + num1
                list.insert(0, result)
                print(list[0])
                return
            elif opr is "-":
                num1 = list.pop(0)
                num2 = list.pop(0)
                result = num2 - num1
                list.insert(0, result)
                print(list[0])
                return
            elif opr is "*":
                num1 = list.pop(0)
                num2 = list.pop(0)
                result = num2 * num1
                list.insert(0, result)
                print(list[0])
                return
            elif opr is "/":
                num1 = list.pop(0)
                num2 = list.pop(0)
                if num1 is 0:
                    print("error: division by zero")
                    list.insert(0, num2)
                    list.insert(0, num1)
                    return
                else:
                    result = num2 / num1
                    list.insert(0, result)
                    print(list[0])
                    return
        else:
            print("invalid operation")


list = []
try:
    while True:
        i = input()
        if ((i is "+") or (i is "-") or (i is "*") or (i is "/") or (i is "~")):
            calculate(list, i)
        else: 
            list.insert(0, int(i))
            print(list[0])
            
except:
    pass

