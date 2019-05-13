temp = input("请输入1到100之间的数字：")
while True:
    if not temp.isdigit():
        print("输入不合法，请重新输入：")
        temp = input()
    else:
        temp = int(temp)
        if temp > 100:
            print("你大爷好丑")
        else:
            print("你妹好漂亮")
        break
