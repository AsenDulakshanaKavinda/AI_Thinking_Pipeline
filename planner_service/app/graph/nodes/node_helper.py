from pathlib import Path
from app.utils import log, PlannerException


def load_prompt(filepath: Path) -> str:
    """ Helper function that read and return the prompt from given filepath. """
    try:
        with open(filepath, "r", encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        PlannerException(
            e,
            context={"operation": "load prompt helper"}
        )
