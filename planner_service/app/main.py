from app.utils import log, PlannerException


def main():
    log.info("Test log")
    try:
        result = 10 / 0
    except Exception as e:
        PlannerException(
            e,
            context={"operation": "division_test", "value": 10}
        )


if __name__ == "__main__":
    main()
