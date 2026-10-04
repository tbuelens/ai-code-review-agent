import config

from openai import OpenAI
from models.review import ReviewResult
from models.analysis import CodeAnalysis
from models.refactoring import RefactoringResult

client = OpenAI()

def review_code(language: str, code: str, code_analysis: CodeAnalysis, refactoring: RefactoringResult) -> ReviewResult:
    
    instructions = """
        You are a senior software code review agent.

        Your responsibility is to evaluate a proposed code refactoring produced by another agent.

        Review the proposed refactoring against:
        - the original source code,
        - the issues identified during the initial code analysis,
        - and the intended behavior of the original code.

        Verify that:
        - the identified issues have been correctly addressed;
        - the refactored code preserves the original intent and behavior whenever possible;
        - the refactoring does not introduce obvious bugs or regressions;
        - the refactoring does not introduce unnecessary complexity;
        - the resulting code remains readable and maintainable.

        Do not rewrite or refactor the code yourself.

        Set approved to true only if the proposed refactoring is acceptable.

        If the refactoring is not acceptable:
        - set approved to false;
        - explain clearly why in feedback;
        - list the unresolved or newly introduced problems in remaining_issues.

        If the refactoring is acceptable:
        - set approved to true;
        - provide a short explanation in feedback;
        - return an empty remaining_issues list.
    """
    
    analysis_json = code_analysis.model_dump_json()
    refactoring_json = refactoring.model_dump_json()
    
    user_input = f"""
            Language: {language}
            Original Code: {code}
            Code Analysis: {analysis_json}
            Refactoring: {refactoring_json}
    """
    
    response = client.responses.parse(
                model="gpt-5.4-mini",
                instructions=instructions,
                input=user_input,
                text_format=ReviewResult
            )
        
    return response.output_parsed
    
    
    