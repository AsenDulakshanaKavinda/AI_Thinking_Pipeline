
from datetime import datetime

import proto.generated.v2.planner_pb2 as pb2
import proto.generated.v2.planner_pb2_grpc as pb2_grpc

from app.utils import log, PlannerException


def planner_response_to_gateway(incoming_request_gateway):

    if not incoming_request_gateway:
        PlannerException(
            "incoming gateway request is empty of missing.",
            context={
                "operation": "planner_response_to_gateway"
            }
        )

    request_id = incoming_request_gateway.meta.request_id
    if not request_id:
        PlannerException(
            "request id is empty of missing.",
            context={
                "operation": "planner_response_to_gateway"
            }
        )

    try:
        log.info("Handling Planner request from the Gateway")
        return pb2.PlannerResponseToGateway(
            meta = pb2.RequestMeta(
                request_id = request_id,
                time = pb2.Timestamp(
                    unix_ms = int(datetime.now().timestamp() * 1000)
                )
            ),
            message = "Received a request from the Gateway."
        )


    except Exception as e:
        PlannerException(
            e,
            context={
                "operation": "planner_response_to_gateway"
            }
        )      





