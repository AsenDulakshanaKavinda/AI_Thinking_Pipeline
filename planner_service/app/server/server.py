"""
Planner Service (gRPC)

This module implements the Planner gRPC service, which acts as the
central orchestration layer between the Gateway and Reasoning services
in the AI Thinking Pipeline.

Responsibilities:
- Receive structured requests from the Gateway service via gRPC
- Perform planning logic and construct a response for the Gateway
- Forward the original request to the Reasoning service asynchronously
  for deeper cognitive or analytical processing
- Handle errors gracefully and propagate gRPC-safe exceptions

Request Flow:
Client
  -> Gateway Service
      -> Planner Service (HandleGatewayRequestToPlanner)
          1. Build and return a Planner response to the Gateway
          2. Dispatch the request to the Reasoning service (non-blocking)
      <- Gateway Service
  <- Client

Design Notes:
- The Planner service is intentionally lightweight and orchestration-focused
- Heavy reasoning or long-running logic must NOT block the Gateway response
- ThreadPoolExecutor enables concurrent request handling
- Business logic is delegated to handler functions to keep gRPC layer thin
- Centralized logging and exception handling are enforced for observability

Port:
- Listens on TCP port 50051 (insecure channel for internal communication)

This service is a core component in a microservice-based AI reasoning pipeline.
"""

import grpc
from concurrent import futures

import generated.v4.python.planner_pb2 as planner_pb2
import generated.v4.python.planner_pb2_grpc as planner_pb2_grpc

from app.handlers import (
    planner_response_to_gateway,
    planner_request_to_reasoning
    
)

from app.utils import log, PlannerException

class PlannerService(planner_pb2_grpc.PlannerServicer):

    # send response to the gateway
    # send request to the reasoning

    def HandleGatewayRequestToPlanner(self, request, context):
        try:
            log.info("Handle planner response to gateway")
            response_from_planner = planner_response_to_gateway(request)
            planner_request_to_reasoning(request)
            return response_from_planner
        except Exception as e:
            PlannerException(
                e,
                context={
                    "operation": "HandleGatewayRequestToPlanner"
                }
            )

def create_planner_server():
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10)
    )

    planner_pb2_grpc.add_PlannerServicer_to_server(
        servicer=PlannerService(), server=server
    )

    server.add_insecure_port("[::]:50051")
    server.start()
    log.info("Planner server running on [Port - 50051]")
    server.wait_for_termination()




