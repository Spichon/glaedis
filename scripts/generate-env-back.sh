#!/usr/bin/env bash

cat > .env <<EOL
COGNITO_USER_POOL_ID=$(aws cloudformation describe-stacks --stack-name glaedis-cognito-${TRAVIS_BRANCH} --query "Stacks[0].Outputs[?OutputKey=='CognitoUserPoolId'].OutputValue" --output text)
COGNITO_USER_POOL_CLIENT_ID=$(aws cloudformation describe-stacks --stack-name glaedis-cognito-${TRAVIS_BRANCH} --query "Stacks[0].Outputs[?OutputKey=='CognitoUserPoolClientId'].OutputValue" --output text)
COGNITO_REGION=eu-west-1
DB_URL=$(aws cloudformation describe-stacks --stack-name glaedis-rds-stack-${TRAVIS_BRANCH} --query "Stacks[0].Outputs[?OutputKey=='EndpointMaster'].OutputValue" --output text)
DB_URL_REPLICA=$(aws cloudformation describe-stacks --stack-name glaedis-rds-stack-${TRAVIS_BRANCH} --query "Stacks[0].Outputs[?OutputKey=='PortReadReplica'].OutputValue" --output text)
DB_NAME=$(aws cloudformation describe-stacks --stack-name glaedis-rds-stack-${TRAVIS_BRANCH} --query "Stacks[0].Outputs[?OutputKey=='DBName'].OutputValue" --output text)
DB_USER=$(aws cloudformation describe-stacks --stack-name glaedis-rds-stack-${TRAVIS_BRANCH} --query "Stacks[0].Outputs[?OutputKey=='DBUser'].OutputValue" --output text)
DB_PASSWORD=$(aws cloudformation describe-stacks --stack-name glaedis-rds-stack-${TRAVIS_BRANCH} --query "Stacks[0].Outputs[?OutputKey=='DBPassword'].OutputValue" --output text)
SECRET_KEY=$(aws cloudformation describe-stacks --stack-name glaedis-rds-stack-${TRAVIS_BRANCH} --query "Stacks[0].Outputs[?OutputKey=='SecretKey'].OutputValue" --output text)
PROJECT_NAME=Glaedis
COIN_MARKET_CAP_API_KEY=$(aws cloudformation describe-stacks --stack-name glaedis-rds-stack-${TRAVIS_BRANCH} --query "Stacks[0].Outputs[?OutputKey=='CoinMarketCapApiKey'].OutputValue" --output text)
EOL
