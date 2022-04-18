from typing import Mapping, Optional, Sequence

import pulumi
import pulumi_aws as aws




class IAM_Role_Args:
    def __init__(self, assume_role_policy, base_tags: Mapping[str, str] ) -> None:
        #self.name
        self.assume_role_policy=assume_role_policy
        self.base_tags=base_tags

class IAM_Role(pulumi.ComponentResource):
    def __init__(
        self,  
        name:str,
        args: IAM_Role_Args,
        opts: pulumi.ResourceOptions = None
    ):

        super().__init__("IAM_Role",name, {},opts)

        self.IAM_role = aws.iam.Role(f"{name}", 
                        assume_role_policy= args.assume_role_policy, 
                        tags= {**args.base_tags},
                        opts=pulumi.ResourceOptions(
                               parent=self,
                           ))