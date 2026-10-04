import logging

from agents.analyzer import analyze_code
from agents.refactor import refactor_code
from models.workflow import WorkflowResult
from agents.reviewer import review_code

logger = logging.getLogger(__name__)

MAX_RETRIES = 1


def run_workflow(language: str, code: str) -> WorkflowResult:

    logger.info("Starting workflow")

    # ---------- ANALYSIS ----------

    logger.info("Starting code analysis")

    code_analysis = analyze_code(language, code)

    logger.info("Code analysis completed")

    # ---------- FIRST REFACTORING ----------

    logger.info("Starting refactoring attempt 1")

    code_refactoring = refactor_code(language, code, code_analysis)

    logger.info("Refactoring attempt 1 completed")

    # ---------- FIRST REVIEW ----------

    logger.info("Starting review attempt 1")

    code_review = review_code(language, code, code_analysis, code_refactoring)

    logger.info("Review attempt 1 completed - approved=%s", code_review.approved)

    # ---------- RETRY LOOP ----------

    retries = 0

    while not code_review.approved and retries < MAX_RETRIES:

        retries += 1
        attempt = retries + 1

        logger.warning("Refactoring rejected - starting retry attempt %s", attempt)

        logger.info("Starting refactoring attempt %s", attempt)

        code_refactoring = refactor_code(language, code, code_analysis, code_review.feedback)

        logger.info("Refactoring attempt %s completed", attempt)

        logger.info("Starting review attempt %s", attempt)

        code_review = review_code(language, code, code_analysis, code_refactoring)

        logger.info("Review attempt %s completed - approved=%s", attempt, code_review.approved)

    # ---------- END ----------

    logger.info("Workflow completed - approved=%s", code_review.approved)

    return WorkflowResult(analysis=code_analysis, refactoring=code_refactoring, review=code_review)