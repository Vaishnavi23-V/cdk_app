from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_iam as iam,
    aws_apigateway as apigateway,
)
from aws_cdk.aws_iam import PolicyStatement, Effect
from aws_cdk.aws_apigateway import LambdaRestApi, Cors
from aws_cdk.aws_lambda import Function, Runtime, Code
from constructs import Construct

class CdkAppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Lambda Function
        hello_function = Function(
            self, "HelloFunction",
            runtime=Runtime.PYTHON_3_9,
            handler="handler.hello",
            code=Code.from_asset("cdk_app/lambda"),
        )

         # API Gateway with CORS support
        api = LambdaRestApi(
            self, "NewApi",
            handler=hello_function,
            default_cors_preflight_options={
                "allow_origins": Cors.ALL_ORIGINS,
                "allow_methods": Cors.ALL_METHODS,
                "allow_headers": ["*"]
            }
        )


       
      