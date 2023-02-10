import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_codepipeline_project_py.aws_codepipeline_project_py_stack import AwsCodepipelineProjectPyStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_codepipeline_project_py/aws_codepipeline_project_py_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsCodepipelineProjectPyStack(app, "aws-codepipeline-project-py")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
