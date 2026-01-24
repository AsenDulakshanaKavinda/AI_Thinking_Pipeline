
import grpc
""" import proto.generated.v2.planner_pb2 as pb2
import proto.generated.v2.planner_pb2_grpc as pb2_grpc """

import generated.v3.python.planner_pb2 as pb2
import generated.v3.python.gateway_pb2_grpc as pb2_grpc

import generated.v4.python.reasoning_pb2 as reasoning_pb2
import generated.v4.python.reasoning_pb2_grpc as reasoning_pb2_grpc

from app.graph import build_graph

from app.utils import log, PlannerException

def planner_request_to_reasoning(incoming_request_gateway):
    channel = grpc.insecure_channel("localhost: 50052")
    stud = reasoning_pb2_grpc.ReasoningStub(channel=channel)



def planner_request_to_reasoning(incoming_request_gateway):
    channel = grpc.insecure_channel("localhost: 50052")
    stdu = pb2_grpc.PlannerStub(channel=channel)

    request_id, user_prompt = verify_incoming_request(incoming_request_gateway)

    payload = {
        "request_id": request_id,
        "user_prompt": user_prompt
    }

    try:
        app = build_graph()
        result = app.invoke(payload)
        output = {
            "request_id": result["request_id"],
            "user_prompt": result["user_prompt"],
            "intent": result["intent"],
            "confidence": result["confidence"],
            "plan": result["plan"].model_dump()  
        }
    except Exception as e:
        PlannerException(
            e,
            context={
                "operation": "planner_response_to_gateway",
                "message": "Error while generating plan."
            }
        )

    reasoning_request =  pb2.PlannerRequestToReasoning(
        request_id = output.get("request_id"),
        user_prompt = output.get("user_prompt"),
        intent = output.get("intent"),
        confidence = output("confidence"),
        plan = output("plan"),
    )

    return stdu.HandlePlannerRequestToReasoning(reasoning_request)

def verify_incoming_request(incoming_request):
    if not incoming_request:
        PlannerException(
            "incoming gateway request is empty of missing.",
            context={
                "operation": "planner_response_to_gateway"
            }
        )

    request_id = incoming_request.meta.request_id
    if not request_id:
        PlannerException(
            "request id is empty of missing.",
            context={
                "operation": "planner_response_to_gateway"
            }
        )

    user_prompt = incoming_request.user_prompt
    if not user_prompt:
        PlannerException(
            "user prompt is empty of missing.",
            context={
                "operation": "planner_response_to_gateway"
            }
        )
    
    return request_id, user_prompt

