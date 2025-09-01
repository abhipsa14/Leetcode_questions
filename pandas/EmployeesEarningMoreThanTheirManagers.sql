/*
 * @lc app=leetcode id=1756423393 lang=mysql
 *
 * EmployeesEarningMoreThanTheirManagers
 * 
 * Difficulty: Level
 * Category: undefined
 * Runtime: N/A
 * Memory: N/A
 */

# Write your MySQL query statement below
select e2.name as Employee
from employee e1
inner join employee e2 on e1.id=e2.managerId
where
e1.salary<e2.salary