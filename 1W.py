def writedata(fname):
    f = open(fname, 'w')
    item_num = int(input("how many items? "))
    for i in range(item_num):
        print("student", i+1)
        stu_name = input("\tStudent Name:")
        mark = input("\tMark for exam:")
        f.write(stu_name)
        f.write('\n')
        f.write(mark)
        if i < item_num - 1:
            f.write('\n')
    print("Student completed!")
    f.close()

def main():
    file_name = input("namePlease:")
    writedata(file_name)

if __name__ == '__main__':
    main()


