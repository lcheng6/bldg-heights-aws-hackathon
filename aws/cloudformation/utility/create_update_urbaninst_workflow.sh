#!/usr/bin/env bash

#use example
#./create_update_environment <update or create> <stackname>

action=$1
stackName=$2

. ./library_functions/library_funcs.sh --source-only

if [ "X$stackName" == "XUrbanInstWorkFlow-us-east-1" ]
then
    export AWS_DEFAULT_REGION=us-east-1
    export AWS_PROFILE=urban-institute-infranetseccf
#    export AWSSecretId=shared-services-infranetsec-cf-user
    export cloudformation_bucket=cf-templates-j3atw72be18l-us-east-1

    #Load in the AWS Credential for the Shared Services Cloudformation User
#    load_aws_credentials_into_env_from_secrets_manager $AWSSecretId useast1

    #Create the cloudformation S3 bucket if it doesn't exist
    create_s3_bucket_if_not_exists $cloudformation_bucket useast1

    #Debug statements to ensure AWS_ACCESS environment are properly loaded
    # echo $AWS_ACCESS_KEY_ID
    # echo $AWS_SECRET_ACCESS_KEY

    aws s3 sync ../workflow-stack/ s3://${cloudformation_bucket}/urban-institute-workflow-stack/ --delete

    if [ "X$action" == "Xupcreate" ]
    then
      #Detect whether the named stack exists
      aws cloudformation describe-stacks --stack-name $stackName > /dev/null 2>&1
      exitCode=$?
      if [ $exitCode -ne 0 ]
      then
        #the stack doesn't exist
        action='create'
      else
        action='update'
      fi
    fi

    if [ "X$action" == "Xupdate" ]
    then
        #do update
        aws cloudformation update-stack --stack-name $stackName \
            --template-url https://s3.amazonaws.com/${cloudformation_bucket}/urban-institute-workflow-stack/step_010_01_instantiate_workflow.yaml \
            --parameters file://../workflow-stack/workflow-stack-params.json \
            --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND

    elif [ "X$action" == "Xcreate" ]
    then
        #do create
        aws cloudformation create-stack --stack-name $stackName \
            --template-url https://s3.amazonaws.com/${cloudformation_bucket}/urban-institute-workflow-stack/step_010_01_instantiate_workflow.yaml \
            --parameters file://../workflow-stack/workflow-stack-params.json \
            --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND

    elif [ "X$action" == "Xwait" ]
    then
        aws cloudformation wait --stack-name $stackName

    elif [ "X$action" == "Xstack-status" ]
    then
        response=$(aws cloudformation describe-stacks --stack-name $stackName)
        statusStatus=$(echo $response | jq -r .Stacks[0].StackStatus)
        echo $statusStatus
    elif [ "X$action" == "Xdelete" ]
    then
        #do delete
        aws cloudformation delete-stack --stack-name $stackName
    fi

fi

#do an unload command here just to be safe
unload_aws_credentials_from_env