import glob
import os

search_dir = "path" #папка из которой будет создан список файлов с слешами направо
files = list(filter(os.path.isfile, glob.glob(search_dir + "*")))
files.sort(key=lambda x: os.path.getmtime(x))
files.reverse()

with open("path", "w", encoding='utf-8-sig') as txt_file: #путь к текстовику в котором будет список файлов
    for line in files:
        txt_file.write("".join(line) + "\n") 