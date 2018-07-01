

INSERT INTO  Employee Values(101,'P',15,76,'Patna')
INSERT INTO  Employee Values(102,'Q',16,76,'Ranchi')
INSERT INTO  Employee Values(103,'R',17,76,'Patna')
INSERT INTO  Employee Values(104,'S',15,76,'Hyderabad')
INSERT INTO  Employee Values(105,'T',12,76,'Pune')

InSERT INTO SkillSet Values(1,'c')
InSERT INTO SkillSet Values(2,'cpp')

InSERT INTO SkillSet Values(3,'c#')
InSERT INTO SkillSet Values(4,'java')
InSERT INTO SkillSet Values(5,'php')
InSERT INTO SkillSet Values(6,'web technology')


INSERT INTO Employee_Skill Values(101,1,4,2)
INSERT INTO Employee_Skill Values(101,2,4,3)
INSERT INTO Employee_Skill Values(101,3,4,2)
INSERT INTO Employee_Skill Values(102,4,4,5)
INSERT INTO Employee_Skill Values(102,1,4,2)
INSERT INTO Employee_Skill Values(104,5,4,1)
INSERT INTO Employee_Skill Values(105,1,4,2)
INSERT INTO Employee_Skill Values(101,1,4,3)
INSERT INTO Employee_Skill Values(102,3,4,2)

INSERT INTO Profile 
Values(1,'Software Engineer','SDE,SE,IT Engineer,Technical Staff')
INSERT INTO Profile 
Values(2,'Accountant','Accounting Manager,accountant')
INSERT INTO Profile 
Values(3,'Database Administrator','Database Administrator,DBA')

INSERT INTO Employee_Profile(EmployeeID,ProfileId)
Values(101,1)


INSERT INTO Employee_Profile(EmployeeID,ProfileId)
Values(102,2)
INSERT INTO Employee_Profile(EmployeeID,ProfileId)
Values(103,3)

