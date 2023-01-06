import os


def readdata(fname):
    f = open(fname, 'r')
    data_list = f.readlines()
    for i in range(len(data_list)):
        data_list[i] = data_list[i].replace('\n', '')
        if i % 2 == 0:
            print("student name: ", data_list[i])
        else:
            print("performance in exam: ", data_list[i])

    ave_mark = 0
    for i in range(1, len(data_list), 2):
        data_list[i] = float(data_list[i])
        ave_mark = ave_mark + data_list[i]
    ave_mark = ave_mark / len(data_list) * 2
    ave_mark_1 = '%.2f'%ave_mark
    print("ave: ", ave_mark_1)




def main():
    while(True):
        filename = input("readName?")
        if os.path.exists(filename):
            readdata(filename)
            break
        else:
            print("file not found\n")


if __name__ == '__main__':
    main()