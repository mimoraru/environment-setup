# the beer song

word = "bottles"
for num_bott in range(99, 0, -1):
    print(num_bott, word, " of beer on a shelf")
    print(num_bott, word, " of beer")
    print("take one down")
    print("pass it around")

    if num_bott == 1:
        print("No more bottles of beer on the wall")   
    else:
        new_num = num_bott-1
        if new_num == 1:
            word = "bottle"
        print(new_num, word, "of beer on a sherlf")

    print()
