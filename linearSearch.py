def linear_search(l, search):
    index = 0
    for i in l:
        if i == search:
            print ("found ", search, "index is: ", index)
            return
        index += 1
    print("could not find", search, "in the array")



def main():
    print("linear search")
    random_list = [6, 1, 5, 2, 7, 3, 87, 32, 8]
    linear_search(random_list[:], 6)
    linear_search(random_list[:], 87)
    linear_search(random_list[:], 137)

if __name__ == '__main__':
    main()