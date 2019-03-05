def insertion_sort(random_list):
    print("unsorted list", random_list)
    for i in range(1,len(random_list)):
        key = random_list[i]
        j =  i - 1
        while j >= 0 and random_list[j] > key:
            random_list[j + 1] = random_list[j]
            j = j -1
            random_list[j +1] = key
    print("sorted list", random_list)

def insertion_sort_reverse(random_list):
    print("unsorted list", random_list)
    for i in range(1,len(random_list)):
        key = random_list[i]
        j =  i - 1
        while j >= 0 and random_list[j] < key:
            random_list[j + 1] = random_list[j]
            j = j -1
            random_list[j +1] = key
    print("sorted list", random_list)

def main():
    print("insertion sort")
    random_list = [6, 1, 5, 2, 7, 3, 87, 32, 8]
    insertion_sort(random_list[:])

    print("insertion sort reverse")
    random_list = [6, 1, 5, 2, 7, 3, 87, 32, 8]
    insertion_sort_reverse(random_list[:])



if __name__ == '__main__':
    main()