import requests
import lxml.html


url = "http://results.logisys.org//reva//app.php?a=DisplayStudentResult"  

session = requests.session()

semister ={                
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
                res['Status'] = 'OK'
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
                print( {
                        "Code":400,
                        "Status":"Error",
                        "Error":"No record found or invalid input. "

                })





         





def printResults(Srn,Sem):
        try:
                payload = {
                "r":Srn,
                "e":semister[Sem]
                }
                result = get_results(payload)
                print(result)
        except:
                print({
                        "Code":"400",
                        "Status":"Bad Request/Invalid Input",
                        "Message":" You have entred Sem: "+Sem+" which is invalid" 
                        })
        


srn,sem = input("Enter the Srn:") , input("Enter the Semister:")

printResults(srn,sem)