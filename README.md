# Search\_Excel\_Demo
## Introduction
This Demo read and clean excel data by Python(Jupyter Notebook)-openpyxl, write data to MySQL by Pandas. Django as backend, HTML and jQuery are frontend of searching data list in webpage.


### Website Draft
When I received this case, the first day I design the main page draft.
![Draft](https://github.com/lingwsh/Search_Excel_Demo/blob/main/img/01_draft.jpg?raw=true)
### Final website result
#### Main search Page
The main search box can blur serach three fields.
![Search Page](https://github.com/lingwsh/Search_Excel_Demo/blob/main/img/03_search_page.png?raw=true)
#### Detail information page 
After click "More" in each row, the new webpage will show detail information.
![Detail Page](https://github.com/lingwsh/Search_Excel_Demo/blob/main/img/04_detail_page.png?raw=true)
#### Video display search result and function explaination

<iframe width="560" height="315" src="https://www.youtube.com/embed/gHfbImUKDls" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## Technical used in this Demo
### IDE 
<ul>
  <li>PyCharm</li>
</ul>

### Language and Framework
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
More technical details are in log file. I record these information in an Excel, please [Download](https://github.com/lingwsh/Search_Excel_Demo/blob/main/work_time_log.xlsx) and read it in local.

## Future Scalable Design
### Does the data need to be pre-processed?
Usually data needs to be checked before it is imported into the database, for example: handling null, validating the format of different fields, etc. I don't know too much about the given file fields and I will spend more time on Django, so I imported the data directly into the database in this case.
### In what ways is the amount of data a problem?
When the volume of data is large, MySQL search speed will be slowed down, so you can add index to the query fileds or use a split table and database. These traditional methods, of course, have improved performance in MongoDB. I have not used MongoDB before, but I am very interested in learning how to use it ASAP. 
### How to solve the problem escalate as more data is added in the future? 
Some ideas may help to solve this problem. The main objective is to minimise manual work and automate the processing of the new data.
<ol>
  <li>If the data is provide from third party, using E-mail ,FTP or other file transfer methods automately receive update data file from different data source. If the source can confirm different period data is not repeated, our system can append these data to database. Otherwise, the system has to check each data record are new in the database.</li>
  <li>If we have the access to the datasource, we can extract the new data by code Periodically. But this situation may not the daily case. Database auto backup is not new. My previous work, we used [Oracle GoldenGate](https://www.oracle.com/integration/goldengate/) for high-speed synchronisation between databases. It is good tool, but not free. </li>
</ol>
### Some usability concerns
Although I did not do time filtering in this case, but according to my experience using PowerBI and Tableau, the order query system can add a powerful time filtering management tools can help users to quickly filter time and generate reports.

<ol>
  <li>According to the dimensions of day, week, month, quarter, year, automatically calculate the summary data of the filter results, such as the total number of orders, total sales, etc.. This function can be used to automatically generate reports.
</li>
  <li>Data for the last n days/weeks/months. This function allows users to quick search for recent data.
</li>
  <li>Fixed time period filtering. General functionality for date filtering.</li>
</ol>

## Deploy Demo in Local Environment
For data security reason, please use provided Excel to creat MySQL table and import data by Python code. I do not upload any data information in Github.

Please follow these steps to start the project in local.

1.Install necessary package by this code:
 <p> pip install -r [requests.txt](https://github.com/lingwsh/Search_Excel_Demo/blob/main/orders_manage_system/requests.txt)

2.run this code in local, import Excel to MySQL database. Remenmber to change the MySQL connection information.
 <p> [creat database by Excel](https://github.com/lingwsh/Search_Excel_Demo/blob/main/create_database_by_excel.py)

3.Change MySQL connection information, [config file](https://github.com/lingwsh/Search_Excel_Demo/blob/main/orders_manage_system/orders_manage_system/settings.py)

4.Run Django at project file by code
 <p>python manage.py runserver
