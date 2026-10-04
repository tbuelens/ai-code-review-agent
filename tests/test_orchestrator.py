from unittest.mock import patch

from models.analysis import CodeAnalysis
from models.refactoring import RefactoringResult
from models.review import ReviewResult

from orchestrator import run_workflow


def test_workflow_approved_first_attempt():

    analysis = CodeAnalysis(
        issues=[]
    )

    refactoring = RefactoringResult(
        refactored_code="print('hello')",
        changes=["No major changes"],
        explanation="Code is acceptable."
    )

    review = ReviewResult(
        approved=True,
        feedback="Refactoring approved.",
        remaining_issues=[]
    )

    with patch("orchestrator.analyze_code", return_value=analysis) as mock_analyze, \
         patch("orchestrator.refactor_code", return_value=refactoring) as mock_refactor, \
         patch("orchestrator.review_code", return_value=review) as mock_review:

        result = run_workflow(
            "python",
            "print('hello')"
        )

    assert result.analysis == analysis
    assert result.refactoring == refactoring
    assert result.review == review

    assert mock_analyze.call_count == 1
    assert mock_refactor.call_count == 1
    assert mock_review.call_count == 1
    
    
def test_workflow_retry_then_approved():

    analysis = CodeAnalysis(
        issues=[]
    )

    first_refactoring = RefactoringResult(
        refactored_code="print('first attempt')",
        changes=["First attempt"],
        explanation="First refactoring attempt."
    )

    second_refactoring = RefactoringResult(
        refactored_code="print('second attempt')",
        changes=["Applied reviewer feedback"],
        explanation="Second refactoring attempt."
    )

    rejected_review = ReviewResult(
        approved=False,
        feedback="The refactoring still has problems.",
        remaining_issues=["One issue remains."]
    )

    approved_review = ReviewResult(
        approved=True,
        feedback="The second refactoring is acceptable.",
        remaining_issues=[]
    )

    with patch(
        "orchestrator.analyze_code",
        return_value=analysis
    ) as mock_analyze, patch(
        "orchestrator.refactor_code",
        side_effect=[first_refactoring, second_refactoring]
    ) as mock_refactor, patch(
        "orchestrator.review_code",
        side_effect=[rejected_review, approved_review]
    ) as mock_review:

        result = run_workflow(
            "python",
            "print('hello')"
        )

    assert mock_analyze.call_count == 1
    assert mock_refactor.call_count == 2
    assert mock_review.call_count == 2
    
    mock_refactor.assert_any_call(
            "python",
            "print('hello')",
            analysis,
            "The refactoring still has problems."
        )

    assert result.analysis == analysis
    assert result.refactoring == second_refactoring
    assert result.review == approved_review
    assert result.review.approved is True
    
    
def test_workflow_stops_after_max_retries():

    analysis = CodeAnalysis(
        issues=[]
    )

    first_refactoring = RefactoringResult(
        refactored_code="print('first attempt')",
        changes=["First attempt"],
        explanation="First refactoring attempt."
    )

    second_refactoring = RefactoringResult(
        refactored_code="print('second attempt')",
        changes=["Second attempt"],
        explanation="Second refactoring attempt."
    )

    first_rejected_review = ReviewResult(
        approved=False,
        feedback="First attempt rejected.",
        remaining_issues=["Issue still present."]
    )

    second_rejected_review = ReviewResult(
        approved=False,
        feedback="Second attempt rejected.",
        remaining_issues=["Issue still present."]
    )

    with patch(
        "orchestrator.analyze_code",
        return_value=analysis
    ) as mock_analyze, patch(
        "orchestrator.refactor_code",
        side_effect=[first_refactoring, second_refactoring]
    ) as mock_refactor, patch(
        "orchestrator.review_code",
        side_effect=[first_rejected_review, second_rejected_review]
    ) as mock_review:

        result = run_workflow(
            "python",
            "print('hello')"
        )

    assert mock_analyze.call_count == 1
    assert mock_refactor.call_count == 2
    assert mock_review.call_count == 2

    assert result.refactoring == second_refactoring
    assert result.review == second_rejected_review
    assert result.review.approved is False