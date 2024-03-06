import os

path_input = input("Enter a path:")
def is_exist(some_path):
    if os.path.exists(some_path):
        for dirname, _, filenames in os.walk(some_path):
            print("Directory:", dirname)
            print("Filenames:")
            for i in filenames:
                print(os.path.join(dirname, i))
            print()
    else:
        print("Path does not exist")
is_exist(path_input)