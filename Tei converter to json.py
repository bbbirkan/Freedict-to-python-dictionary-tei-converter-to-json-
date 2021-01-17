import time
import os
from tqdm import tqdm
import re
from collections import defaultdict
import json
import io
from tkinter import filedialog as bir

dictionary=[]
#---------------name of data-------------
sub=bir.askopenfilename()
subs = open(sub)
#print(os.path.basename(subs.name))
teiname=os.path.basename(subs.name)
teiname=os.path.basename(subs.name)# took name
list2=[]#filtre
list2.append(re.split('.tei',teiname))
def sec(lst):
    output = []
    def _sec(i):
        if isinstance(i, list) or isinstance(i, tuple):
            [_sec(j) for j in i]
        else:
            output.append(i)
    _sec(lst)
    return output
sade=sec(list2)
sade = sade[:len(sade)-1] #LAST 1 ELEMENT DELETE
def modification(a,b):
    for x in b:
        try:
            a.remove(x)
        except ValueError:
            pass
    return a
list_to_remove =['']
name_of_file=modification(sade,list_to_remove)
ok_n = ""
for n in sade:
  ok_n = ok_n +" "+n+".json" #make one line merge fonksiyonu for text
print("Creating please wait",ok_n)

#print(*(name_of_file))#
lines = open(sub).readlines()
with open(sub, 'w') as f:
    f.writelines(lines[81:])

# read file line by line
file=open(sub, "r")
lines = file.readlines()
file.close()
text =""
for line in tqdm(lines):
    if re.search('^[0-9]+$', line) is None and re.search('^[0-9]{2}:[0-9]{2}:[0-9]{2}', line) is None and re.search('^$', line) is None:
        text += ' ' + line.rstrip('\n')
        text = text.lstrip()
#print(text)
list2=[]#filtre
list2.append(re.split(' |<cit type="trans">|</body>|<quote>|</TEI>|</text>|n="|<entry>|</entry>|<form>|</quote>|</cit>|</form>|</sense>|<sense>|<sense|">|\[',text))#|>|<
def sec(lst):
    output = []
    def _sec(i):
        if isinstance(i, list) or isinstance(i, tuple):
            [_sec(j) for j in i]
        else:
            output.append(i)
    _sec(lst)
    return output
sade=sec(list2)
elamancikar = [element for element in sade if element]
butun = ""
for n in elamancikar:
    butun = butun +" "+n #make one line merge fonksiyonu for text
#print("butun",butun)
list_to_remove=[" "]
son=[]
son.append(re.split('<orth>|</orth>',butun))
#print(son)
def sec(lst):
    output = []
    def _sec(i):
        if isinstance(i, list) or isinstance(i, tuple):
            [_sec(j) for j in i]
        else:
            output.append(i)
    _sec(lst)
    return output
z=sec(son)

#print(z)

def modification(a,b):
    for x in b:
        try:
            a.remove(x)
        except ValueError:
            pass
    return a

list_to_remove=[" "]
mm=modification(z,list_to_remove)
print(mm)
#---------------------make two list----------------
key_list=[]
value_list=[]
a=-2
b=-1
len=(len(mm))/2# for not show range eror
for i in range(int(len)):
     b=b+2
     a = a + 2
     key_list.append(mm[a])
     value_list.append(mm[b])
     key_list = [x.strip(' ') for x in key_list]
     value_list = [x.strip(' ') for x in value_list]
print("key", key_list)
print("value", value_list)
#--------------------------------------------------


my_dict = defaultdict(list)
for key, value in zip(key_list, value_list):
    #print(key, value)
    my_dict[key].append(value)

print("my_dict", my_dict)
for key in set(key_list):
    for value in value_list:
        if value.startswith('({})'.format(key)):
            my_dict[key].append(value)
new_key = my_dict.keys()
new_value = ['--'.join(value) for value in my_dict.values()]
print(new_key)
print(new_value)
print(my_dict)
#print(my_dict["a la carte"])#simple check

#with open(sub, "w") as fp:
    #json.dump(my_dict,fp, indent = 4)
#with open(ok_n, 'w') as fp:
    #json.dump(my_dict, fp)

with io.open(ok_n, 'w', encoding='utf8') as f3:
   json.dump(my_dict, f3, ensure_ascii=False , indent = 1)
   my_dict = json.dumps(my_dict, ensure_ascii=False)
   #f3.write(unicode(my_dict))