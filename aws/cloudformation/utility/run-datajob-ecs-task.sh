
export AWS_PROFILE=urban-institute-infranetseccf
aws ecs run-task \
  --launch-type 'FARGATE' \
  --cluster 'ecscluster-urbaninst-dev' --count 1 \
  --task-definition "urbaninst-dev-lidarprocessing" \
  --network-configuration 'awsvpcConfiguration={subnets=[subnet-0f2296d1facaad0d1,subnet-076aed91c3669be38,subnet-04b284cd9799f101b],securityGroups=[sg-0b88a78a4862aae3e],assignPublicIp=DISABLED}' \
  --group "family:urbaninst-dev-lidarprocessing" \
  --overrides "{\"containerOverrides\": [{\"command\": [\"--laskey\",\"1122.las\"],\"name\":\"urbaninst-dev-lidarprocessing\"}]}"


unset AWS_PROFILE
