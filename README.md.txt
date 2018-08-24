# Logs Analysis - Udacity
### Full Stack Web Development ND
_______________________
## About
The project has three questions.

- Q1. What are the most popular three articles of all time?.
- Q2. Who are the most popular article authors of all time?.
- Q3. On which days did more than 1% of requests lead to errors?.


## Prerequisites
	* Git [https://git-scm.com/downloads]
	* Python [https://www.python.org/downloads/]
	* Virtual box[https://www.virtualbox.org/wiki/Download_Old_Builds_5_1]
	* Vagrant [https://www.vagrantup.com/]
	* Download the Virtual Machine [https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip]


## Follow the steps below

-  Unzip "fsnd-virtual-machine.zip" located on downloads folder
-  Go to unziped directory (fsnd-virtual-machine\FSND-Virtual-Machine\vagrant) 
-  Right click and select the option "Git bash here"
-  Run command "vagrant up"
-  Run command "vagrant ssh"
-  Go to shared directory run command "cd /vagrant"
-  Run command "psql -d new -f newsdata.sql"
-  Run command "psql news"

## Create views

	-  create view daily_total as select time::date,count(time::date) from 	log group by time::date order by 2 desc;
	-  create view failed as select time::date,count(time::date) from log 	where status like '%404%' group by time::date order by 2 desc;
	-  create view daily_perc as select daily_total.time,(failed.count *100.0 / daily_total.count )perc from daily_total,failed where daily_total.time=failed.time order by 2 desc;

## Run the .py file

 - Run command "python log.py"
