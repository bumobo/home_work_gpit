import re

a = 'D:/test/Новий текстовий документ (3).txt'

def normalize(path):
    reg = r'\b/[\w\d\W ]+$'
    res = re.findall(reg, a)
    
    return res




print(normalize(a))