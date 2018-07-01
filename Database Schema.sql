CREATE Table Employee
(
  EmployeeId INT Primary key,
  Name Varchar(100),
  Age INT,
  Mobile varchar(12),
  Location varchar(100)
)

CREATE table SkillSet
(
  SkillId int primary key,
  Name varchar(50)
)

CREATE Table Employee_Skill
(
  EmployeeId INT,
  SkillId INT,  
  Proficiency float,
  experience float
  constraint Employee_Fk foreign key(EmployeeId) references Employee,
  constraint SkillId_Fk foreign key(skillId) references SkillSet,
  constraint Employee_Skill_pk primary key(EmployeeId,SkillId) 
)

CREATE Table Profile
(
   ProfileId INT,
   ProfileName varchar(100),
   ProfileAliases varchar(2000)
) 

CREATE TABLE Employee_Profile
(
   ProfileId INT,
   EmployeeId INT
)