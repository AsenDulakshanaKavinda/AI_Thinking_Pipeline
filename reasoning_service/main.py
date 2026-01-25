from app.server import create_reasoning_server

from app.utils import log, ReasoningException


def main():
    create_reasoning_server()


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



