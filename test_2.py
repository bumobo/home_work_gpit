import re
import os

a = ['D:/test/test_2/audio_3.txt', 'D:/test/test_2/Новий документ у форматі RTF.rtf', 'D:/test/test_2/Створити точковий рисунок.bmp', 
     'D:/test/Нова папка/video_3.txt', 'D:/test/Нова папка/Нова папка/Нова стиснута ZIP-папка.zip', 'D:/test/Нова папка/Нова папка/Новий документ у форматі RTF.rtf', 
     'D:/test/Нова папка/Нова папка/Новий текстовий документ.txt', 'D:/test/Нова папка/Нова папка/Створити точковий рисунок.bmp', 
     'D:/test/Нова папка/Нова стиснута ZIP-папка.zip', 'D:/test/Нова папка/Новий текстовий документ.txt', 'D:/test/Новий текстовий документ (2).txt', 
     'D:/test/Новий текстовий документ (3).txt', 'D:/test/Новий текстовий документ.txt', 'D:/test/Створити точковий рисунок (2).bmp', 
     'D:/test/Створити точковий рисунок.bmp', 'D:/test/Створити точковий рисунок.pdf']



ALL_EXPANSION = ['.jpeg', '.png', '.jpg', '.svg', '.avi', '.mp4', '.mov', '.mkv', 
                 '.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx', 
                 '.mp3', '.ogg', '.wav', '.amr', '.zip', '.gz', '.tar'
                ]                                                                     #0-3 image, 4-7 video, 8-13 doc, 14-17 audio, 18-20 zip   

for t in a:

     res = os.path.splitext(t)
     
     if res[1] in ALL_EXPANSION:
          if 0 <= ALL_EXPANSION.index(res[1]) <= 3: 
               print(res[1], 'image')
          elif 4 <= ALL_EXPANSION.index(res[1]) <= 7:
               print(res[1], 'video')
          elif 8 <= ALL_EXPANSION.index(res[1]) <= 13:
               print(res[1], 'doc')
          elif 14 <= ALL_EXPANSION.index(res[1]) <= 17:
               print(res[1], 'audio')
          elif 18 <= ALL_EXPANSION.index(res[1]) <= 20:
               print(res[1], 'zip')               

     else:
          print(res[1], 'other')
               
            
  
        
               


