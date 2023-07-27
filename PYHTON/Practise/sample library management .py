class library_management():
   
   def __init__(self,books):
      self.book_list=books[:]
      self.available_book_list=books
      self.book_lent={} #key=book value=username
    
   def available_books(self):
      for book in self.available_book_list:
         print(book)
   def all_books(self):
      for book in self.book_list:
         print(book)

   def lend_book(self,book,name):
      if book not in self.book_list:
         print('Incorrect Book Name! please check AllBooks')
         return
      if book in self.available_book_list:
         self.book_lent.update({book:name})
         self.available_book_list.remove(book)
         print('you can take a book')
      else:
         print('The book is already taken by ' + self.book_lent[book])

   def return_book(self,book):
      del self.book_lent[book]
      self.available_book_list.append(book)
      print('Book Return Sucessfully!')


if __name__=="__main__":
   lib=library_management(['Harry Potter','Rich Dad Poor Dad','The Almond','The Secret of Mind','Galaxy Spritual'])
   print("Welcome to Our Library")

   while True:
      print('1) Show Available Books.')
      print('2) Show All Books.')
      print('3) Show Book Lent.')
      print('4) Return the Book')
      print('5) Quit')

      choice=int(input('Enter Your Choice:'))

      if(choice==1):
        lib.available_books()
      elif(choice==2):
        lib.all_books()
      elif(choice==3):
        name=input('Lender Name')
        book=input('Book name')
        lib.lend_book(book,name)
      elif(choice==4):
        book=input('Enter a Book Name:')
        lib.return_book(book)
      elif(choice==5):
        break
      else:
         print('Invalid choice! Please Enter a valid choice')