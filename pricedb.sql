CREATE TABLE Price(
    dt DATE NOT NULL,
    price NUMERIC,
    PRIMARY KEY dt
);


CREATE TABLE Network_fee(
    regime PRIMARY KEY INT(1);
    fee NUMERIC
);