/* Check that the table doesn't already exist in the database. If it does,remove it from the database */
DROP TABLE IF EXISTS food_nutrition;

/* Create the table in the database & give it a name */
CREATE TABLE food_nutrition (

/* Tell the database which data to import, what its name in the database should be, & the type of data to import */
	"Category" text,
    "Description" text,
    "Nutrient Data Bank Number" int,
    "Alpha Carotene" float,
    "Ash" float,
    "Beta Carotene" float,
    "Beta Cryptoxanthin" float,
    "Carbohydrate" float
);