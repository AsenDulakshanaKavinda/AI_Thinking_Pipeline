from datetime import datetime
import generated.v4.python.common_pb2 as common_pb2
import generated.v4.python.common_pb2_grpc as common_pb2_grpc

import generated.v4.python.reasoning_pb2 as reasoning_pb2
import generated.v4.python.reasoning_pb2_grpc as reasoning_pb2_grpc

from app.utils import log, ReasoningException

def reasoning_response_to_planner(incoming_request):

    request_id, _ = verify_incoming_request(incoming_request=incoming_request)

    try:
        response = reasoning_pb2.ReasoningResponseToPlanner(
            response=common_pb2.Response(
                meta=common_pb2.RequestMeta(
                    request_id=request_id,
                    time=common_pb2.Timestamp(
                        unix_ms=int(datetime.now().timestamp() * 1000)
                    ),
                ),
                message="Received a request from the planner."
            )
        )
        
        return response
    except Exception as e:
        raise ReasoningException(
            str(e),
            context={"operation": "reasoning_response_to_planner"},
        )
    

def verify_incoming_request(incoming_request):
    if not incoming_request:
        ReasoningException(
            "incoming gateway request is empty of missing.",
            context={
                "operation": "reasoning_response_to_planner"
            }
        )

    request_id = incoming_request.request_id
    if not request_id:
        ReasoningException(
            "request id is empty of missing.",
            context={
                "operation": "reasoning_response_to_planner"
            }
        )

    user_prompt = incoming_request.user_prompt
    if not user_prompt:
        ReasoningException(
            "user prompt is empty of missing.",
            context={
                "operation": "reasoning_response_to_planner"
            }
        )
    
    return request_id, user_prompt

