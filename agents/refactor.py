import config

from openai import OpenAI
from models.analysis import CodeAnalysis
from models.refactoring import RefactoringResult

client = OpenAI()

def refactor_code(language: str, code: str, code_analysis: CodeAnalysis, review_feedback: str | None = None) -> RefactoringResult:
    
    instructions = """
            You are a software refactoring agent.

            Your responsibility is to improve source code based on issues
            identified by a code analysis agent.

            Correct the identified issues while preserving the original
            behavior and intent of the program whenever possible.

            Do not introduce unnecessary complexity.

            Return the complete refactored code and clearly describe the
            changes you made.
            """
            
    analysis_json = code_analysis.model_dump_json()
    
    if review_feedback is not None:
        user_input = f"""
                    Language: {language}
        
                    Original code: {code}
        
                    Code analysis: {analysis_json}
                    
                    Reviewer Feedback from a previous Refactoring Attempt: {review_feedback}
                    
                """
    else:
        user_input = f"""
            Language: {language}

            Original code: {code}

            Code analysis: {analysis_json}
        """
    
        
    response = client.responses.parse(
            model="gpt-5.4-mini",
            instructions=instructions,
            input=user_input,
            text_format=RefactoringResult
        )
    
    return response.output_parsed
    