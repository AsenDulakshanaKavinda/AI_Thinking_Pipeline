from app.utils import log, PlannerException
from app.graph import build_graph
import uuid
from app.server import create_planner_server


""" def main():
    try:
        log.info("Graph test starting...")
        app = build_graph()
        initial_state = {
            "request_id": str(uuid.uuid4()),
            "user_prompt": "Design a scalable AI thinking pipeline"
        }
        result = app.invoke(initial_state)

        output = {
            "request_id": result["request_id"],
            "user_prompt": result["user_prompt"],
            "intent": result["intent"],
            "confidence": result["confidence"],
            "plan": result["plan"].model_dump()  
        }

        print(output)

        return output

    except Exception as e:
        PlannerException(
            e,
            context={"operation": "testing graph", "status": "failed"}
        ) """

def main():
    create_planner_server()


if __name__ == "__main__":

    try:
        main()
    except Exception as e:
        PlannerException(
            e, 
            context={
                "operation": "Planner server", "message": "Error"
            }
        )
    except KeyboardInterrupt:
        log.info("[Planner Server] - Shutdown.")

