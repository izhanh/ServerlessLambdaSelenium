# ServerlessLambdaSelenium
Run Webdriver tests in Lambda with Serverless Framework + Python

## Requirements

(With Serverless)
* Serverless Framework `npm install serverless`
  * Python specific lib `serverless-python-requirements`
* Confifure your Serverless AWS creds
  * `export AWS_ACCESS_KEY_ID=<your-key-here>`
  * `export AWS_SECRET_ACCESS_KEY=<your-secret-key-here>`
* Deploy! `sls deploy`

(Pure AWS)
* Zip the entire folder and upload it to AWS Lambda
