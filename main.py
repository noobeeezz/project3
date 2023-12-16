from logic import sort_folder
import os

if __name__ == "__main__":
    folders = ["А", "Б", "В", "Г"]

    for folder in folders:
        path1 = os.path.abspath(folder)
        path2 = os.path.abspath("new " + folder)

        sort_folder(path1, path2)

