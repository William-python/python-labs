# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.
import pathlib
path=pathlib.Path.cwd()
for filepath in path.iterdir():
    if str(filepath).endswith(".py"):
        print(filepath)
    if filepath.is_dir():
        for dirpath in filepath.iterdir():
            if str(dirpath).endswith(".py"):
                print(dirpath)
            if dirpath.is_dir():
                for dirpath2 in dirpath.iterdir():
                    if str(dirpath2).endswith(".py"):
                        print(dirpath2)
                    