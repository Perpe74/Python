import os

def change_extension(path, current_extension, dest_extension):

    os.chdir(path)
    for filename in os.listdir(path):

        if filename.endswith(current_extension):
            prefix = filename.split(".")[0]
            os.rename(filename, prefix + dest_extension)


path = "C:/Python2/2_praca_z_plikami/pliki"
change_extension(path, ".jpg", ".png")
