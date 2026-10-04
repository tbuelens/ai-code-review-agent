from pydantic import BaseModel
from models.analysis import CodeAnalysis
from models.refactoring import RefactoringResult
from models.review import ReviewResult

class WorkflowResult(BaseModel):
    analysis: CodeAnalysis
    refactoring: RefactoringResult
    review: ReviewResult