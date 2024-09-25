import os

print(f"The files and folders in {os.getcwd()} are:")
items = os.listdir('.')
for items in items:
    prefix = "(d) " if os.path.isdir(items) else "(f) "
    print(f"{prefix}{items}")
