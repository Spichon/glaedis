#!/usr/bin/env bash

touch .env

cat > .env << EOL
COGNITO_USER_POOL_CLIENT_ID=$(aws cloudformation describe-stacks --stack-name glaedis-cognito-master --query "Stacks[0].Outputs[?OutputKey=='CognitoUserPoolClientId'].OutputValue" --output text)
COGNITO_USER_POOL_ID=$(aws cloudformation describe-stacks --stack-name glaedis-cognito-master --query "Stacks[0].Outputs[?OutputKey=='CognitoUserPoolId'].OutputValue" --output text)
AWS_REGION=eu-west-1
REDIRECT_URL=https://www.${ROOT_DOMAIN}
ROOT_DOMAIN=${ROOT_DOMAIN}
USER_API=https://user.${ROOT_DOMAIN}
TEST_API=https://test.${ROOT_DOMAIN}
EOL
