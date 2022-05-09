import boto3
client=boto3.client('s3')
s3=boto3.resource('s3')

##TO CREATE BUCKET
# bucket=s3.create_bucket(Bucket='bucket1-jae',CreateBucketConfiguration={
#     'LocationConstraint':'ap-south-1'
# })

##FILE UPLOAD TO S3 BUCKET
# s3.meta.client.upload_file('D:\Aroha_Tech\python_vishwanath\oops\Aroha_Assignments\Python_Aroha1\Total_Construction_Cost_of_Healthcare_Projects.csv', 'bucket1-jae', 'construction.csv')

##FILE DOWNLOAD FROM S3 BUCKET  
#s3.Bucket('bucket1-jae').download_file('hello.txt', 'JAE2.txt')
my_bucket=s3.Bucket('bucket1-jae')
for my_bucket_object in my_bucket.objects.all():
    print(my_bucket_object.key)
