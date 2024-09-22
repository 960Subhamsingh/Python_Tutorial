

parent_dir = "D:/Project/Python_Tutorial/13_csvfile/read.txt"

 
with open(parent_dir, 'r') as f1:
    for  i in f1:
        print(f1.readlines())
