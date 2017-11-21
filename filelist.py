import os
import random


f = []
for (dirpath, dirnames, filenames) in os.walk('/home/krushn/Station/savneet'):
    f.extend(filenames)
    break
#print(f)




for file in f:
    d = str(random.randint(7,12)).zfill(2)+str(random.randint(1,30)).zfill(2)
    os.system('sudo date +%Y%m%d -s "2017'+ d +'"')
    
    
    os.system("git add "+ file)
    os.system("git commit -m '"+ file +" added'")

