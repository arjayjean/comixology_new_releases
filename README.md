# ComiXology's Weekly Featured New Releases ETL

### Purpose:
* This project was my introduction into learning how to implement an ETL process with Python. My goal was to find out who was the best super hero and super villain in their respected universe and overall. In order to do so, I needed to take the stats for each individual character, that was provided, and calculate them into an overall rating.     

1. Every week, there are new comicbooks getting release on Amazon's cloud-based digital distribution platform for comics, [ComiXology](https://www.amazon.com/kindle-dbs/comics-store/home/ "Amazon's ComiXology"). As a comicbook enthusiast and aspiring Cloud Data Engineer, I wanted to learn how to create an ETL process that was automated using AWS services, load the data in a CSV file, and would store the CSV file of the weekly releases in Amazon S3. In order to do so, I used AWS Step Functions to create a cron job that will be called upon every Monday at 6pm 


### Requirements:
* Knowledge:
⋅⋅* Python
⋅⋅* Scrapy (Python Package)
⋅⋅* AWS Lambda
⋅⋅* AWS Step Functions
⋅⋅* Amazon EventBridge Schedule
⋅⋅* Amazon Simple Storage Service (S3)
⋅⋅* Amazon Simple Notifaction Service (SNS)


### ETL Process:
1. Every Monday at 6pm, a cron job using EventBridge Schedule will call for a Step Function workflow to collect [ComiXology's](https://www.amazon.com/kindle-dbs/comics-store/home/ "Amazon's ComiXology"), an Amazon cloud-based digital distribution platform for comics, weekly featured new releases.
2. Withing that workflow, there are two Lambda function will trigger a Python script that will web scrape  
3. Another Lambda function will trigger a message dir
4. 
5. 

![comixology_new_releases drawio](https://user-images.githubusercontent.com/97479656/213268895-04e6876a-6716-40e1-a1d9-804deec00128.png)

