#1. 查出至少有一个员工的部门。显示部门编号、部门名称、部门位置、部门人数。

SELECT a.*,b.c FROM t_dept a,
(SELECT deptno,COUNT(*)AS c FROM t_employees  GROUP BY deptno HAVING COUNT(*)>1)AS b
WHERE a.deptno=b.deptno;

SELECT a.*,b.c FROM t_dept a INNER JOIN 
(SELECT deptno,COUNT(*)AS c FROM t_employees  GROUP BY deptno HAVING COUNT(*)>1)AS b
ON a.deptno=b.deptno;

#2. 列出所有员工的姓名及其直接上级的姓名。

SELECT a.ename,b.ename AS "上级领导"  FROM t_employees a,t_employees b WHERE a. mgr=b.empno
UNION
SELECT a.ename,a.mgr FROM t_employees a WHERE a.mgr IS NULL;

SELECT a.ename,b.ename AS '上级领导' FROM t_employees a JOIN t_employees b ON a.mgr=b.empno
UNION
SELECT a.ename,a.mgr FROM t_employees a WHERE a.mgr IS NULL;

#3. 列出受雇日期早于直接上级的所有员工的编号、姓名、部门名称。

SELECT a.empno,a.ename,b.dname FROM t_employees a,t_dept b,t_employees c WHERE 
a.mgr=c.empno AND a.deptno=b.deptno AND a.hiredate<c.hiredate;

#4. 列出部门名称和这些部门的员工信息，同时列出那些没有员工的部门。
SELECT b.dname,a.* FROM t_dept b LEFT JOIN t_employees a ON a.deptno=b.deptno;

#5. 列出最低薪金大于2500的各种工作及从事此工作的员工人数。

SELECT job,COUNT(*) FROM t_employees  GROUP BY job HAVING MIN(sal)>2500;

#6. 列出在公关部工作的员工的姓名，假定不知道公关部的部门编号。

SELECT * FROM t_employees WHERE deptno=(SELECT deptno FROM t_dept WHERE dname='公关部');

#7. 列出薪金高于公司平均薪金的所有员工信息，所在部门名称，上级领导，工资等级。

SELECT b.dname,a.mgr,a.sal FROM t_employees a JOIN t_dept b ON a.deptno=b.deptno HAVING a.sal>AVG(sal);

#8. 列出与张飞从事相同工作的所有员工及部门名称。

SELECT b.dname,a.ename FROM t_employees a JOIN t_dept b ON a.deptno=b.deptno 
WHERE a.job=(SELECT job FROM t_employees WHERE ename='张飞');

#9. 列出薪金高于在部门30工作的所有员工的薪金的员工姓名和薪金、部门名称。

SELECT a.ename,a.sal,b.dname FROM t_employees a JOIN t_dept b ON a.deptno=b.deptno
WHERE a.deptno=30;