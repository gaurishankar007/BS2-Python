create table if not exists authors(
Author_ID int not null auto_increment primary key, 
Author_First_Name varchar(25) not null, 
Author_Last_Name varchar(25) not null, 
No_Of_Books varchar(4) not null
);

create table if not exists Book_Genres(
Book_Genre_ID int not null auto_increment primary key, 
Book_Genre_Name varchar(25), 
No_Of_Books varchar(4) not null
);

create table if not exists Books(
ISBN varchar(20) not null primary key, 
Book_Title varchar(100), 
Language varchar(10), 
Author_ID int, 
Book_Genre_ID int, 
Publication_Year varchar(4), 
Price varchar(15), 
No_Of_Copies varchar(4) not null,
FOREIGN KEY (Author_ID) REFERENCES authors(Author_ID) ON DELETE CASCADE ON UPDATE CASCADE, 
FOREIGN KEY (Book_Genre_ID) REFERENCES Book_Genres (Book_Genre_ID) ON DELETE CASCADE ON UPDATE CASCADE
);


