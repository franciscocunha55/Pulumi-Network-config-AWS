


import base64
from os import path
import pulumi
from pulumi import export
from resources.ec2_route import Route, RouteArgs
from resources.iam_role_class import IAM_Role, IAM_Role_Args
from resources.securityGroup_class import Ingress, IngressArgs, SecurityGroup, SecurityGroupArgs
from resources.transit_gateway import Tgw_attachment, Tgw_attachmentArgs
from resources.subnet_class import Subnet, SubnetArgs
from resources.autoScalingGroup_class import AutoScaling, AutoScalingSchedule, AutosScalingArgs, AutosScalingScheduleArgs, LaunchTemplate, LaunchTemplateArgs
from resources.vpc_class import Vpc, VpcArgs
from resources.instance_class import Instance, InstanceArgs

import pulumi_aws as aws

from resources.vars import *


if __name__ == "__main__":
        
    ### VPC ### 
    vpc1 = Vpc("pulumi-vpc", VpcArgs(
                cidr_block="10.235.22.0/23",
                enable_dns_hostnames= True,
                enable_dns_support= True,
                base_tags={
                    "Name": "pulumi-vpc",
                }
            ))
    

    #### Subnets EKS #######

    subnets_private_EKS1=[Subnet(f"subnet-eks-{i}",SubnetArgs(availability_zone=name, vpc_id=vpc1.vpc.id, cidr_block= "10.235.23." + str(i*64)+"/26", 
                        base_tags={
                                    "Name": f"subnet-eks-private-{i}",
                                }))
                          for i, name in enumerate(availability_zone_names) ]

    ### Transit Gateway Attachment
    if transit_gateway_id != "":
        transit_gateway_attachment1=Tgw_attachment("transit_gateway_attachment1", Tgw_attachmentArgs(transit_gateway_id,vpc_id=vpc1.vpc.id,
        subnet_ids=[sub.subnet.id  for i , sub in enumerate (subnets_private_EKS1)],
        base_tags={
                                    "Name": "tgw-vpc-attach-" + pulumi.get_stack(),
        }))

    
    ## AutoScalingGroup ### 

    launchTemplate1=LaunchTemplate("launchTemplate1", LaunchTemplateArgs("pulumi-template-", "ami-0dcc0ebde7b2e00db", "t2.micro", 
    user_data=((lambda path: base64.b64encode(open(path).read().encode()).decode())("resources/user_data.sh")), base_tags={"Name": "pulumi-tutorial-host"}))

   
    autoScalingGroup1=AutoScaling("autoScalingGroup1", AutosScalingArgs(name="pulumi-autoScaling-" + pulumi.get_stack() ,
                                desired_capacity=1,min_size=1,max_size=1, 
                                vpc_zone_identifiers= [ sub for i, sub in enumerate(vpc1.private_subnets)] if pulumi.get_stack() == "dev" else [ sub for i, sub in enumerate(vpc1.public_subnets)] ,
                                 
                        
                        launch_template=aws.autoscaling.GroupLaunchTemplateArgs(
                                            id=launchTemplate1.launchTemplate.id,
                                                version="$Latest" ), 
                        
                        tags=[aws.autoscaling.GroupTagArgs(
                                                        key="Name",
                                                        value="pulumi-host-" + pulumi.get_stack(),
                                                        propagate_at_launch=True,
                                                    )]
                        ))

    ### Autoscaling Schedule #### 

    autoScalingSchedule1=AutoScalingSchedule("autoScalingSchedule_offline", 
    AutosScalingScheduleArgs("autoScalingSchedule_offline", 0,0,0,recurrence="0 21 * * 1-5", autoscaling_group_name=autoScalingGroup1.autoScaling.id))

    autoScalingSchedule1=AutoScalingSchedule("autoScalingSchedule_online", 
    AutosScalingScheduleArgs("autoScalingSchedule_online", 1,1,1,recurrence="0 9 * * 1-5", autoscaling_group_name=autoScalingGroup1.autoScaling.id))

    ### EC2 IAM Role ###
    iamRole1 = IAM_Role("iamRole1", IAM_Role_Args(assume_role_policy=assume_role_policy_ec2, base_tags={"Name": "EC2 IAM Role"}  ))

    ### Security Group ###
 
    securityGroup1= SecurityGroup("securityGroup1", SecurityGroupArgs("ssh access", 
            vpc_id=vpc1.vpc.id,
             ingress=[
        { 'protocol': 'tcp', 'from_port': 22, 'to_port': 22, 'cidr_blocks': [vpc1.vpc.cidr_block] }
    ], base_tags={"Name": "pulumi-sg"} ))

    export("vpc", vpc1.vpc.id)
