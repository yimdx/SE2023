CREATE TABLE upShelfRequest(
    userName varchar(11), 
    shopName varchar(13) not null, 
    name varchar(195) not null primary key, 
    discription varchar(387) not null, 
    picture text not null, 
    price float not null, 
    stock int not null, 
    submitStatus varchar(20) not null
)DEFAULT CHARACTER SET utf8mb4;

CREATE TABLE MCIRequest(
    userName varchar(11), 
    shopName varchar(13) not null, 
    name varchar(195) not null primary key, 
    discription varchar(387) not null, 
    picture text not null, 
    price float not null, 
    stock int not null,
    submitStatus varchar(10) not null
)DEFAULT CHARACTER SET utf8mb4;

CREATE TABLE openningRequestForm(
    userName varchar(11) primary key, 
    shopName varchar(13) not null, 
    goodsType TEXT not null, 
    identificationID varchar(19) not null, 
    shopIntro varchar(129) not null, 
    address varchar(32) not null, 
    initialFund int not null, 
    startTime varchar(11) not null, 
    submitStatus varchar(20) not null
)DEFAULT CHARACTER SET utf8mb4;

CREATE TABLE shopList(
    userName varchar(11) primary key, 
    shopName varchar(13) not null, 
    goodsType TEXT not null, 
    identificationID varchar(19) not null, 
    shopIntro varchar(129) not null, 
    address varchar(32) not null, 
    initialFund int not null, 
    startTime varchar(11) not null, 
    balance float not null DEFAULT 0.0
)DEFAULT CHARACTER SET utf8mb4;

CREATE TABLE goodsList(
merchantName varchar(13),
name varchar(195) primary key, 
discription varchar(387) not null, 
picture text not null, 
price float not null, 
stock int not null, 
shelf varchar(4) not null
)DEFAULT CHARACTER SET utf8mb4;

CREATE TABLE cart(
buyerName varchar(11),
merchantName varchar(11), 
goodsName varchar(195) primary key, 
picture text not null, 
unitPrice float not null, 
quantity int not null, 
shelf varchar(4)
)DEFAULT CHARACTER SET utf8mb4;
