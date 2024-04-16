CREATE DATABASE Library_management;
USE Library_management;

CREATE TABLE genre(
ID INT PRIMARY KEY IDENTITY(1,1),
Name VARCHAR(20) NOT NULL UNIQUE
);

CREATE TABLE author(
ID INT PRIMARY KEY IDENTITY(1,1),
First_name VARCHAR(20) NOT NULL,
Last_name VARCHAR(20) NOT NULL
);

CREATE TABLE book(
ID INT PRIMARY KEY IDENTITY(1,1),
Genre_ID INT FOREIGN KEY REFERENCES genre(ID) not null,
Author_ID INT FOREIGN KEY REFERENCES author(ID) not null,
Title VARCHAR(255) NOT NULL
);

CREATE TABLE shelf(
ID INT PRIMARY KEY IDENTITY(1,1),
Book_ID INT FOREIGN KEY REFERENCES book(ID) not null,
Shelf_no INT NOT NULL,
Floor INT NOT NULL
);

CREATE TABLE publisher(
ID INT PRIMARY KEY IDENTITY(1,1),
Name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE book_copy(
ID INT PRIMARY KEY IDENTITY(1,1),
Book_ID INT FOREIGN KEY REFERENCES book(ID) not null,
Publisher_ID INT FOREIGN KEY REFERENCES publisher(ID) not null,
Date_of_publication DATE NOT NULL
);

CREATE TABLE users(
ID INT PRIMARY KEY IDENTITY(1,1),
First_name VARCHAR(20) NOT NULL,
Last_name VARCHAR(20) NOT NULL,
Date_of_birth DATE NOT NULL,
Email VARCHAR(50) UNIQUE NOT NULL CHECK(Email LIKE '%@%'),
Phone VARCHAR(13) NOT NULL,
Address VARCHAR(255) NOT NULL
);

CREATE TABLE admin(
ID INT PRIMARY KEY IDENTITY(1,1),
Users_ID INT FOREIGN KEY REFERENCES users(ID) not null,
Role VARCHAR(50),
Password VARCHAR(255)
);

CREATE TABLE borrowing(
ID INT PRIMARY KEY IDENTITY(1,1),
Book_ID INT FOREIGN KEY REFERENCES book(ID) not null,
Users_ID INT FOREIGN KEY REFERENCES users(ID) not null,
Borrowed_date DATE NOT NULL,
Due_date DATE NOT NULL
);



-- insers
INSERT INTO users(First_name, Last_name, Date_of_birth, Email, Phone, Address) VALUES('Tonda', 'Hrouda', '1998-04-10','tonda.hrouda@gmail.com' ,'+420690535420' ,'U Pùjèovny 18'); 
INSERT INTO admin(Users_ID, Role, Password) VALUES(1, 'Admin', '1234');



-- ulozene selecty
SELECT Email, Password FROM users INNER JOIN admin ON users.ID = admin.Users_ID WHERE users.Email = 'tonda.hrouda@gmail.com' AND admin.Password = '1234';

SELECT * FROM publisher;
SELECT * FROM genre;
SELECT * FROM author;
SELECT * FROM users;
SELECT * FROM book;
SELECT * FROM book_copy;
SELECT * FROM borrowing;
SELECT * FROM shelf;

EXEC Create_borrowing_books 'War and Peace','Tonda','Hrouda','2024-01-01','2024-01-01';

SELECT Name FROM publisher;
SELECT Title from book;

SELECT First_name FROM author;
SELECT Last_name FROM author;

SELECT First_name FROM users;
SELECT Last_name FROM users;

SELECT Email FROM users;

--DELETE DATA
DELETE FROM publisher;
DELETE FROM genre;
DELETE FROM author;
DELETE FROM book;
DELETE FROM book_copy;
DELETE FROM borrowing;
DELETE FROM shelf;

-- views
GO
CREATE VIEW Borrowed_books_by_users AS
SELECT borrowing.ID, users.First_name, users.Last_name, users.Phone, book.Title, borrowing.Borrowed_date, borrowing.Due_date 
FROM borrowing INNER JOIN users ON borrowing.Users_ID = users.ID INNER JOIN book ON borrowing.Book_ID = book.ID;
GO

GO
CREATE VIEW Books_author_genre AS
SELECT book.Title, author.First_name, author.Last_name, genre.Name 
FROM book INNER JOIN author ON book.Author_ID = author.ID INNER JOIN genre ON book.Genre_ID = genre.ID;
GO

GO
CREATE VIEW Books_and_publisher AS
SELECT book.Title, book_copy.Date_of_publication, publisher.Name 
FROM book_copy INNER JOIN book ON book_copy.Book_ID = book.ID INNER JOIN publisher ON book_copy.Publisher_ID = publisher.ID;
GO

GO
CREATE VIEW Books_shelf AS
SELECT shelf.ID, Title, shelf.Shelf_no, shelf.Floor FROM book INNER JOIN shelf ON shelf.Book_ID = book.ID;
GO

GO
CREATE VIEW User_info AS
SELECT users.First_name, users.Last_name, users.Email, users.Phone, users.Address, users.Date_of_birth
FROM users;
GO

SELECT * FROM Borrowed_books_by_users;
SELECT * FROM Books_author_genre;
SELECT * FROM Books_and_publisher;
SELECT * FROM Books_shelf;
SELECT * FROM User_info;
-- procedures
GO
CREATE PROCEDURE Add_user @First_name VARCHAR(20), @Last_name VARCHAR(20), @Date_of_birth DATE, @Email VARCHAR(50), @Phone VARCHAR(13), @Address VARCHAR(255)
AS
BEGIN
	BEGIN TRANSACTION;
	BEGIN TRY
		INSERT INTO users (First_name, Last_name, Date_of_birth, Email, Phone, Address)
		VALUES (@First_name, @Last_name, @Date_of_birth, @Email, @Phone, @Address);
		COMMIT;
	END TRY
    BEGIN CATCH
        ROLLBACK;
        THROW;
    END CATCH;
END
GO

EXEC Add_book 'horor','Simon','Simonovsky','U dvou';

GO
CREATE PROCEDURE Add_book @Genre_name VARCHAR(20), @Author_first_name VARCHAR(20), @Author_last_name VARCHAR(20), @Title VARCHAR(255)
AS
BEGIN
	DECLARE @Genre_ID INT;
	DECLARE @Author_ID INT;

	SET @Genre_ID = (SELECT ID FROM genre WHERE Name = @Genre_name);

	SET @Author_ID = (SELECT ID FROM author WHERE First_name = @Author_first_name AND Last_name = @Author_last_name);

	IF @Genre_ID IS NULL OR @Author_ID IS NULL
    BEGIN
        THROW 50000, 'Genre or Author not found.', 1;
    END

	INSERT INTO book (Genre_ID, Author_ID, Title)
	VALUES (@Genre_ID, @Author_ID, @Title);
	COMMIT;
END
GO

GO
CREATE PROCEDURE Create_borrowing_books @Book_title VARCHAR(225), @User_first_name VARCHAR(20), @User_last_name VARCHAR(20), @Borrowed_date DATE, @Due_date DATE
AS
BEGIN
	DECLARE @Users_ID INT;
	DECLARE @Book_ID INT;

	SET @Users_ID = (SELECT ID FROM users WHERE First_name = @User_first_name AND Last_name = @User_last_name);
	SET @Book_ID = (SELECT TOP 1 ID FROM book WHERE Title = @Book_title);

	IF @Users_ID IS NULL OR @Book_ID IS NULL
	BEGIN
		THROW 50000, 'Genre or Author not found.', 1;
	END

	INSERT INTO borrowing (Book_ID, Users_ID, Borrowed_date, Due_date)
	VALUES (@Book_ID, @Users_ID, @Borrowed_date, @Due_date);

	COMMIT;
END
GO

GO
CREATE PROCEDURE Create_book_copy @Book_title VARCHAR(255), @Publisher_name VARCHAR(50)
AS
BEGIN
	DECLARE @Book_ID INT;
	DECLARE @Publisher_ID INT;

	SET @Book_ID = (SELECT ID FROM book WHERE Title = @Book_title);
	SET @Publisher_ID = (SELECT ID FROM publisher WHERE Name = @Publisher_name);

	INSERT INTO book_copy(Book_ID, Publisher_ID, Date_of_publication)
	VALUES (@Book_ID, @Publisher_ID, GETDATE());
		IF @Book_ID IS NULL OR @Publisher_ID IS NULL
    BEGIN
        THROW 50000, 'Genre or Author not found.', 1;
    END

	COMMIT;
END
GO

GO
CREATE PROCEDURE Add_book_to_shelf @Book_title VARCHAR(255), @Shelf_no INT, @Floor_no INT
AS
BEGIN
	DECLARE @Book_ID INT;

	SET @Book_ID = (SELECT ID FROM book WHERE Title = @Book_title);

	IF @Book_ID IS NULL
    BEGIN
        THROW 50000, 'Genre or Author not found.', 1;
    END

	INSERT INTO shelf(Book_ID, Shelf_no, Floor)
	VALUES (@Book_ID, @Shelf_no, @Floor_no);


	COMMIT;
END
GO

GO
CREATE PROCEDURE Find_book @Book_title VARCHAR(255)
AS
BEGIN
	SELECT book.Title, author.First_name, author.Last_name ,shelf.Shelf_no, shelf.Floor 
	FROM book INNER JOIN author ON book.Author_ID = author.ID INNER JOIN shelf ON shelf.Book_ID = book.ID
	WHERE book.Title = @Book_title
END
GO

GO
CREATE PROCEDURE Import_data @Book_title VARCHAR(255), @Author_first_name VARCHAR(20), @Author_last_name VARCHAR(20), @Genre_name VARCHAR(20), @Publisher_name VARCHAR(50), @Shelf_no INT, @Floor_no INT
AS
BEGIN
	DECLARE @Author_ID INT;
	DECLARE @Genre_ID INT;
	DECLARE @Publisher_ID INT;
	DECLARE @Book_ID INT;

	INSERT INTO author(First_name, Last_name) VALUES(@Author_first_name, @Author_last_name);
	INSERT INTO genre(Name) VALUES(@Genre_name);
	INSERT INTO publisher(Name) VALUES(@Publisher_name);

	SET @Author_ID = (SELECT ID FROM author WHERE First_name = @Author_first_name AND Last_name = @Author_last_name);
	SET @Genre_ID = (SELECT ID FROM genre WHERE Name = @Genre_name);
	SET @Publisher_ID = (SELECT ID FROM publisher WHERE Name = @Publisher_name);

	INSERT INTO book(Genre_ID, Author_ID, Title) VALUES(@Genre_ID, @Author_ID, @Book_title);

	SET @Book_ID = (SELECT ID FROM book WHERE Title = @Book_title);

	INSERT INTO book_copy(Book_ID, Publisher_ID, Date_of_publication)
	VALUES (@Book_ID, @Publisher_ID, GETDATE());

	INSERT INTO shelf(Book_ID, Shelf_no, Floor) VALUES(@Book_ID, @Shelf_no, @Floor_no);

	IF @Book_ID IS NULL OR @Publisher_ID IS NULL OR @Genre_ID IS NULL OR @Author_ID IS NULL 
    BEGIN
        THROW 50000, 'Error.', 1;
    END
END
GO
