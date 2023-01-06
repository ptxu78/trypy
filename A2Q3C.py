studentList = []

# input function
def main():
    inStr = input("in:")
    while inStr != "quit":
        if inStr == '':
            print("empty")
        else:
            studentList.append(inStr)
        inStr = input("in:")


def form_3_groups(stu_list):
    class_group_list = [[], [], []]
    for stu_n in range(len(stu_list)):
        class_group_list[stu_n % 3].append(stu_list[stu_n])
        # if stu_n % 3 == 0:
        #     class_group_list[0].append(stu_list[stu_n])
        # elif stu_n % 3 == 1:
        #     class_group_list[1].append(stu_list[stu_n])
        # elif stu_n % 3 == 2:
        #     class_group_list[2].append(stu_list[stu_n])

    # for i in range(len(class_group_list)):
    #     class_group_list.remove([])
    return class_group_list

def form_groups_of_3(stu_list):
    class_group_list = []
    # stu_list[0:3]
    # stu_list[3:6]
    # stu_list[6:9]
    # stu_list[9:len(stu_list)]
    len_of_group = 3

    for i in range(0, len(stu_list) - len_of_group + 1, len_of_group):
        class_group_list.append(stu_list[i : i+len_of_group])

    if len(stu_list) % 3 != 0:
        tail = len(stu_list) % 3
        class_group_list.append(stu_list[-tail::])

    return class_group_list



main()
print(studentList)
fGroup1 = form_groups_of_3(studentList)
for G in fGroup1:
    print(G)