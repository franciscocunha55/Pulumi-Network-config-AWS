from ensurepip import version
import pulumi
import pulumi_aws as aws
from typing import Mapping, Optional, Sequence

class LaunchTemplateArgs:
    def __init__(self,name_prefix,image_id,instance_type, user_data, base_tags: Mapping[str, str]) -> None:
        self.name_prefix=name_prefix
        self.image_id=image_id
        self.instance_type=instance_type
        self.user_data=user_data
        self.base_tags=base_tags


class LaunchTemplate(pulumi.ComponentResource):

    def __init__(
        self,  
        resource_name:str,
        args: LaunchTemplateArgs,
        opts: pulumi.ResourceOptions = None
    ):

        super().__init__("autoScaling:index:autoScaling",resource_name, {},opts)

        self.resource_name = resource_name
        self.launchTemplate=aws.ec2.LaunchTemplate(
                            resource_name,
                            name_prefix=args.name_prefix,
                            image_id=args.image_id,
                            instance_type=args.instance_type,
                            user_data=args.user_data,
                            tags={**args.base_tags},
                            opts=pulumi.ResourceOptions(
                                parent=self,
                           ))


class AutosScalingArgs:
    def __init__(self, name ,desired_capacity,min_size,max_size,vpc_zone_identifiers,launch_template: Optional[pulumi.Input['LaunchTemplateArgs']] ,tags) -> None:
        
        self.name=name
        self.desired_capacity=desired_capacity
        self.min_size=min_size
        self.max_size=max_size
        self.vpc_zone_identifiers=vpc_zone_identifiers
        self.launch_template=launch_template
        self.tags=tags
        
  

class AutoScaling(pulumi.ComponentResource):

    def __init__(
        self, 
        resource_name: str, 
        args: AutosScalingArgs,
        opts: pulumi.ResourceOptions = None
    ):

        super().__init__("autoScaling:index:AutoScaling", resource_name, {},opts)
        self.resource_name = resource_name
    

        self.autoScaling= aws.autoscaling.Group(resource_name,
                            name = args.name,
                            desired_capacity=args.desired_capacity,
                            min_size=args.min_size,
                            max_size=args.max_size,
                            vpc_zone_identifiers=args.vpc_zone_identifiers,
                            launch_template=args.launch_template,
                            tags=args.tags,
                            opts=pulumi.ResourceOptions(
                                parent=self,
                           ))
    

class AutosScalingScheduleArgs:
    def __init__(self, scheduled_action_name ,desired_capacity,min_size,max_size,recurrence,autoscaling_group_name) -> None:
        
        self.scheduled_action_name=scheduled_action_name
        self.desired_capacity=desired_capacity
        self.min_size=min_size
        self.max_size=max_size
        self.recurrence=recurrence
        self.autoscaling_group_name=autoscaling_group_name
        
  

class AutoScalingSchedule(pulumi.ComponentResource):

    def __init__(
        self, 
        resource_name: str, 
        args: AutosScalingScheduleArgs,
        opts: pulumi.ResourceOptions = None
    ):

        super().__init__("AutoScalingSchedule:index:AutoScalingSchedule", resource_name, {},opts)

        self.resource_name = resource_name
    

        self.autoScalingSchedule= aws.autoscaling.Schedule(resource_name,
                            scheduled_action_name = args.scheduled_action_name,
                            desired_capacity=args.desired_capacity,
                            min_size=args.min_size,
                            max_size=args.max_size,
                            recurrence=args.recurrence,
                            autoscaling_group_name=args.autoscaling_group_name,
                            opts=pulumi.ResourceOptions(
                                parent=self,
                           ))
    

