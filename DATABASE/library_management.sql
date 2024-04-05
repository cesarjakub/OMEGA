CREATE DATABASE Library_management;
USE Library_management;

CREATE TABLE genre(
ID INT PRIMARY KEY IDENTITY(1,1),
Name VARCHAR(20) NOT NULL
);

CREATE TABLE author(
ID INT PRIMARY KEY IDENTITY(1,1),
First_name VARCHAR(20) NOT NULL,
Last_name VARCHAR(20) NOT NULL
);

CREATE TABLE book(
ID INT PRIMARY KEY IDENTITY(1,1),
Genre_ID INT FOREIGN KEY REFERENCES genre(ID),
Author_ID INT FOREIGN KEY REFERENCES author(ID),
Title VARCHAR(255) NOT NULL
);

CREATE TABLE shelf(
ID INT PRIMARY KEY IDENTITY(1,1),
Book_ID INT FOREIGN KEY REFERENCES book(ID),
Shelf_no INT NOT NULL,
Floor INT NOT NULL
);

CREATE TABLE publisher(
ID INT PRIMARY KEY IDENTITY(1,1),
Name VARCHAR(50) NOT NULL
);

CREATE TABLE book_copy(
ID INT PRIMARY KEY IDENTITY(1,1),
Book_ID INT FOREIGN KEY REFERENCES book(ID),
Publisher_ID INT FOREIGN KEY REFERENCES publisher(ID),
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
Users_ID INT FOREIGN KEY REFERENCES users(ID),
Role VARCHAR(50),
Password VARCHAR(255)
);

CREATE TABLE borrowing(
ID INT PRIMARY KEY IDENTITY(1,1),
Book_ID INT FOREIGN KEY REFERENCES book(ID),
Users_ID INT FOREIGN KEY REFERENCES users(ID),
Borrowed_date DATE NOT NULL,
Due_date DATE NOT NULL
);

-- insers
INSERT INTO users(First_name, Last_name, Date_of_birth, Email, Phone, Address) VALUES('Tonda', 'Hrouda', '1998-04-10','tonda.hrouda@gmail.com' ,'+420690535420' ,'U Pùjèovny 18'); 
INSERT INTO admin(Users_ID, Role, Password) VALUES(1, 'Admin', '1234');


-- ulozene selecty
SELECT Email, Password FROM users INNER JOIN admin ON users.ID = admin.Users_ID WHERE users.Email = 'tonda.hrouda@gmail.com' AND admin.Password = '1234';

-- views
GO
CREATE VIEW Borrowed_books_by_users AS
SELECT users.ID, users.First_name, users.Last_name, users.Phone, book.Title, borrowing.Borrowed_date, borrowing.Due_date 
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

GO
CREATE PROCEDURE Add_book @Genre_name VARCHAR(20), @Author_first_name VARCHAR(20), @Author_last_name VARCHAR(20), @Title VARCHAR(255)
AS
BEGIN
	BEGIN TRANSACTION;
	BEGIN TRY
		DECLARE @Genre_ID INT;
		DECLARE @Author_ID INT;

		SET @Genre_ID = (SELECT ID FROM genre WHERE Name = @Genre_name);

		SET @Author_ID = (SELECT ID FROM author WHERE First_name = @Author_first_name AND Last_name = @Author_last_name);

		INSERT INTO book (Genre_ID, Author_ID, Title)
		VALUES (@Genre_ID, @Author_ID, @Title);
		COMMIT;
	END TRY
    BEGIN CATCH
        ROLLBACK;
        THROW;
    END CATCH;
END
GO

GO
CREATE PROCEDURE Create_borrowing_books @Book_title VARCHAR(20), @User_first_name VARCHAR(20), @User_last_name VARCHAR(20), @Borrowed_date DATE, @Due_date DATE
AS
BEGIN
	BEGIN TRANSACTION;
	BEGIN TRY
		DECLARE @Users_ID INT;
		DECLARE @Book_ID INT;

		SET @Users_ID = (SELECT ID FROM users WHERE First_name = @User_first_name AND Last_name = @User_last_name);
		SET @Book_ID = (SELECT ID FROM book WHERE Title = @Book_title);

		INSERT INTO borrowing (Book_ID, Users_ID, Borrowed_date, Due_date)
		VALUES (@Book_ID, @Users_ID, @Borrowed_date, @Due_date);

		COMMIT;
	END TRY
    BEGIN CATCH
        ROLLBACK;
        THROW;
    END CATCH;
END
GO

GO
CREATE PROCEDURE Create_book_copy @Book_title VARCHAR(255), @Publisher_name VARCHAR(50)
AS
BEGIN
	BEGIN TRANSACTION;
	BEGIN TRY
		DECLARE @Book_ID INT;
		DECLARE @Publisher_ID INT;

		SET @Book_ID = (SELECT ID FROM book WHERE Title = @Book_title);
		SET @Publisher_ID = (SELECT ID FROM publisher WHERE Name = @Publisher_name);

		INSERT INTO book_copy(Book_ID, Publisher_ID, Date_of_publication)
		VALUES (@Book_ID, @Publisher_ID, GETDATE());

		COMMIT;
	END TRY
    BEGIN CATCH
        ROLLBACK;
        THROW;
    END CATCH;
END
GO