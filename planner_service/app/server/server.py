
import grpc
from concurrent import futures
import generated.v3.python.planner_pb2 as pb2
import generated.v3.python.planner_pb2_grpc as pb2_grpc

from .handlers import (
    planner_response_to_gateway,
    
)

from app.utils import log, PlannerException

class PlannerService(pb2_grpc.PlannerServicer):

    def HandleGatewayRequestToPlanner(self, request, context):
        try:
            log.info("Handle planner response to gateway")
            response_from_planner = planner_response_to_gateway(request)
            return response_from_planner
        except Exception as e:
            PlannerException(
                e,
                context={
                    "operation": "HandleGatewayRequestToPlanner"
                }
            )


"""     def HandlePlannerRequestToReasoning(self, request, context):
        try:
            log.info("Handle planner request to reasoning")
            return handle_planner_request_to_reasoning(request)
        except Exception as e:
            PlannerException(
                e,
                context={
                    "operation": "HandlePlannerRequestToReasoning"
                }
            ) """
    
def create_planner_server():
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10)
    )

    pb2_grpc.add_PlannerServicer_to_server(
        servicer=PlannerService(), server=server
    )

    server.add_insecure_port("[::]:50051")
    server.start()
    log.info("Planner server running on [Port - 50051]")
    server.wait_for_termination()

if __name__ == "__main__":
    try:
        create_planner_server()
    except Exception as e:
        PlannerException(
            e, 
            context={
                "operation": "Planner server", "message": "Error"
            }
        )
    except KeyboardInterrupt:
        log.info("[Gateway Server] - Shutdown.")














