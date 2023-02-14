
# AWS CDK Pipeline Python project!

- The `cdk.json` file tells the CDK Toolkit how to execute your app.
- The initialization process also creates a virtualenv within this project, stored under the `.venv` directory. 
- To create the virtualenv it assumes that there is a `python3` executable in your path with access to the `venv`package.
- If for any reason the automatic creation of the virtualenv fails, you can create the virtualenv manually. To manually create a virtualenv on MacOS and Linux: `python3 -m venv .venv`
## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

## Preliminary preparations
* `brew upgrade awscli` for MacOS 
* `aws --version` 
* `brew upgrade aws-cdk` for MacOS
* `cdk --version`
* After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.<br>
`source .venv/bin/activate`
* `python3 -m pip install --upgrade pip` 
* Once the virtualenv is activated, you can install the required dependencies.<br>
`pip install -r requirements.txt`
* At this point you can now synthesize the CloudFormation template for this code.<br>
`cdk ls` 
`cdk synth`
* To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Create Pipeline with AWS CDK
### Create Pipeline Stack
- The first step is to create the stack that will contain our pipeline.
- Create a new file called **pipeline_stack.py**
- Add the following to that file:
```python
from constructs import Construct
from aws_cdk import (
    Stack
)

class WorkshopPipelineStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Pipeline code will go here
```

### Update CDK Deploy Entrypoint
- Next, since the purpose of our pipeline is to deploy our application stack, we no longer want the main CDK application to deploy our original app. Instead, we can change the entry point to deploy our pipeline, which will in turn deploy the application. 
- To do this, edit the code in **app.py**
```python
#!/usr/bin/env python3

import aws_cdk as cdk
from cdk_workshop.pipeline_stack import WorkshopPipelineStack

app = cdk.App()
WorkshopPipelineStack(app, "WorkshopPipelineStack")

app.synth()
```
### Define an Empty Pipeline
- Now we are ready to define the basics of the pipeline.
- Return to the file **pipeline_stack.py** and edit as follows:
```python
from constructs import Construct
from aws_cdk import (
    Stack,
    aws_codecommit as codecommit,
    pipelines as pipelines,
)

class WorkshopPipelineStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Creates a CodeCommit repository called 'WorkshopRepo'
        repo = codecommit.Repository(
            self, "WorkshopRepo", repository_name="WorkshopRepo"
        )

        pipeline = pipelines.CodePipeline(
            self,
            "Pipeline",
            synth=pipelines.ShellStep(
                "Synth",
                input=pipelines.CodePipelineSource.code_commit(repo, "main"),
                commands=[
                    "npm install -g aws-cdk",  # Installs the cdk cli on Codebuild
                    "pip install -r requirements.txt",  # Instructs Codebuild to install required packages
                    "cdk synth",
                ]
            ),
        )
```
- The above code does several things:
    - **pipelines.CodePipeline(...):** This initializes the pipeline with the required values. This will serve as the base component moving forward. Every pipeline requires at bare minimum:
        - **pipelines.ShellStep(...):** 
            - The **synth** of the pipeline describes the commands necessary to install dependencies, build, and synth the CDK application from source. This should always end in a synth command, for NPM-based projects this is always npx cdk synth.
            - The **input** of the synth step specifies the repository where the CDK source code is stored.




