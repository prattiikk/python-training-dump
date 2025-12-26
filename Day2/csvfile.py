import csv
f=open("student.csv","w",newline="")
w=csv.writer(f)
w.writerow(["ID","Name","Marks"])
w.writerow([1,"Ravi",90])
w.writerow([2,"Tej",80])
f.close()