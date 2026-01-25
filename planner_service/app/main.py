from app.utils import log, PlannerException
from app.server import create_planner_server

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

