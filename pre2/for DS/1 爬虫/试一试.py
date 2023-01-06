for i in range(0,10):
    # try里面的语句,出错了也不会终结程序
    try:
        a  = 1/i
        print("我没错"+str(i))
    # try里的语句出错了, 就会转而执行except里的语句
    except:
        print("我错了"+str(i))