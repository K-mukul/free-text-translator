
import pytrie
import pyodbc
import time

class SearchBox:
    tr = pytrie.StringTrie()

    def __init__(self):
        try:
            server = 'fopo2ibguo.database.windows.net'
            database = 'testingdacpac'
            username = 'devuser'
            password = 'Passw0rd'
            driver = 'ODBC Driver 13 for SQL Server'
            self.conn = pyodbc.connect(
                'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1443;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

        except:
            print ("I am unable to connect to the database")
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT  distinct Location from Employee")
        rows = self.cursor.fetchall()
        for row in rows:
            self.tr.__setitem__(row[0], ['Location',  row[0]])

        self.cursor.execute("SELECT  * from profile")
        rows = self.cursor.fetchall()
        for row in rows:
            self.tr.__setitem__(row[1], ['ProfileId', row[0]])
            for alias in row[2].split(','):
                self.tr.__setitem__(alias, ['ProfileId',  row[0]])

        self.cursor.execute("SELECT  * from skillset")
        rows = self.cursor.fetchall()
        for row in rows:
            try:
                self.tr.__setitem__(row[1], ['SkillId',  row[0]])
            except:
                pass

    def contains(self, string):
        try:
            return self.tr.__getitem__(string)
        except:
            return []

    def listToString(self, fieldName, listOfString):
        listString = ""
        i = 0;
        listLength = len(listOfString)
        print("LENGTH OF ", listLength)
        while i < listLength:

            # for item in listOfString:
            if listString == "":
                listString = " ( " + fieldName + " = " + str(listOfString[i])
            else:
                listString += " or " + fieldName + " = " + str(listOfString[i])
            i += 1
        return listString + " )"

    def rowToList(self, rowList):
        rowString = " in ("
        for row in rowList:
            rowString += str(row[0]) + ","
        return rowString[:-1] + ")"

    def search(self, searchString):
        #searchString = searchString.lower()
        startTime = time.time()

        token = searchString.split(' ')
        expr = 0
        queryString = ""
        tokenLength = len(token)
        i = 0
        type = []
        fieldStorage = {None: [None]}
        fieldNameStorage = {None: None}


        i = 0
        prevField = None
        while i < tokenLength:

            type = self.contains(token[i])

            if(len(type) ==0 and i < tokenLength - 1):
                type = self.contains(token[i]+ " "+ token[i+1])
                if(len(type) == 0 and i < tokenLength - 2):
                    type= self.contains(token[i]+ " "+ token[i+1] +" "+ token[i+2])


            if len(type) > 0:
                print(token[i], type[0], "'" + type[0] + "'", type[1])
                fieldNameStorage["'" + type[0] + "'"] = type[1]
                try:

                    if type[0] == "experience":
                        j = 1
                        flag = True
                        while (i + j < tokenLength or i - j > 0) and flag:
                            try:

                                expr = int(token[i + j])
                                flag = False

                            except:
                                pass
                            if flag == True:
                                try:
                                    expr = int(token[i - j])
                                    flag = False
                                except:
                                    pass
                            j += 1
                        try:
                            print(expr)

                            fieldStorage["'" + type[0] + "'"].append(expr)
                        except:
                            fieldStorage["'" + type[0] + "'"] = [expr, ]
                    else:
                        if type[0] in fieldStorage:
                            fieldStorage[type[0]].append(type[1])
                            prevField = type[0]
                        else:
                            fieldStorage[type[0]]=[type[1], ]
                            prevField = type[0]
                except:
                    pass
            i += 1
        fieldFlag = False
        for item in fieldStorage:

            if item != None:
                if fieldFlag == False:
                    queryString += " select * from Employee_View where " + self.listToString(item, fieldStorage[item])
                    fieldFlag = True
                else:
                    queryString += " and " + self.listToString(item, fieldStorage[item])

        print (queryString)

        self.cursor.execute(queryString)
        rows = self.cursor.fetchall()


        for row in rows:
            print(row)
            i+=1
            if i==40:
                i=0
                input()



s = SearchBox()
s.search(input("Type Your Query "))
s.search(input("Type Your Query "))
s.search(input("Type Your Query "))
