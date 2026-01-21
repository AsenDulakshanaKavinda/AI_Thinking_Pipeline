from app.utils import log, PlannerException
from app.graph import build_graph
import uuid


def main():
    try:
        log.info("Graph test starting...")
        app = build_graph()
        initial_state = {
            "request_id": str(uuid.uuid4()),
            "user_prompt": "Design a scalable AI thinking pipeline"
        }
        print(initial_state)
        result = app.invoke(initial_state)
        print(result)
    except Exception as e:
        PlannerException(
            e,
            context={"operation": "testing graph", "status": "failed"}
        )


if __name__ == "__main__":
    main()
