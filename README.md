<h1 align="center">ComiXology's Weekly Featured New Releases ETL</h1>

<h3 align="center">🧰 Languages and Tools</h3>
<p align="center">
<img src="https://user-images.githubusercontent.com/97479656/214594812-e19961c9-00cd-4c7a-9c56-5b8b45f9ed13.png">
</p>
<hr>

### Purpose:
* Every week, there are new comic books getting released on Amazon's cloud-based digital distribution platform for comics, [ComiXology](https://www.amazon.com/kindle-dbs/comics-store/home/ "Amazon's ComiXology"). As a comic book enthusiast, I wanted to create an ETL process that is automated using AWS services, extracts the appropriate data, transformed by Python, and is loaded into a CSV file, that would then be stored in Amazon S3.
#

<div>

<table align="center">

<tr>
<td>⚙ ETL Process:</td>
<td>AWS Diagram</td>
</tr>

<tr>
<td width="50%">
<ol>
<li>Every Tuesday at 9am, a cron job using <a href="https://aws.amazon.com/eventbridge/scheduler/">Amazon EventBridge Scheduler</a> will call for an <a href="https://aws.amazon.com/lambda/">AWS Lambda</a> function that is an ETL process created with Python to collect ComiXology's weekly featured new releases.</li>
<br>
<li>The ETL process will start with the extraction of the data using <a href="https://beautiful-soup-4.readthedocs.io/en/latest/">BeautifulSoup</a>.</li>
<br>
<li>Once the data has been extracted, there will be a process of data cleaning and formatting, so that it can be loaded into a CSV file.</li>
<br>
<li>After the cleaning, a CSV file will be created, then the data will be loaded into it (Which will end the ETL process).</li>
<br>
<li>With the completion of the ETL process, the recently created CSV file will be stored in <a href="https://aws.amazon.com/s3/">AWS S3</a>. This is possible with <a href="https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html">Boto3</a>, an AWS SDK for Python (This will be the end of the first Lambda function).</li>
<br>
<li>The storing of the file will then trigger another Lambda function that was set to be triggered when an object has been created in the defined S3 bucket.</li> 
<br>
<li>Once triggered, the Python script within the Lambda function will publish a message and send it to my email, that is a subscriber to a Topic I have created in <a href="https://aws.amazon.com/sns/">SNS</a>.</li> 
</ol>
</td>

<td>
<img height="100%" width="100%" src="https://user-images.githubusercontent.com/97479656/214634385-496ebeb6-ab5b-4c9c-b904-5344ff3aec67.png">
</td>
</tr>

</table>

</div>
