COPY           5 RECORDS INTO region   FROM '/Users/lujing/Desktop/cources/dbms/assignment_1/downloaded/dbgen/SF-1/data/region.tbl'      USING DELIMITERS '|', '|\n';
COPY          25 RECORDS INTO nation   FROM '/Users/lujing/Desktop/cources/dbms/assignment_1/downloaded/dbgen/SF-1/data/nation.tbl'      USING DELIMITERS '|', '|\n';
COPY       10000 RECORDS INTO supplier FROM '/Users/lujing/Desktop/cources/dbms/assignment_1/downloaded/dbgen/SF-1/data/supplier.tbl'    USING DELIMITERS '|', '|\n';
COPY      150000 RECORDS INTO customer FROM '/Users/lujing/Desktop/cources/dbms/assignment_1/downloaded/dbgen/SF-1/data/customer.tbl'    USING DELIMITERS '|', '|\n';
COPY      200000 RECORDS INTO part     FROM '/Users/lujing/Desktop/cources/dbms/assignment_1/downloaded/dbgen/SF-1/data/part.tbl'        USING DELIMITERS '|', '|\n';
COPY      800000 RECORDS INTO partsupp FROM '/Users/lujing/Desktop/cources/dbms/assignment_1/downloaded/dbgen/SF-1/data/partsupp.tbl'    USING DELIMITERS '|', '|\n';
COPY     1500000 RECORDS INTO orders   FROM '/Users/lujing/Desktop/cources/dbms/assignment_1/downloaded/dbgen/SF-1/data/orders.tbl'      USING DELIMITERS '|', '|\n';
COPY     6001215 RECORDS INTO lineitem FROM '/Users/lujing/Desktop/cources/dbms/assignment_1/downloaded/dbgen/SF-1/data/lineitem.tbl'    USING DELIMITERS '|', '|\n';
