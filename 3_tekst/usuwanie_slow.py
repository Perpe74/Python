def remove_words(word_list, path_r):

    f1 = open(path_r, "r", encoding="utf8")  # Open file to read
    text = f1.read()        # Read file and save content in "text" variable
    f1.close()              # Close file we read from

    print(text)             # Print text got from file

    # for loop to check if there are words form list in "text"-string
    for i in range(len(word_list)):
        text = text.replace(word_list[i], "")   # Replace word from list with empty string

    print(text)             # Print text without words we wanted to remove

    path_w = "C:/Python2/3_tekst/teksty/pan_tadeusz_usuniete.txt"
    f2 = open(path_w, "w", encoding = "utf-8")  # Open file to write
    f2.write(text)          # Write text to file
    f2.close()              # Close file we wrote to


path = "C:/Python2/3_tekst/teksty/pan_tadeusz.txt"
word_list_to_remove = ["się", "i", "oraz", "nigdy", "dlaczego"]
remove_words(word_list_to_remove, path)
