import sys
from pathlib import Path
 
image = [] #all_files[0]
video = [] #all_files[1]
document = [] #all_files[2]
music = [] #all_files[3]
archive = [] #all_files[4]
other = []

temp = []

result_sort = [image, video, document, music, archive, other]

all_expansion = [['.jpeg', '.png', '.jpg', '.svg'], ['.avi', '.mp4', '.mov', '.mkv'], 
                 ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'], 
                 ['.mp3', '.ogg', '.wav', '.amr'], ['.zip', '.gz', '.tar']]

path_file = {}

def main():

    if len(sys.argv) < 2:
        user_input = ''
 
    else:
        user_input = sys.argv[1]

    path = Path(user_input)
    
    if path.exists():
        
        if path.is_dir():
#            print(path)
            recursion(path)
               
        else:
            print(f'{path} is file')
    
    else:
        print(f'{path.absolute()} is not exists')

def recursion(path_folder):
    
    if path_folder.is_dir():
#        print(path_folder.name + '/')
 
        for item in path_folder.iterdir():
            recursion(item)
 
    else:
#        all_1.append(str(path_folder.name))
        path_file[path_folder.name] = path_folder
#        print(path_folder)
#        print(path_folder.name)

if __name__ == '__main__':
    main()

for key in path_file:

    for list in all_expansion:

        for expansion in list:

            if Path(key).suffix == expansion:
                result_sort[all_expansion.index(list)].append(key)
            
            else:
                temp.append(key)

#temp_sort = set(temp)

#for i in temp_sort:
#    other.append(i)  
              
print(result_sort)


    