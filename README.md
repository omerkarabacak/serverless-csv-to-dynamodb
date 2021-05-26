# Serverless Application for importing CSV files to DynamoDB
This serverless application created for automatically importing CSV files to DynamoDB which are uploaded into S3 bucket. It is a simple example for AWS Lambda Demo.

## Infrastructure

AWS CDK (Python) used for Infrastructure as Code (Seperate repository)

* DynamoDB
* S3 Bucket
* Lambda (Triggered with S3 object created event)

IaC repository: https://github.com/omerkarabacak/multi-stack-aws-cdk-python-iac-project
## CICD

Github Actions used for auto deploying the Lambda