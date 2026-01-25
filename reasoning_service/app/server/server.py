
import grpc

from concurrent import futures

import generated.v4.python.reasoning_pb2 as reasoning_pb2
import generated.v4.python.reasoning_pb2_grpc as reasoning_pb2_grpc

from app.handlers import reasoning_response_to_planner

from app.utils import log, ReasoningException


class ReasoningService(reasoning_pb2_grpc.ReasoningServicer):
    def HandlePlannerRequestToReasoning(self, request, context):
        try:
            log.info("Handle Planner Request To Reasoning")
            response = reasoning_response_to_planner(request)
            return response
        except Exception as e:
            raise ReasoningException(
                e,
                context={"operation": "HandlePlannerRequestToReasoning"},
            )              

    
def create_reasoning_server():
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10)
    )

    reasoning_pb2_grpc.add_ReasoningServicer_to_server(
        ReasoningService(), server
    )

    server.add_insecure_port("[::]:50052")
    server.start()
    log.info("Reasoning server running on [Port - 50052]")
    server.wait_for_termination()

if __name__ == "__main__":
    try:
        create_reasoning_server()
    except Exception as e:
        ReasoningException(
            e, 
            context={
                "operation": "Reasoning server", "message": "Error"
            }
        )
    except KeyboardInterrupt:
        log.info("[Reasoning Server] - Shutdown.")



