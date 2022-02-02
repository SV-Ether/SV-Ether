-- M_id M Company M_Name M_Price M_Mt_date
CREATE TABLE MobileMaster (M_id CHAR(5), M_Company VARCHAR(25), M_Name VARCHAR(20), M_Price INT, M_Mt_date DATE);
-- MB001 Samsung Galaxy 4500 2013-02-12
-- 3 Nokia N1100 2250 2011-04-15
-- 4 Micromxa Unite3 4500 2016-10-17
-- 5 Sony XperiaM 7500 2017-11-20
-- 6 Oppo SelfieEx 8500 2010-08-21
-- Mobile Stock
INSERT INTO MobileMaster VALUES('MB003', 'Nokia', 'N1100', 2250, '2011-04-15')
INSERT INTO MobileMaster VALUES('MB004', 'Micromax', 'Unite3', 4500, '2016-10-17')
INSERT INTO MobileMaster VALUES('MB005', 'Sony', 'XperiaM', 7500, '2017-11-20')
INSERT INTO MobileMaster VALUES('MB006', 'Oppo', 'SelfieEx', 8500, '2010-08-21')
-- S_id M_id M_Qty M_Supplier

CREATE TABLE MobileStock (S_id CHAR(4), M_id CHAR(5), M_Qty INT, M_Supplier VARCHAR(25));
-- S001 MB004 450 New Vision
-- 2 MB003 250 Praveen Gallery
-- 3 MB001 300 Classic Mobile Store
-- 4 MB006 150 A-One Mobiles
-- 5 MB004 150 The Mobile
-- 6 MB006 50 Mobile Center
INSERT INTO MobileStock VALUES('S001', 'MB004', 450, 'New Vision');
INSERT INTO MobileStock VALUES('S002', 'MB003', 250, 'Praveen Gallery');
INSERT INTO MobileStock VALUES('S003', 'MB001', 300, 'Classic Mobile Store');
INSERT INTO MobileStock VALUES('S004', 'MB006', 150, 'A-One Mobiles');
INSERT INTO MobileStock VALUES('S005', 'MB004', 150, 'The Mobile');
INSERT INTO MobileStock VALUES('S006', 'MB006', 50 , 'Mobile Center');


SELECT M_Company, M_Name, M_Price FROM MobileMaster GROUP BY M_Mt_Date ASC;
SELECT * FROM MobileMaster WHERE M_Name LIKE "S%";
SELECT M_Supplier, M_Qty FROM MobileStock WHERE M_id NOT LIKE "MB003";
SELECT M_Company, M_Price FROM MobileMaster WHERE M_Price > 3000 and M_Price < 5000;

-- POST QUERY AND OUTPUT
SELECT M_id, SUM(M_Qty) FROM MobileStock GROUP BY M_id;
SELECT MAX(M_Mt_Date), MIN(M_Mt_Date) FROM MobileMaster;
SELECT AVG(M_price) FROM MobileMaster;