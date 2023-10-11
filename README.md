# BigDataTechnologies_CSP-554
Big Data Technologies CSP-554

//---------------------------------------------------------------------

Assignment : 01 Learnings : 

1)What is Amazon Web Services(AWS)
2)How to create the AWS account
3)What is  S3 bucket in AWS 
ANS : 	
		1)S3 is a Storage Service(ONE OF THE AMAZON PROVIDED SERVICES)
		2) It's an Object Storage System.
		
4)How to create S3 bucket and how to upload the files into s3 bucket
==================================================================================================

Assignment : 02 Learnings : 

1)what is AWS Terminal Window Capability ? 
2) To avoid unnecessary Billing usage. Setting alarm for Triggering Amount
3)What is Cluster ? 
       What does Hadoop Cluster Mean ? 
	   how can EMR "Elastic Map Reduce" relavent to Hadoop Product ?
4)HDFS - Hadoop Distributed File System

5)EMR ? Analytics Service(ONE OF THE AMAZON PROVIDED SERVICES)
  Analytics mean insights(Tracking what and all the services are up/running)
6)COMPLETED : AWS Cost Management Instructions.
       Created Alert
7)EMR(Elastic Map Reduce) Cluster

Amazon EMC2 :  Amazon Elastic Compute Cloud 	
*********Created Private Key and saved in the Assignment_02/privateKey Folder

Step 5: Launch Your Initial Amazon EMR Cluster

1)
How to create Cluster/Virtual System
1)Create EC2 Key  (Key Pair)
2)Create role (IAM)
3)Server configuration(m4.large, m5.large of Cluster(server) Specifications)

------------------------------
10/10/2023 updated
ec2-18-216-214-97.us-east-2.compute.amazonaws.com


//git to emr Cluster by open Git bash in our system 
ssh -i /D/2023/000_fall_2023Sem2/BigData_CSP-554/Assignment/02/emr-key-pair.pem hadoop@ec2-18-216-214-97.us-east-2.compute.amazonaws.com

//to send files from the system to cluster by open another Git bash in our system 
scp -i /D/2023/000_fall_2023Sem2/BigData_CSP-554/Assignment/02/emr-key-pair.pem /D/2023/000_fall_2023Sem2/BigData_CSP-554/Assignment/04/TestDataGen.class hadoop@ec2-18-216-214-97.us-east-2.compute.amazonaws.com:/home/hadoop

//to check whether the files transfered/copied to cluster from our local file 
//in emr git bash 
command : ls

//run the file in emr Cluster 
//how to run the files(java/python) in the emr cluster 
command : java TestDataGen



D/2023/000_fall_2023Sem2/BigData_CSP-554/Assignment/03/WordCount

home hadoop

hadoop@ec2-52-15-123-62.us-east-2.compute.amazonaws.com

hadoop fs -put /home/hadoop/w.data /user/hadoop

hadoop fs -ls

ec2-52-15-123-62.us-east-2.compute.amazonaws.com

scp -i /D/2023/000_fall_2023Sem2/BigData_CSP-554/Assignment/02/emr-key-pair.pem /D/2023/000_fall_2023Sem2/BigData_CSP-554/Assignment/03/WordCount.py hadoop@ec2-52-15-123-62.us-east-2.compute.amazonaws.com:/home/hadoop


ec2-52-15-123-62.us-east-2.compute.amazonaws.com

scp -i /D/2023/000_fall_2023Sem2/BigData_CSP-554/Assignment/02/emr-key-pair.pem /D/2023/000_fall_2023Sem2/BigData_CSP-554/Assignment/03/w.data hadoop@ec2-52-15-123-62.us-east-2.compute.amazonaws.com:/home/hadoop

----------------------------------
new

ec2-3-144-219-59.us-east-2.compute.amazonaws.com

scp -i /D/2023/000_fall_2023Sem2/BigData_CSP-554/Assignment/02/emr-key-pair.pem /D/2023/000_fall_2023Sem2/BigData_CSP-554/Assignment/03/user.py hadoop@ec2-3-144-219-59.us-east-2.compute.amazonaws.com:/home/hadoop

scp -i /D/2023/000_fall_2023Sem2/BigData_CSP-554/Assignment/02/emr-key-pair.pem /D/2023/000_fall_2023Sem2/BigData_CSP-554/Assignment/03/test.data hadoop@ec2-3-144-219-59.us-east-2.compute.amazonaws.com:/home/hadoop

hadoop fs -put /home/hadoop/w.data /user/hadoop


ssh -i /D/2023/000_fall_2023Sem2/BigData_CSP-554/Assignment/02/emr-key-pair.pem hadoop@ec2-3-144-219-59.us-east-2.compute.amazonaws.com

-----------------------------------------------------------------

ec2-3-144-219-59.us-east-2.compute.amazonaws.com

