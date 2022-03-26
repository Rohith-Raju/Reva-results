import requests
import lxml.html
from flask import Flask 


url = "http://results.logisys.org//reva//app.php?a=DisplayStudentResult"  

session = requests.session()

sem ={                
        "First":"A",
        "Second":"B",
        "Third":"C",
        "Fourth":"D",
        "Fifth":"E",    
        "Sixth":"F",
        "Seventh":"G",
        "Eight":"H"
        }








def get_results(payload):
        response = session.post(url,data=payload,stream=True)
        print(response.raw)
        response.raw.decode_content = True
        tree = lxml.html.parse(response.raw)
        sliceConstructor = slice(12,20)
        res={}
        try:
                unfiltredSrn = tree.xpath('//table[@id="student_info"]/tr[2]/td/text()')[0]
                srn =  unfiltredSrn[sliceConstructor]
                unfiltredName = tree.xpath('//table[@id="student_info"]/tr[3]/td/text()')[0]
                name = (unfiltredName.split(':')[1].split('\\')[0])
                res['Code'] = 200
                res['Satus'] = 'OK'
                res['Srn'] = srn
                res['Name'] = name
                res['Results'] = {}

                for i in tree.xpath('.//table[@id="results_subject_table"]/tr')[0]: #xpath
                    subarray =  i.xpath('.//td[2]/text()')
                    marks = i.xpath('.//td[6]/text()')
                for i in range(1,len(subarray)-1):
                        res["Results"].update({subarray[i]:marks[i]})  

                res['SGPA'] = tree.xpath('.//table[@id="results_subject_table"]//table[1]//tr/td[1]/text()')[0].split(',')[0].split(":")[1] 
        
                return res
        except:
                return {
                        "Code":400,
                        "Status":"Error",
                        "Error":"No record found or invalid input. Ex results/r19cs261/Fourth "

                }




application = Flask(__name__)

@application.route('/')
def printWelcome():
        return "<h1>Hello There</h1>"+"<br>"+" <a href=""/results"">click here to query results</a>"
                



@application.route('/results')
def printTutorial():
        return "<h1>Append Srn and Semister to the url <h1>"+"<h4>Exapmle: results/r19cs261/Fourth<h4>"

@application.route('/results/<Srn>/<Sem>')
def printResults(Srn,Sem):
        try:
                payload = {
                "r":Srn,
                "e":sem[Sem]
                }
                result = get_results(payload)
                return result
        except:
                return {
                        "Code":"400",
                        "Status":"Bad Request/Invalid Input",
                        "Message":" You have entred Sem: "+Sem+" which is invalid" 
                        }
        

@application.route('/results/range/<from>/<to>')
def range():
        print("hello")




if __name__ == "__main__":
    application.run(port=5000, debug=True)