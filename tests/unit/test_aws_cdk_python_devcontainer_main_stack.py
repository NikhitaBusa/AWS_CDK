import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_cdk_python_devcontainer_main.aws_cdk_python_devcontainer_main_stack import AwsCdkPythonDevcontainerMainStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_cdk_python_devcontainer_main/aws_cdk_python_devcontainer_main_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsCdkPythonDevcontainerMainStack(app, "aws-cdk-python-devcontainer-main")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
