#1
import sqlite3

db = sqlite3.connect('library.db')

c = db.cursor()

c.execute("""
CREATE TABLE authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);
""")

c.execute("""
CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author_id INTEGER,
    publication_year INTEGER,
    FOREIGN KEY(author_id) REFERENCES authors(id)
);
""")

c.execute("""
CREATE TABLE sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER,
    quantity INTEGER NOT NULL,
    FOREIGN KEY(book_id) REFERENCES books(id)
);
""")

c.execute("INSERT INTO authors (first_name, last_name) VALUES ('George', 'Orwell')")
c.execute("INSERT INTO authors (first_name, last_name) VALUES ('J.K.', 'Rowling')")
c.execute("INSERT INTO authors (first_name, last_name) VALUES ('Harper', 'Lee')")

c.execute("INSERT INTO books (title, author_id, publication_year) VALUES ('1984', 1, 1949)")
c.execute("INSERT INTO books (title, author_id, publication_year) VALUES ('Animal Farm', 1, 1945)")
c.execute("INSERT INTO books (title, author_id, publication_year) VALUES ('Harry Potter and the Philosopher's Stone', 2, 1997)")
c.execute("INSERT INTO books (title, author_id, publication_year) VALUES ('To Kill a Mockingbird', 3, 1960)")

c.execute("INSERT INTO sales (book_id, quantity) VALUES (1, 5)")
c.execute("INSERT INTO sales (book_id, quantity) VALUES (2, 10)")
c.execute("INSERT INTO sales (book_id, quantity) VALUES (3, 15)")
c.execute("INSERT INTO sales (book_id, quantity) VALUES (4, 7)")

db.commit()

db.close()





#2
import sqlite3

db = sqlite3.connect('library.db')

c = db.cursor()

print("Books and their Authors:")
c.execute("""
SELECT books.title, authors.first_name, authors.last_name
FROM books
INNER JOIN authors ON books.author_id = authors.id;
""")
inner_join_results = c.fetchall()
for row in inner_join_results:
    print(row)

print("\nAuthors and their Books (including authors without books):")
c.execute("""
SELECT authors.first_name, authors.last_name, books.title
FROM authors
LEFT JOIN books ON authors.id = books.author_id;
""")
left_join_results = c.fetchall()
for row in left_join_results:
    print(row)

print("\nBooks and their Authors (including books without authors):")
c.execute("""
SELECT books.title, authors.first_name, authors.last_name
FROM books
LEFT JOIN authors ON books.author_id = authors.id;
""")
right_join_results = c.fetchall()
for row in right_join_results:
    print(row)

c.execute("""
SELECT books.title, authors.first_name, authors.last_name
   FROM books
   INNER JOIN authors ON books.author_id = authors.id
""")

c.execute("""
 SELECT authors.first_name, authors.last_name, books.title
   FROM authors
   LEFT JOIN books ON authors.id = books.author_id
""")

c.execute("""
SELECT books.title, authors.first_name, authors.last_name
   FROM books
   LEFT JOIN authors ON books.author_id = authors.id
""")

db.close()



#3
import sqlite3

db = sqlite3.connect('library.db')

c = db.cursor()

print("Books, their Authors, and Sales:")
c.execute("""
SELECT books.title, authors.first_name, authors.last_name, sales.quantity
FROM books
INNER JOIN authors ON books.author_id = authors.id
INNER JOIN sales ON books.id = sales.book_id;
""")
inner_join_results = c.fetchall()
for row in inner_join_results:
    print(row)

print("\nAuthors, their Books, and Sales (including authors without books and books without sales):")
c.execute("""
SELECT authors.first_name, authors.last_name, books.title, sales.quantity
FROM authors
LEFT JOIN books ON authors.id = books.author_id
LEFT JOIN sales ON books.id = sales.book_id;
""")
left_join_results = c.fetchall()
for row in left_join_results:
    print(row)

c.execute("""
SELECT books.title, authors.first_name, authors.last_name, sales.quantity
   FROM books
   INNER JOIN authors ON books.author_id = authors.id
   INNER JOIN sales ON books.id = sales.book_id
""")

c.execute("""
SELECT authors.first_name, authors.last_name, books.title, sales.quantity
   FROM authors
   LEFT JOIN books ON authors.id = books.author_id
   LEFT JOIN sales ON books.id = sales.book_id
""")

db.close()



#4
import sqlite3

db = sqlite3.connect('library.db')

c = db.cursor()

print("Total sold books for each author (only authors with sales):")
c.execute("""
SELECT authors.first_name, authors.last_name, SUM(sales.quantity) AS total_sold
FROM authors
INNER JOIN books ON authors.id = books.author_id
INNER JOIN sales ON books.id = sales.book_id
GROUP BY authors.id;
""")
inner_join_results = c.fetchall()
for row in inner_join_results:
    print(row)

print("\nTotal sold books for each author (including authors without sales):")
c.execute("""
SELECT authors.first_name, authors.last_name, SUM(sales.quantity) AS total_sold
FROM authors
LEFT JOIN books ON authors.id = books.author_id
LEFT JOIN sales ON books.id = sales.book_id
GROUP BY authors.id;
""")
left_join_results = c.fetchall()
for row in left_join_results:
    print(row)

c.execute("""
SELECT authors.first_name, authors.last_name, SUM(sales.quantity) AS total_sold
   FROM authors
   INNER JOIN books ON authors.id = books.author_id
   INNER JOIN sales ON books.id = sales.book_id
   GROUP BY authors.id
""")

c.execute("""
SELECT authors.first_name, authors.last_name, SUM(sales.quantity) AS total_sold
   FROM authors
   LEFT JOIN books ON authors.id = books.author_id
   LEFT JOIN sales ON books.id = sales.book_id
   GROUP BY authors.id
""")

db.close()


#5

import sqlite3

db = sqlite3.connect('library.db')

c = db.cursor()

print("Author with the most books sold:")
c.execute("""
SELECT authors.first_name, authors.last_name, SUM(sales.quantity) AS total_sold
FROM authors
INNER JOIN books ON authors.id = books.author_id
INNER JOIN sales ON books.id = sales.book_id
GROUP BY authors.id
HAVING total_sold = (
    SELECT MAX(total_sold)
    FROM (
        SELECT SUM(sales.quantity) AS total_sold
        FROM authors
        INNER JOIN books ON authors.id = books.author_id
        INNER JOIN sales ON books.id = sales.book_id
        GROUP BY authors.id
    ) AS subquery
);
""")
highest_selling_author = c.fetchone()
print(highest_selling_author)

print("\nBooks sold in quantities exceeding the average number of sales:")
c.execute("""
SELECT books.title, SUM(sales.quantity) AS total_sold
FROM books
INNER JOIN sales ON books.id = sales.book_id
GROUP BY books.id
HAVING total_sold > (
    SELECT AVG(total_sold)
    FROM (
        SELECT SUM(sales.quantity) AS total_sold
        FROM books
        INNER JOIN sales ON books.id = sales.book_id
        GROUP BY books.id
    ) AS subquery
);
""")
above_average_sales_books = c.fetchall()
for row in above_average_sales_books:
    print(row)

c.execute("""
SELECT authors.first_name, authors.last_name, SUM(sales.quantity) AS total_sold
FROM authors
INNER JOIN books ON authors.id = books.author_id
INNER JOIN sales ON books.id = sales.book_id
GROUP BY authors.id
HAVING total_sold = (
    SELECT MAX(total_sold)
    FROM (
        SELECT SUM(sales.quantity) AS total_sold
        FROM authors
        INNER JOIN books ON authors.id = books.author_id
        INNER JOIN sales ON books.id = sales.book_id
        GROUP BY authors.id
    ) AS subquery
)
""")

c.execute("""
SELECT books.title, SUM(sales.quantity) AS total_sold
FROM books
INNER JOIN sales ON books.id = sales.book_id
GROUP BY books.id
HAVING total_sold > (
    SELECT AVG(total_sold)
    FROM (
        SELECT SUM(sales.quantity) AS total_sold
        FROM books
        INNER JOIN sales ON books.id = sales.book_id
        GROUP BY books.id
    ) AS subquery
)
""")

db.close()




