from typing import Mapping, Optional, Sequence

import pulumi
import pulumi_aws as aws
from pulumi import Input
from resources.vars import *


### Ingress ###

class IngressArgs:

    def __init__(self, description, from_port,to_port, protocol,cidr_blocks) -> None:
        self.description=description
        self.from_port=from_port
        self.to_port=to_port
        self.protocol=protocol
        self.cidr_blocks=cidr_blocks

class Ingress(pulumi.ComponentResource):

    def __init__(
        self,  
        resource_name:str,
        args: IngressArgs,
        opts: pulumi.ResourceOptions = None
    ):

        super().__init__("Ingress:index:Ingress",resource_name, {},opts)

        self.resource_name = resource_name
        self.ingress= [aws.ec2.SecurityGroupIngressArgs(
            resource_name,
            description=args.description,
            from_port=args.from_port,
            to_port=args.to_port,
            protocol=args.protocol,
            cidr_blocks=args.cidr_blocks,
            opts=pulumi.ResourceOptions(
                                parent=self,
                           )
        )]
        

### Security Group Definition ###

class SecurityGroupArgs:

    def __init__(self, description,vpc_id, ingress, base_tags: Mapping[str, str] )-> None:
        self.description= description
        self.vpc_id=vpc_id
        self.ingress=ingress
        #self.egress = egress
        self.base_tags = base_tags
        



class SecurityGroup(pulumi.ComponentResource):

    def __init__(self,
                 name: str,
                 args: SecurityGroupArgs,
                 opts: pulumi.ResourceOptions = None):
        
        super().__init__('SecurityGroup', name, {}, opts)

        self.name=name
        #self.base_tags = args.base_tags

        self.vpc=aws.ec2.SecurityGroup(f"{name}", 
                        description= args.description, 
                        vpc_id=args.vpc_id,
                        ingress=args.ingress,
                        #egress=args.egress,
                        tags= {**args.base_tags},
                        opts=pulumi.ResourceOptions(
                               parent=self,
                           ))
        

