try:
    # try to open a file
    fo = open("Hello.txt", 'r') 
except FileNotFoundError as e:
    print("File notfound:", e)