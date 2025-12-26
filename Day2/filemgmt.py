
import os
f=open("demo.txt","w")
f.write("Hello File Handling")
f.close()
print("File is Closed")
print(os.path.exists(("demo1.txt")))
print(os.path.getsize("demo.txt"),"bytes")

try:
    f1=open("demo.txt","a")
    f1.write("\n New Append Line")
    print(f1.read())
    f1.close()
except:
    print("File Error")
