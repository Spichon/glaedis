#!/usr/bin/env bash

cat > frontend/.env.temp <<EOL
DB_URL=$(aws cloudformation describe-stacks --stack-name glaedis-rds-stack-${TRAVIS_BRANCH} --query "Stacks[0].Outputs[?OutputKey=='EndpointMaster'].OutputValue" --output text)
DB_NAME=$(aws cloudformation describe-stacks --stack-name glaedis-rds-stack-${TRAVIS_BRANCH} --query "Stacks[0].Outputs[?OutputKey=='EndpointMaster'].OutputValue" --output text)
VUE_APP_COGNITO_USER_POOL_ID=$(aws cloudformation describe-stacks --stack-name glaedis-cognito-${TRAVIS_BRANCH} --query "Stacks[0].Outputs[?OutputKey=='CognitoUserPoolId'].OutputValue" --output text)
VUE_APP_AWS_REGION=eu-west-1
VUE_APP_REDIRECT_URL=https://www.${ROOT_DOMAIN}/
VUE_APP_ROOT_DOMAIN=${ROOT_DOMAIN}
VUE_APP_USER_API=https://user.${ROOT_DOMAIN}
VUE_APP_TEST_API=https://test.${ROOT_DOMAIN}
EOL
