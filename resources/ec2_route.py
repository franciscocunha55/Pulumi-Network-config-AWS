from typing import Mapping, Optional, Sequence
import pulumi
import pulumi_aws as aws

class RouteArgs:
    def __init__(self, route_table_id ,transit_gateway_id, destination_cidr_block, base_tags: Mapping[str, str] ) -> None:
        self.route_table_id=route_table_id
        self.transit_gateway_id=transit_gateway_id
        self.destination_cidr_block=destination_cidr_block
        self.base_tags=base_tags



class Route(pulumi.ComponentResource):

    def __init__(self,
                 name: str,
                 args: RouteArgs,
                 opts: pulumi.ResourceOptions = None):

        super().__init__('Route', name, {}, opts)

        self.name=name

        self.tgw_attachment=aws.ec2transitgateway.Route(f"{name}",
                                route_table_id=args.route_table_id,
                                transit_gateway_id=args.transit_gateway_id,
                                destination_cidr_block=args.destination_cidr_block,
                                tags= {**args.base_tags},
                                opts=pulumi.ResourceOptions(
                               parent=self,
                            ))