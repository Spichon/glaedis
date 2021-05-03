#!/usr/bin/env bash

cat > .env.alembic <<EOL
DB_URL=$(aws cloudformation describe-stacks --stack-name glaedis-rds-stack-${TRAVIS_BRANCH} --query "Stacks[0].Outputs[?OutputKey=='EndpointMaster'].OutputValue" --output text)
DB_URL_REPLICA=$(aws cloudformation describe-stacks --stack-name glaedis-rds-stack-${TRAVIS_BRANCH} --query "Stacks[0].Outputs[?OutputKey=='PortReadReplica'].OutputValue" --output text)
DB_NAME=$(aws cloudformation describe-stacks --stack-name glaedis-rds-stack-${TRAVIS_BRANCH} --query "Stacks[0].Outputs[?OutputKey=='DBName'].OutputValue" --output text)
DB_USER=$(aws cloudformation describe-stacks --stack-name glaedis-rds-stack-${TRAVIS_BRANCH} --query "Stacks[0].Outputs[?OutputKey=='DBUser'].OutputValue" --output text)
DB_PASSWORD=$(aws cloudformation describe-stacks --stack-name glaedis-rds-stack-${TRAVIS_BRANCH} --query "Stacks[0].Outputs[?OutputKey=='DBPassword'].OutputValue" --output text)
EOL

export $(cat .env.alembic | xargs)
