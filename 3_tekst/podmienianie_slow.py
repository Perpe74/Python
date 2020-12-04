def replace_words(old_words, new_words, path_r):

    f1 = open(path_r, "r")  # Open file to read
    text = f1.read()        # Read file and save content in "text" variable
    f1.close()              # Close file we read from

    print(text)             # Print text got from file

    dictionary = {old_words[0]: new_words[0], old_words[1]: new_words[1], old_words[2]: new_words[2],
                  old_words[3]: new_words[3]}
    # for loop to check if there are words form list in "text"-string
    for key in dictionary:
        text = text.replace(key, dictionary[key])

    print(text)             # Print text with replaced words

    path_w = "C:/Python2/3_tekst/teksty/test_podmienione.txt"
    f2 = open(path_w, "w")  # Open file to write
    f2.write(text)          # Write text to file
    f2.close()              # Close file we wrote to


path_r = "C:/Python2/3_tekst/teksty/test.txt"

old_words = ["i", "oraz", "nigdy", "dlaczego"]
new_words = ["oraz", "i", "prawie nigdy", "czemu"]

replace_words(old_words, new_words, path_r)
