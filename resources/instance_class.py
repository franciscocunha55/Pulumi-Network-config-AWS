import pulumi
import pulumi_aws as aws
from typing import Mapping, Sequence

class InstanceArgs:
    def __init__(self,instance_type,ami,subnet,base_tags: Mapping[str, str],) -> None:
        
        self.instance_type=instance_type
        self.ami=ami
        self.subnet=subnet
        self.base_tags=base_tags
  

class Instance(pulumi.ComponentResource):

    def __init__(
        self, 
        name: str, 
        args: InstanceArgs, 
        opts: pulumi.ResourceOptions = None
    ):

        super().__init__("instance:index:Instance", name, {},opts)
        self.name = name
        
        

        self.instance=aws.ec2.Instance(f"{name}",
                            instance_type=args.instance_type,
                            ami=args.ami,
                            subnet_id=args.subnet,
                            tags={**args.base_tags},
                            opts=pulumi.ResourceOptions(
                                parent=self,
                           ))