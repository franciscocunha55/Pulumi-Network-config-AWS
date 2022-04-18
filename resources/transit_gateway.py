from typing import Mapping, Optional, Sequence
import pulumi
import pulumi_aws as aws

class Tgw_attachmentArgs:
    def __init__(self, transit_gateway_id,vpc_id, subnet_ids:Optional[Sequence[str]], base_tags: Mapping[str, str] ) -> None:
        self.transit_gateway_id=transit_gateway_id
        self.vpc_id=vpc_id
        self.subnet_ids=subnet_ids
        self.base_tags=base_tags



class Tgw_attachment(pulumi.ComponentResource):

    def __init__(self,
                 name: str,
                 args: Tgw_attachmentArgs,
                 opts: pulumi.ResourceOptions = None):

        super().__init__('Tgw_attachment', name, {}, opts)

        self.name=name

        self.tgw_attachment=aws.ec2transitgateway.VpcAttachment(f"{name}",
                                transit_gateway_id=args.transit_gateway_id,
                                vpc_id=args.vpc_id,
                                subnet_ids=args.subnet_ids,
                                tags= {**args.base_tags},
                                opts=pulumi.ResourceOptions(
                               parent=self,
                            ))