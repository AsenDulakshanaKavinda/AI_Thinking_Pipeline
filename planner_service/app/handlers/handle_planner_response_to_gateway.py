
from datetime import datetime


import generated.v4.python.common_pb2 as common_pb2
import generated.v4.python.common_pb2_grpc as common_pb2_grpc

import generated.v4.python.planner_pb2 as planner_pb2
import generated.v4.python.planner_pb2_grpc as planner_pb2_grpc

from app.utils import log, PlannerException


def planner_response_to_gateway(incoming_request_gateway):
    """
    Handles a GatewayRequestToPlanner and returns a PlannerResponseToGateway.
    """

    if incoming_request_gateway is None:
        raise PlannerException(
            "Incoming gateway request is empty or missing.",
            context={"operation": "planner_response_to_gateway"},
        )
    log.info("Received request from the gateway. ")

    request_id = incoming_request_gateway.meta.request_id

    if not request_id:
        raise PlannerException(
            "Request ID is empty or missing.",
            context={"operation": "planner_response_to_gateway"},
        )
    
    log.info(f"Handling request {request_id}")

    try:
        response = planner_pb2.PlannerResponseToGateway(
            response=common_pb2.Response(
                meta=common_pb2.RequestMeta(
                    request_id=request_id,
                    time=common_pb2.Timestamp(
                        unix_ms=int(datetime.now().timestamp() * 1000)
                    ),
                ),
                message="Received a request from the Gateway.",
            )
        )

        return response

    except Exception as e:
        raise PlannerException(
            str(e),
            context={"operation": "planner_response_to_gateway"},
        )

