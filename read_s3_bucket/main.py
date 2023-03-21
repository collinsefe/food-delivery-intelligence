import boto3
import pandas as pd


def read_s3_file(bucket, key):
    s3 = boto3.client('s3',
                      aws_access_key_id="{ ACCESS_KEY_ID }",
                      aws_secret_access_key="{ AWS_SECRET_ACCESS_KEY }")

    obj = s3.get_object(Bucket=bucket, Key=key)
    df = pd.read_csv(obj['Body'])
    print(df)
    return df

read_s3_file("uk-naija-datascience-21032023", "omolewa.csv")