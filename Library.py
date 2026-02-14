from datetime import datetime
import pymysql as sqlt


password = input('Enter the password :')
if password != "helloWorld":
   print("Wrong password!")
   exit()


else:
   print("           WELCOME TO THE LIBRARY    ")
   mycon = sqlt.connect(host = "localhost",user="root",password = "helloWorld",database = "company")
   cursor = mycon.cursor()




def addbook():
   bno = int(input('Enter the new book number: :'))
   name = input('Enter the new book name :')
   st = input('Enter whether book is available/issued :')
   author = input('Enter the name of author :')
   add = "insert into book(book_no, book_name, status, author) values(%s,%s,%s,%s)"
   val = (bno,name,st,author)
   cursor.execute(add,val)
   mycon.commit()
  


def delbook():
   name = input('Enter the name of the book to be deleted :')
   delete = "delete from book where book_name = %s"
   cursor.execute(delete,name)
   mycon.commit()




def issuebook():
   num = int(input('Enter the number of book that is to be issued :'))
   name = input('Enter the name to whom book is issued :')
   dateInput = input("Enter the issuedate in the format yyyy/mm/dd :")


   try:
       dateObject = datetime.strptime(dateInput, "%Y/%m/%d")
   except ValueError:
       raise ValueError("WRONG DATE FORMAT!")


   sql = "insert into issued(book_no,issuedto,issuedate) values(%s,%s,%s)"
   val = (num,name,str(dateObject))
   val2 = ('issued',num)
   cursor.execute(sql,val)
   cursor.execute("update book set status=%s where book_no=%s",val2)
   mycon.commit()




def viewbook():
   num = int(input('Enter the book number which you want to see :'))
   cursor.execute("select * from book where book_no=%s",num)
   data = cursor.fetchall()
   for i in data:
       print(i)




def returnbook():
   retdate = input("Enter the date of return in format yyyy/mm/dd :")
   try:
       dateobject = datetime.strptime(retdate, "%Y/%m/%d")
   except ValueError:
           raise ValueError('wrong date format!')
   cursor.execute('select * from issued where book_no = %s',b)
   item = cursor.fetchall()
   j = item[0]
   p = "select datediff(%s,%s ) as days"
   val = (retdate,j[2])
   cursor.execute(p,val)
   day = cursor.fetchall()
   x = day[0]
   print('book is returned after :',x[0],'days')


   if x[0]>7:
           print("amount of fine to be paid :")
           fine = (x[0] - 7)*10
           print(fine)
   elif x[0]<=7:
           print("NO fine to be charged!")
   value = ('available',num)
   cursor.execute("update book set status =%s where book_no = %s",value)
   s = "delete from issued where book_no = %s"
   cursor.execute(s,num)
   mycon.commit()


while True:   
   print('    Enter 1 for adding book')
   print('    Enter 2 for deleting book')
   print('    Enter 3 for issuing book')
   print('    Enter 4 for viewing book info')
   print('    Enter 5 for returning book')
   print('    Enter 6 for exiting ')


   ch = int(input('Enter the value :'))


   if ch == 1:
       addbook()
  
       cursor.execute('select * from book')
       dat1 = cursor.fetchall()
       for i in dat1:


           print(i)


   elif ch == 2:
       delbook()


       cursor.execute('select * from book')
       dat2 = cursor.fetchall()
       for p in dat2:
           print(p)


   elif ch == 3:
       cursor.execute("select * from book")
       dat3 = cursor.fetchall()


       for k in dat3:
           if k[2] == "available":
               issuebook()


               cursor.execute('select * from issued')
               dat4 = cursor.fetchall()
               for j in dat4:
                   print(j)
          
               cursor.execute('select * from book')
               dat5 = cursor.fetchall()
               print('After issuing the book table BOOK changes as follows :')
               for z in dat5:
                   print(z)
               break


           else:
               print("Sorry book is currently issued!")


   elif ch == 4:
       viewbook()


   elif ch == 5:
       cursor.execute("select * from book")
       tup = cursor.fetchall()
	 num = int(input(‘Enter the book no to be returned’))
       for k in tup:
           if k[2] == "issued" and k[0]== num:
               returnbook()
               print('After returning table BOOK changes as follows :')
               print(k) 
           else:
               print("BOOK is already available!")
   elif ch == 6:
       exit()


