import os

def method_one():
    archive_dir = next(os.walk('.'))[1][1]
    path = f"./{archive_dir}"
    flag = True

    while flag:
        dirs = next(os.walk(path))[1]
        path += f"/{dirs[0]}"
        if len(dirs)>1:
            flag = False

def find_by_name(name, path):
    for root, _, files in os.walk(path):
        for i in files:
            if name in i:
                return os.path.join(root, i)

print(find_by_name("pmlogsummary", "archive"))
