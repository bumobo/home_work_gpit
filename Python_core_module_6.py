import sys
import os
import shutil
from pathlib import Path


ALL_EXPANSION = ['.jpeg', '.png', '.jpg', '.svg', 
                 '.avi', '.mp4', '.mov', '.mkv', 
                 '.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx', 
                 '.mp3', '.ogg', '.wav', '.amr', 
                 '.zip', '.gz', '.tar'
                ]                                   #0-3 image, 4-7 video, 8-13 doc, 14-17 audio, 18-20 zip

translit_dict = {
        ord('а'): 'a', ord('А'): 'A', ord('б'): 'b', ord('Б'): 'B', ord('в'): 'v', ord('В'): 'V', ord('г'): 'h', ord('Г'): 'H', ord('ґ'): 'g', ord('Ґ'): 'G',
        ord('д'): 'd', ord('Д'): 'D', ord('е'): 'e', ord('Е'): 'E', ord('є'): 'ie', ord('Є'): 'Ie', ord('ж'): 'zh', ord('Ж'): 'Zh', ord('з'): 'z', ord('З'): 'Z',
        ord('и'): 'y', ord('И'): 'Y', ord('і'): 'i', ord('І'): 'I', ord('ї'): 'i', ord('Ї'): 'I', ord('й'): 'i', ord('Й'): 'I', ord('к'): 'k', ord('К'): 'K',
        ord('л'): 'l', ord('Л'): 'L', ord('м'): 'm', ord('М'): 'M', ord('н'): 'n', ord('Н'): 'N', ord('о'): 'o', ord('О'): 'O', ord('п'): 'p', ord('П'): 'P',
        ord('р'): 'r', ord('Р'): 'R', ord('с'): 's', ord('С'): 'S', ord('т'): 't', ord('Т'): 'T', ord('у'): 'u', ord('У'): 'U', ord('ф'): 'f', ord('Ф'): 'F',
        ord('х'): 'kh', ord('Х'): 'Kh', ord('ц'): 'ts', ord('Ц'): 'Ts', ord('ч'): 'ch', ord('Ч'): 'Ch', ord('ш'): 'sh', ord('Ш'): 'Sh', 
        ord('щ'): 'shch', ord('Щ'): 'Shch', ord('ь'): '', ord('ю'): 'iu', ord('Ю'): 'Iu', ord('я'): 'ia', ord('Я'): 'Ia'
    }                                               #словник для транслітерації 

MISS_FOLDER = ['video', 'archives', 'audio', 'documents', 'images', 'others']

path_folder = []                                    #список всіх папок для обробки скрипта
full_path = []                                      #список повного шляху всіх файлів
b = []                                              #список перетворених функцією - транслітерації назв файлів

user_input_def = ''

path_folder_finish = []

video = []
archives = []
audio = []
documents = []
images = []
other = []
all_folder = [video, audio, images, documents, archives, other]


def normalize(path):                                #функція транслітерації назв файлів
     
    res = path.rsplit('\\')
    translated = res[-1].translate(translit_dict)
        
    for k in translated:
        if k == '.':
            break
        elif k.isdigit() or k.isalpha():
            continue
#        elif k == ' ':
#            continue
        else:
            translated = translated.replace(k, '_')
     
    b.append(translated)
    return translated

def recursion(path):                                #функція рекурсії, додавання шляхів файлів і папок в окремі списки, крім папок MISS_FOLDER

    if path.is_dir():
        
        if path.name in MISS_FOLDER:
            pass
        else: 
            path_folder.append(path.absolute())
            path_folder_finish.append(path.absolute())
            

        
            for item in path.iterdir():           
                recursion(item)
    
    elif path.is_dir() == False:
       full_path.append(path.absolute())
        
def rm_empty_dir(folder):                           #функція видалення порожніх каталогів 
    
    el = 1
    el_x = 1
    
    while el == el_x:
       
        el_x += 1
       
        for i in folder:
            
            if next(os.scandir(i), None) == None:

                folder.pop(folder.index(i))
                os.rmdir(i)
                el_x = el


def move(start, finish):                           #функція перміщення файлів по категоріям
    
    shutil.move(start, finish)

     
rm_empty_dir(path_folder)                          #виклик функції перевірки порожніх каталогів


#print(full_path)
#print(path_folder)

if len(sys.argv) < 2:                              #отримує дані від корисьувача та перевіряє коректність
    user_input = ''
 
else:
    user_input = sys.argv[1]
        
path = Path(user_input)
   
if path.exists():
        
    if path.is_dir():
        user_input_def = str(path)    
        recursion(path)                            #передача коректних даних веденна користувачем до функції рекурсії
               
    else:
        print(f'{path} is file')
    
else:
    print(f'{path.absolute()} is not exists')


for t in full_path:                                #цикл розпізнавання розширення файлів (дописати: -переміщення файлів у кінцеві папки)

    res = os.path.splitext(t)
     
    if res[1] in ALL_EXPANSION:
          
        if 0 <= ALL_EXPANSION.index(res[1]) <= 3:
            foldername = 'images'
            filepath = os.path.join(user_input_def, foldername)

            try: 
                os.mkdir(filepath)
            except FileExistsError:
                pass 

            result = normalize(str(t))
            
            filepath_new = os.path.join(filepath, result)
            move(t, filepath_new)
            rm_empty_dir(path_folder_finish)

        elif 4 <= ALL_EXPANSION.index(res[1]) <= 7:

            foldername = 'video'
            filepath = os.path.join(user_input_def, foldername)

            try: 
                os.mkdir(filepath)
            except FileExistsError:
                pass

            result = normalize(str(t))

            filepath_new = os.path.join(filepath, result)
            move(t, filepath_new)
            rm_empty_dir(path_folder_finish)
                   


        elif 8 <= ALL_EXPANSION.index(res[1]) <= 13:

            foldername = 'documents'
            filepath = os.path.join(user_input_def, foldername)

            try: 
                os.mkdir(filepath)
            except FileExistsError:
                pass 

            result = normalize(str(t))
            documents.append(result)

            filepath_new = os.path.join(filepath, result)
            move(t, filepath_new)
            rm_empty_dir(path_folder_finish)
            
             

            
        elif 14 <= ALL_EXPANSION.index(res[1]) <= 17:
            foldername = 'audio'
            filepath = os.path.join(user_input_def, foldername)

            try: 
                os.mkdir(filepath)
            except FileExistsError:
                pass 

            result = normalize(str(t))
            audio.append(result)
            
            filepath_new = os.path.join(filepath, result)
            move(t, filepath_new)
            rm_empty_dir(path_folder_finish)
           

        elif 18 <= ALL_EXPANSION.index(res[1]) <= 20:
            foldername = 'archives'
            filepath = os.path.join(user_input_def, foldername)

            try: 
                os.mkdir(filepath)
            except FileExistsError:
                pass 

            result = normalize(str(t))
            archives.append(result)

            result = result.rsplit('.')
            
            filepath_new = os.path.join(filepath, result[0])

            try:
                shutil.unpack_archive(t, filepath_new)
            except ValueError:
                os.remove(t)
            
            os.remove(t)

            
            #move(t, filepath_new)
            rm_empty_dir(path_folder_finish)
           

    else:
        foldername = 'other'
        filepath = os.path.join(user_input_def, foldername)

        try: 
            os.mkdir(filepath)
        except FileExistsError:
            pass 

        result = normalize(str(t))
        other.append(result)
            
        filepath_new = os.path.join(filepath, result)
        move(t, filepath_new)
        rm_empty_dir(path_folder_finish)

                                    





counter = 0

separator = '-' * 55
colums_name = '|{:^32}|{:^22}|'.format('file name', 'file extension')
colums = ''

for folder in all_folder:

    if len(folder) == 0:
        pass
    else:

        if counter == 0:
            header = '|{:^55}|'.format('FOLDER VIDEO')
        elif counter == 1:
            header = '|{:^55}|'.format('FOLDER AUDIO')
        elif counter == 2:
            header = '|{:^55}|'.format('FOLDER IMAGES')
        elif counter == 3:
            header = '|{:^55}|'.format('FOLDER DOCUMENTS')
        elif counter == 4:
            header = '|{:^55}|'.format('FOLDER ARCHIVES')
        else:
            header = '|{:^55}|'.format('FOLDER OTHERS')
        
        table = '\n'.join([separator, header, separator, colums_name, separator])
        print(table)

        for file in folder: 
            file = file.rsplit('.')
            colums = '|{:<32}|{:^22}|'.format(file[0], file[1])

            print(colums)
    counter += 1


