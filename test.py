import sys
import os
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

MISS_FOLDER = ['video', 'archive', 'audio', 'documents', 'images', 'others']

path_folder = []                                    #список всіх папок для обробки скрипта
full_path = []                                      #список повного шляху всіх файлів
b = []                                              #список перетворених функцією - транслітерації назв файлів


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

def main():                                         #функція отримання данних від користувача, перевіряє коректність

    if len(sys.argv) < 2:
        user_input = ''
 
    else:
        user_input = sys.argv[1]
        
    path = Path(user_input)
   
    if path.exists():
        
        if path.is_dir():
            
            recursion(path)                        #передача коректних даних веденна користувачем до функції рекурсії
               
        else:
            print(f'{path} is file')
    
    else:
        print(f'{path.absolute()} is not exists')

if __name__ == '__main__':
    main()
     
rm_empty_dir(path_folder)                          #виклик функції перевірки порожніх каталогів

#print(full_path)
#print(path_folder)

for t in full_path:                                #цикл розпізнавання розширення файлів (дописати: -переміщення файлів у кінцеві папки)

     res = os.path.splitext(t)
    
     if res[1] in ALL_EXPANSION:
          
          if 0 <= ALL_EXPANSION.index(res[1]) <= 3:
               result = normalize(str(t)) 
#               print(t, res[1], 'image')
               print(result, '-- image')

          elif 4 <= ALL_EXPANSION.index(res[1]) <= 7:
               result = normalize(str(t)) 
#               print(t, res[1], 'video')
               print(result, '-- video')

          elif 8 <= ALL_EXPANSION.index(res[1]) <= 13:
              result = normalize(str(t)) 
#              print(t, res[1], 'doc')
              print(result, '-- doc')

          elif 14 <= ALL_EXPANSION.index(res[1]) <= 17:
               result = normalize(str(t)) 
#               print(t, res[1], 'audio')
               print(result, '-- audio')

          elif 18 <= ALL_EXPANSION.index(res[1]) <= 20:
               result = normalize(str(t)) 
#               print(t, res[1], 'zip')
               print(result, '-- zip')               

     else:
          result = normalize(str(t)) 
#          print(t, res[1], 'other')
          print(result, '-- other')


#print(b)
