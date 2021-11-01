import requests
from bs4 import BeautifulSoup


url = "http://results.logisys.org//reva//app.php?a=DisplayStudentResult"  

session = requests.session()



payload = {
"r":"r19cs267",
"e":"D"
}


r = session.post(url,data=payload)

print(r.content)

soup = BeautifulSoup(r.content,'html5lib')

#print(r.content)

table = soup.select_one(".result_table_footer")
print(table)
