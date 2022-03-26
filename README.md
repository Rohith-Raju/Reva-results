# Reva-results
Reva-results is a python script that scrapes the Reva result website and displays the result of the student as its output.

## Getting started
### Libraries that need to be installed
Use pip to install for ex: pip install requests 
1) requests
2) lxml

### Running the script
You can run the script by typing ```python3 script.py``` in your command line and provide the following inputs:
1) Srn
2) Semister
```
Enter the Srn:r19cs261
Enter the Semister:Fifth
```

### Output
If everything goes well the results of all the subjects will be displayed.
```
{
'Code': 200, 
'Status': 'OK', 
'Srn': 'R19CS261', 
'Name': ' ROHITH  K', 
'Results': {
            'Python for Data Analysis': '27.00', 
            'Computer Networks': '30.00', 
            'Operating Systems': '40.00', 
            'IoT Programming and Applications': '21.00', 
            'Unix System Programming': '27.00', 
            'Statistical Data Analysis Lab': '20.00', 
            'Computer Networks Lab': '18.00', 
            'Skill Development -5': '9.00'}, 
            'SGPA': ' 9.12'
             }
} 
```
