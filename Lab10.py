import random

def main():
    print("dict is:")
    a_dict = dict()
    # a_dict[5] = "hahaha"
    for i in range(1, 10+1):
        a_dict[i] = i * i * i
        # a_dict.setdefault(i, i**3)
    print(a_dict)


if __name__ == '__main__':
    main()