from typing import Mapping, Optional, Sequence

import pulumi
import pulumi_aws as aws
from pulumi import Input
from resources.vars import *

class VpcArgs:

    def __init__(self, cidr_block: str, enable_dns_hostnames: Optional[bool], enable_dns_support: Optional[bool],  base_tags: Mapping[str, str] )-> None:
        self.cidr_block= cidr_block
        self.enable_dns_hostnames=enable_dns_hostnames
        self.enable_dns_support=enable_dns_support
        self.availability_zone_names = availability_zone_names
        self.base_tags = base_tags
        


class Vpc(pulumi.ComponentResource):

    def __init__(self,
                 name: str,
                 args: VpcArgs,
                 opts: pulumi.ResourceOptions = None):
        
        super().__init__('Vpc', name, {}, opts)

        self.name=name
        #self.base_tags = args.base_tags

        self.vpc=aws.ec2.Vpc(f"{name}", 
                        cidr_block= args.cidr_block, 
                        enable_dns_hostnames=args.enable_dns_hostnames,
                        enable_dns_support=args.enable_dns_support,
                        tags= {**args.base_tags},
                        opts=pulumi.ResourceOptions(
                               parent=self,
                           ))
        
        self.private_subnets = [aws.ec2.Subnet(f"{name}-private-subnet-{i}",
                                           vpc_id=self.vpc.id,
                                           cidr_block=cidr,
                                           availability_zone=args.availability_zone_names[i],
                                           tags={**args.base_tags, "Name": f" pulumi-Private Subnet-{i}"},
                                           opts=pulumi.ResourceOptions(
                                               parent=self.vpc,
                                           ))
                                for i, cidr in enumerate(subnet_private_cidr_block) 
                                ]
        
        self.public_subnets=[aws.ec2.Subnet(f"{name}-public-subnet-{i}",
                                           vpc_id=self.vpc.id,
                                           cidr_block=cidr,
                                           availability_zone=args.availability_zone_names[i],
                                           tags={**args.base_tags, "Name": f" pulumi-Public Subnet-{i}"},
                                           opts=pulumi.ResourceOptions(
                                               parent=self.vpc,
                                           ))
                                for i, cidr in enumerate(subnet_public_cidr_block) 
                                ]
        