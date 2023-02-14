
# AWS CDK Pipeline Python project!

- The `cdk.json` file tells the CDK Toolkit how to execute your app.
- The initialization process also creates a virtualenv within this project, stored under the `.venv` directory. 
- To create the virtualenv it assumes that there is a `python3` executable in your path with access to the `venv`package.
- If for any reason the automatic creation of the virtualenv fails, you can create the virtualenv manually. To manually create a virtualenv on MacOS and Linux:<br>
`python3 -m venv .venv`
## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

## Preliminary preparations
* After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.<br>
`source .venv/bin/activate`
* `python3 -m pip install --upgrade pip` 
* Once the virtualenv is activated, you can install the required dependencies.<br>
`pip install -r requirements.txt`
* `brew upgrade awscli` for MacOS 
* `aws --version` 
* `brew upgrade aws-cdk` for MacOS
* `cdk --version`
* At this point you can now synthesize the CloudFormation template for this code.<br>
`cdk synth`
* To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Create Pipeline with AWS CDK





