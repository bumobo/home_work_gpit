import sys
import os
from pathlib import Path

ALL_EXPANSION = ['.jpeg', '.png', '.jpg', '.svg', 
                 '.avi', '.mp4', '.mov', '.mkv', 
                 '.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx', 
                 '.mp3', '.ogg', '.wav', '.amr', 
                 '.zip', '.gz', '.tar'
                ]                                   #0-3 image, 4-7 video, 8-13 doc, 14-17 audio, 18-20 zip

MISS_FOLDER = ['video', 'archive', 'audio', 'documents', 'images', 'others']

path_folder = []                                    #список всіх папок для обробки скрипта
full_path = []                                      #список повного шляху всіх файлів

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
            recursion(path)                        #передача даних до функції рекурсії
               
        else:
            print(f'{path} is file')
    
    else:
        print(f'{path.absolute()} is not exists')

if __name__ == '__main__':
    main()
     
rm_empty_dir(path_folder)                          #виклик функції перевірки порожніх каталогів

#print(full_path)
#print(path_folder)

for t in full_path:                                #цикл розпізнавання розширення файлів

     res = os.path.splitext(t)
     
     if res[1] in ALL_EXPANSION:
          
          if 0 <= ALL_EXPANSION.index(res[1]) <= 3: 
               print(t, res[1], 'image')

          elif 4 <= ALL_EXPANSION.index(res[1]) <= 7:
               print(t, res[1], 'video')

          elif 8 <= ALL_EXPANSION.index(res[1]) <= 13:
               print(t, res[1], 'doc')

          elif 14 <= ALL_EXPANSION.index(res[1]) <= 17:
               print(t, res[1], 'audio')

          elif 18 <= ALL_EXPANSION.index(res[1]) <= 20:
               print(t, res[1], 'zip')               

     else:
          print(t, res[1], 'other')
          