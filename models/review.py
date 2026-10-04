from pydantic import BaseModel


class ReviewResult(BaseModel):
    approved: bool
    feedback: str
    remaining_issues: list[str]