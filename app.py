#!/usr/bin/env python3
import os

import aws_cdk as cdk

# from aws_cdk_python_devcontainer_main.aws_cdk_python_devcontainer_main_stack import AwsCdkPythonDevcontainerMainStack


# app = cdk.App()
# AwsCdkPythonDevcontainerMainStack(app, "AwsCdkPythonDevcontainerMainStack",
#     # If you don't specify 'env', this stack will be environment-agnostic.
#     # Account/Region-dependent features and context lookups will not work,
#     # but a single synthesized template can be deployed anywher
#     # Uncomment the next line to specialize this stack for the AWS Account
#     # and Region that are implied by the current CLI configuration.

#     #env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

#     # Uncomment the next line if you know exactly what Account and Region you
#     # want to deploy the stack to. */

#     #env=cdk.Environment(account='123456789012', region='us-east-1'),

#     # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
#     )

# app.synth()

from aws_cdk_python_devcontainer_main.pipeline_stack import MyPipelineStack

app = cdk.App()
MyPipelineStack(app, "MyPipelineStack")

app.synth()

