import os
import shutil


def extract_numbers(input_string):
    result = ""
    for char in input_string:
        if char.isdigit():
            result += char
    return result


def get_files_cnt_from(path):
    with os.scandir(path) as entries:
        num_files = sum(1 for entry in entries if entry.is_file())

    return num_files


def sort_folder(path1, path2):
    if not os.path.exists(path2):
        os.makedirs(path2)

        for i in range(1, 11):
            pth = os.path.join(path2, str(i))
            os.makedirs(pth)

    for root, dirs, files in os.walk(path1):
        for file in files:
            file_path = os.path.join(root, file)

            file_number = extract_numbers(file)

            if int(file_number) > 10 or int(file_number) < 1: continue

            fold = os.path.join(path2, file_number)
            num = get_files_cnt_from(fold)

            new_file_path = os.path.join(fold, str(num + 1) + ".jpg")

            shutil.move(file_path, new_file_path)

    shutil.rmtree(path1)
