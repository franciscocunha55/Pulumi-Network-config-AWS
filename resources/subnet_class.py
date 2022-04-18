from typing import Mapping, Optional, Sequence

import pulumi
import pulumi_aws as aws
from pulumi import Input
from resources.vars import *

class SubnetArgs:

    def __init__(self, availability_zone,vpc_id, cidr_block: str, base_tags: Mapping[str, str] )-> None:
        self.availability_zone=availability_zone
        self.vpc_id=vpc_id
        self.cidr_block= cidr_block
        self.availability_zone_names = availability_zone_names
        self.base_tags = base_tags
        



class Subnet(pulumi.ComponentResource):

    def __init__(self,
                 name: str,
                 args: SubnetArgs,
                 opts: pulumi.ResourceOptions = None):
        
        super().__init__('Subnet', name, {}, opts)

        self.name=name
        #self.base_tags = args.base_tags

        self.subnet=aws.ec2.Subnet(f"{name}", 
                        cidr_block= args.cidr_block, 
                        availability_zone=args.availability_zone,
                        vpc_id=args.vpc_id,
                        tags= {**args.base_tags},
                        opts=pulumi.ResourceOptions(
                               parent=self,
                           ))