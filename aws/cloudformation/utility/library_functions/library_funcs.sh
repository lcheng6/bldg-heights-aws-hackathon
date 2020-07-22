#!/bin/bash

#this assumes jq program is already installed
create_s3_bucket_if_not_exists() {
  local bucketname=$1
  local region=$2
  local mbResult
  local REGION='us-east-1' #default region for bucket
  if [ "X$region" == "Xuseast1" ]
  then
    REGION='us-east-1'
  elif [ "X$region" == "Xuseast2" ]
  then
    REGION='us-east-2'
  elif [ "X$region" == "Xeuwest1" ]
  then
    REGION='eu-west-1'
  else
    REGION='us-east-1' #default region for bucket
  fi

  aws s3 ls "s3://$bucketname" 2>&1 | grep -q 'NoSuchBucket'
  bucketExists=$?
  if [ $bucketExists == "0" ]
  then
    echo $bucketname
    echo $REGION
    mbResult=`aws s3 mb "s3://$bucketname" --region $REGION`
    echo $mbResult
    if ( echo $mbResult | grep -q "not available" )
    then
      #print out the error to STDERR
      echo "S3 bucket $bucketname already exists"
    elif ( echo $mbResult | grep -q "$bucketname" )
    then
      echo "S3 bucket $bucketname was successfully created"
      echo "Configuring $bucketname for versioning, encryption, and policy"
      #Need to give AWS some time in the backend to recognize that the bucket has been created
      sleep 15
      #turn on versioning
      aws s3api put-bucket-versioning --bucket $bucketname --versioning-configuration Status=Enabled --region $REGION
      #Set encryption
      aws s3api put-bucket-encryption --bucket $bucketname --server-side-encryption-configuration '{"Rules": [{"ApplyServerSideEncryptionByDefault": {"SSEAlgorithm": "AES256"}}]}' --region $REGION
      #Set no public access policy
      aws s3api put-public-access-block \
        --bucket $bucketname \
        --public-access-block-configuration "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true" \
        --region $REGION
    fi
  else
    echo "Bucket $bucketname already exists within account"
  fi

}

#Remove AWS Credential from Bash memory
unload_aws_credentials_from_env (){
  unset AWS_ACCESS_KEY_ID
  unset AWS_SECRET_ACCESS_KEY
  unset AWS_SESSION_TOKEN
  unset AWS_PROFILE
}

# load AWS credentials into environment variables
load_aws_credentials_into_env_from_secrets_manager(){
  local secretid=$1
  local region=$2
  #unset the previously defined AWS parameters
  unload_aws_credentials_from_env
  REGION='us-east-1' #default region for bucket
  if [ "X$region" == "Xuseast1" ]
  then
    REGION='us-east-1'
  elif [ "X$region" == "Xuseast2" ]
  then
    REGION='us-east-2'
  elif [ "X$region" == "Xeuwest1" ]
  then
    REGION='eu-west-1'
  else
    REGION='us-east-1' #default region for bucket
  fi

  SECRETSMANAGER_READER_PROFILE=lordabbett_shrsvc_cf_user

  #Get a secret string to test
  #secretvalue=`aws secretsmanager get-secret-value --secret-id backuprestore-prod-infranetsec-cf-user --profile $SECRETSMANAGER_READER_PROFILE`
  secretvalue=`aws secretsmanager get-secret-value --secret-id $secretid --profile $SECRETSMANAGER_READER_PROFILE --region $REGION`
  export AWS_ACCESS_KEY_ID=`echo $secretvalue |  jq '.SecretString' --raw-output | jq '.AWS_ACCESS_KEY_ID' --raw-output`
  export AWS_SECRET_ACCESS_KEY=`echo $secretvalue |  jq '.SecretString' --raw-output | jq '.AWS_SECRET_ACCESS_KEY' --raw-output`

}



