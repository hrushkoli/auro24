-- Get the sales count for all books where the book category is Comic Book in the year 2006

select bk.Name, count(cbf.Sales), t.year 

from

Comic_books cbf,
Books b,
Time t,
BookCategory bc

where 

cbf.BookCategory_id = bc.BookCategory.id,
bc.Name = "Comic Book",
t.year = 2006


-- Get the maxium sales for the book where the book category is Comic Book in the year 2006

select max(cbf.Sales), b.name

from

Comic_books cbf,
Books b,
Time t,
BookCategory bc

where 

cbf.BookCategory_id = bc.BookCategory.id,
bc.Name = "Comic Book",
t.year = 2006
