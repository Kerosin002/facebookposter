#from tokenize import group
import pyodbc


def rowCount(groupArr):
    conn=pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=main-server-nych.database.windows.net;DATABASE=ElTime;UID=CloudSA66f830c2;PWD=Levis2009')
    cursor=conn.cursor()
    #query=("select count(id) from FaceBookGroups")
    query=("select * from FaceBookGroups")
    for row in cursor.execute(query):
        print(row.id,row.GroupName,row.Link,row.AnonPost)
        strLink=row.Link
        sl=strLink.rfind('/')
        idLink=strLink[sl+1:]
        groupArr.append(idLink)
   