# ComiXology's Weekly Featured New Releases ETL

### Purpose:
* Every week, there are new comicbooks getting release on Amazon's cloud-based digital distribution platform for comics, [ComiXology](https://www.amazon.com/kindle-dbs/comics-store/home/ "Amazon's ComiXology"). As a comicbook enthusiast, I wanted to create an ETL process that is automated using AWS services, load the data in a CSV file, and would store the CSV file of the weekly releases in Amazon S3. In order to do so, I used AWS Step Functions to create a cron job that will be called upon every Monday at 6pm 


### Tools:
* Python
* Scrapy (Python Package)
* AWS Lambda
* AWS Step Functions
* Amazon EventBridge Schedule
* Amazon Simple Storage Service (S3)
* Amazon Simple Notifaction Service (SNS)


### ETL Process:
1. Every Monday at 6pm, a cron job using EventBridge Schedule will call for a Step Function workflow to collect [ComiXology's](https://www.amazon.com/kindle-dbs/comics-store/home/ "Amazon's ComiXology"), an Amazon cloud-based digital distribution platform for comics, weekly featured new releases.
2. Withing that workflow, there are two Lambda function will trigger a Python script that will web scrape  
3. Another Lambda function will trigger a message dir
4. 
5. 

![comixology_new_releases drawio](https://user-images.githubusercontent.com/97479656/214044955-92951e6b-d952-4048-a5b9-a54cc75e82a5.png)

