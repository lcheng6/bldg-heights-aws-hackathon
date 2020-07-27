import boto3
from botocore.exceptions import ClientError
import lasutility

def initiate_ecs_task_run_for_las_file(lasfilename):
  ecs_client = boto3.client('ecs')
  response = ecs_client.run_task (
    # launchType = 'FARGATE',
    capacityProviderStrategy = [
      {
        'capacityProvider' : 'FARGATE_SPOT'
      }
    ],
    cluster = "ecscluster-urbaninst-dev",
    count = 1,
    taskDefinition= "urbaninst-dev-lidarprocessing",
    networkConfiguration = {
      'awsvpcConfiguration': {
        'subnets': [
          'subnet-0f2296d1facaad0d1',
          'subnet-076aed91c3669be38',
          'subnet-04b284cd9799f101b',
        ],
        'securityGroups': [
          'sg-0b88a78a4862aae3e',
        ],
        'assignPublicIp': 'DISABLED'
      }
    },
    group = "family:urbaninst-dev-lidarprocessing",
    overrides = {
      'containerOverrides': [
        {
          'command': ['--laskey',lasfilename],
          'name':'urbaninst-dev-lidarprocessing'
        }
      ]
    }
  )
  print(response)

def mainfunction():
  laskeynames = lasutility.get_las_file_names()
  # laskeynames = laskeynames[1:2] #pick a small subset to play with
  for laskeyname in laskeynames:
    keysequencenum = laskeyname.split('.')[0] #get the #### of the file "####.las"
    lasfilename = f"{keysequencenum}.las"
    print("process file: ", lasfilename)
    initiate_ecs_task_run_for_las_file(lasfilename)


mainfunction()