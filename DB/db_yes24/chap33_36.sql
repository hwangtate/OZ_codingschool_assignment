USE yes24;

-- SELECT title, author FROM Books;
-- SELECT * FROM Books WHERE rating > 9.9; 
-- SELECT title, review FROM Books WHERE review >= 1 ORDER BY review DESC;
-- SELECT title, price FROM Books WHERE price < 20000 ORDER BY price DESC;
-- SELECT * FROM Books WHERE ranking_weeks >= 4 ORDER BY ranking_weeks DESC;
-- SELECT * FROM Books WHERE author = '최진영 저';
-- SELECT * FROM Books WHERE publisher = '은행나무';
-- SELECT author, COUNT(*) AS books_count FROM  Books GROUP BY author ORDER BY books_count DESC;
-- SELECT publisher, COUNT(*) AS count_publisher FROM books GROUP BY publisher ORDER BY count_publisher DESC;
-- SELECT author, AVG(rating) AS rating_avg FROM books GROUP BY author ORDER BY rating_avg DESC LIMIT 10;
-- SELECT title, author FROM books WHERE ranking = 1;
-- SELECT sales, review , title FROM books ORDER BY sales DESC, review DESC LIMIT 10;
-- SELECT * FROM books ORDER BY publishing DESC LIMIT 5;

-- SELECT author, AVG(rating) AS author_avg FROM books GROUP BY author ORDER BY author_avg DESC;
-- SELECT publishing, COUNT(*) AS count_publishing FROM books GROUP BY publishing ORDER BY count_publishing DESC;
-- SELECT title, AVG(price) AS title_pirce FROM books GROUP BY title ORDER BY title_pirce DESC;
-- SELECT * FROM books ORDER BY review DESC LIMIT 5;
-- SELECT ranking, AVG(review) AS avg_review FROM books GROUP BY ranking ORDER BY avg_review DESC;

-- SELECT title, rating FROM books WHERE rating > (SELECT AVG(rating) FROM books) ORDER BY rating DESC;
-- SELECT title, price FROM books WHERE price > (SELECT AVG(price) FROM books) ORDER BY price DESC;
-- SELECT title, review FROM books WHERE review > (SELECT MAX(review) FROM books);
-- SELECT title, price
-- FROM books
-- WHERE price < (SELECT AVG(price) FROM books);
-- SELECT author, title FROM books
-- WHERE author = (SELECT author FROM books GROUP BY author ORDER BY COUNT(*) DESC LIMIT 1);

-- UPDATE Books 
-- SET price = 99999
-- WHERE bookID = 1 
-- UPDATE books
-- SET title = '제목업데이트'
-- WHERE author = '태영';
-- DELETE FROM Books WHERE sales = (SELECT MIN(sales) FROM Books); <- 이거 동일한 테이블이여서 삭제 안됨
-- UPDATE books
-- SET rating = rating + 1
-- WHERE publisher = '태영';

-- SELECT author, AVG(rating), AVG(sales)
-- FROM books
-- GROUP BY author
-- ORDER BY AVG(rating) DESC, AVG(sales) DESC;
-- SELECT publishing, AVG(price) FROM books  GROUP BY publishing ORDER BY publishing ASC; 
-- SELECT publisher, COUNT(*) AS book_count, SUM(review) AS review_sum
-- FROM books GROUP BY publisher ORDER BY book_count DESC;
-- SELECT ranking, AVG(sales) FROM books GROUP BY ranking;
-- SELECT price, AVG(review), AVG(rating) FROM books GROUP BY price;

-- SELECT publisher, author, AVG(sales) AS p_p FROM books GROUP BY publisher, author ORDER BY p_p DESC LIMIT 1;
-- SELECT title, review, price
-- FROM Books
-- WHERE review > (SELECT AVG(review) FROM Books) AND price < (SELECT AVG(price) FROM Books);

-- SELECT author, COUNT(*) as num_books
-- FROM Books
-- GROUP BY author
-- ORDER BY num_books DESC
-- LIMIT 1;

-- SELECT title, author, MAX(sales) AS m_s
-- FROM books
-- GROUP BY title, author
-- ORDER BY m_s DESC LIMIT 1;

-- SELECT YEAR(publishing) as year, COUNT(*) as num_books, AVG(price) as avg_price
-- FROM Books
-- GROUP BY year;

-- SELECT publisher, MAX(rating) - MIN(rating) as rating_difference
-- FROM Books
-- GROUP BY publisher
-- ORDER BY rating_difference DESC
-- LIMIT 1;








