import aws_cdk as cdk
from constructs import Construct
from aws_cdk_python_devcontainer_main.aws_cdk_python_devcontainer_main_stack import AwsCdkPythonDevcontainerMainStack

class MyPipelineAppStage(cdk.Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambdaStack = AwsCdkPythonDevcontainerMainStack(self, "LambdaStack")
