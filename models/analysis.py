from pydantic import BaseModel
from typing import Literal


class Issue(BaseModel):
    severity: Literal["low", "medium", "high"]
    category: Literal["bug", "security", "readability", "maintainability", "performance", "bad_practice", "robustness"]
    description: str


class CodeAnalysis(BaseModel):
    issues: list[Issue]