#1. 笛卡尔积
SELECT * FROM t_employees,t_dept;
SELECT * FROM t_employees  JOIN t_dept;
#2. 内连接 就是笛卡尔积加等值连接，整合表显示左右都有的数据，inner 可以省略
SELECT * FROM t_employees INNER JOIN t_dept ON t_employees.deptno=t_dept.deptno;
SELECT * FROM t_employees,t_dept WHERE t_employees.deptno=t_dept.deptno;
#3. 自然连接 就是跟其他连接方式加等值连接相似，又不大一样，（自然连接不需要加等值连接，他会把相等的字段去除）
SELECT * FROM t_employees NATURAL JOIN t_dept;
SELECT * FROM t_employees NATURAL RIGHT  JOIN t_dept;
SELECT * FROM t_employees NATURAL LEFT JOIN t_dept;
#4. 左外连接 整合表，显示左表有的数据，如果有标没有对应的数据，用NUll补全。outer 项inner一样可以省略
SELECT * FROM t_employees a LEFT OUTER JOIN t_dept b ON a.deptno=b.deptno; 
#5. 右外连接 整合表，显示右表的数据，如果左表没有对应的数据，用NUll补全。
SELECT * FROM t_employees a RIGHT JOIN t_dept b ON a.deptno=b.deptno; 
#6. 全外连接，整合表，两边表的数据都显示，如果左表或右表没有有对应数据，用null补全。（mysql 不支持全外连接）

#SELECT * FROM t_employees a full JOIN t_dept b ON a.deptno=b.deptno; 
#mysql 可以使用左连接和右连接求并集得到全外连接
SELECT * FROM t_employees a LEFT OUTER JOIN t_dept b ON a.deptno=b.deptno
UNION
SELECT * FROM t_employees a RIGHT JOIN t_dept b ON a.deptno=b.deptno; 

