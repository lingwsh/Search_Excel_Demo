# Search\_Excel\_Demo
## Introduction
This Demo read and clean excel data by Python(Jupyter Notebook)-openpyxl, write data to MySQL by Pandas. Use Django as backend and simple HTML apply function of searching data list in webpage.

After click "More" in each row, the new webpage will show detail information.

The main search box can blur serach three fields: 
### Website Draft
When I received this case, the first day I design the main page draft.
![Draft](https://github.com/lingwsh/Search_Excel_Demo/blob/main/img/01_draft.jpg)
### Final website result
#### Main search Page
#### Detail information page 
#### Video explaination

## Technical used in this Demo
<ul>
  <li>Python</li>
  <li>Pandas</li>
  <li>openpyxl</li>
  <li>MySQL</li>
  <li>Django</li>
  <li>Bootstrap</li>
  <li>HTML</li>
  <li>JavaScript</li>
</ul>

### Django URL design
This four URL are used in Django app Order. There are use for searching and return search results.
![Django_URL](https://github.com/lingwsh/Search_Excel_Demo/blob/main/img/02_Search_Excel_Django_URL1.png?raw=true)


## Log file and more design explaination
I record these information in Excel, please [Download](https://github.com/lingwsh/Search_Excel_Demo/blob/main/work_time_log.xlsx) and read in local.

## Future Scalable Design
### In what ways is the amount of data a problem?
### How to solve the problem escalate as more data is added in the future? 
Some ideas may help to solve this problem. The main objective is to minimise manual work and automate the processing of the new data.
<ol>
  <li>If the data is provide from third party, using E-mail ,FTP or other file transfer methods automately receive update data file from different data source. If the source can confirm different period data is not repeated, our system can append these data to database. Otherwise, the system has to check each data row are new in the database.</li>
  <li>If we have the access to the datasource, we can extract the new data by code Periodically. But this situation may not the daily case. Database auto backup is not new. My previous work, we used [Oracle GoldenGate](https://www.oracle.com/integration/goldengate/) for high-speed synchronisation between databases. It is good tool, but not free. </li>
</ol>
### Some usability concerns


## Deploy Demo in Local Environment
For data security reason, please use provided Excel to creat MySQL table and import data by Python code. I do not upload any data information in Github.
 