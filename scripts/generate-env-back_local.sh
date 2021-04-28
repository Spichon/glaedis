#!/usr/bin/env bash

cat > .env.temp <<EOL
DB_URL=$(aws cloudformation describe-stacks --stack-name glaedis-rds-stack-${TRAVIS_BRANCH} --query "Stacks[0].Outputs[?OutputKey=='EndpointMaster'].OutputValue" --output text)
DB_URL_REPLICA=$(aws cloudformation describe-stacks --stack-name glaedis-rds-stack-${TRAVIS_BRANCH} --query "Stacks[0].Outputs[?OutputKey=='PortReadReplica'].OutputValue" --output text)
DB_NAME=$(aws cloudformation describe-stacks --stack-name glaedis-rds-stack-${TRAVIS_BRANCH} --query "Stacks[0].Outputs[?OutputKey=='DBName'].OutputValue" --output text)
DB_USER=$(aws cloudformation describe-stacks --stack-name glaedis-rds-stack-${TRAVIS_BRANCH} --query "Stacks[0].Outputs[?OutputKey=='DBUser'].OutputValue" --output text)
DB_PASSWORD=$(aws cloudformation describe-stacks --stack-name glaedis-rds-stack-${TRAVIS_BRANCH} --query "Stacks[0].Outputs[?OutputKey=='DBPassword'].OutputValue" --output text)
PGADMIN_DEFAULT_EMAIL=pgadmin4@pgadmin.org
PGADMIN_DEFAULT_PASSWORD=admin
RABBITMQ_DEFAULT_USER=guest
RABBITMQ_DEFAULT_PASS=guest
EOL
