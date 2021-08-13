# Feastv 0.12 sample

## Reference
 - https://docs.feast.dev/getting-started

## Prepare
    - Create S3 bucket (optional)
        Not use in tutorial.
    - Create Redshift Cluster
        - Need to assume IAM role to FullAccess to S3
    - Create EC2 instance to execute feast core.
        - Need to attach IAM role to FullAccess to S3, DynamoDB and Redshift.

## Procedure
- install feast for aws
```
pip install 'feast[aws]'
```
- create feature repository on local
```
feast init it aws
```
- demo on Feast
```
python3 test_myself.py
```
