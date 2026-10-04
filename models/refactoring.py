from pydantic import BaseModel

class RefactoringResult(BaseModel):
    refactored_code: str
    changes: list[str]
    explanation: str