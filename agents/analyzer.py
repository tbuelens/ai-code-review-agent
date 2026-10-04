import config

from openai import OpenAI
from models.analysis import CodeAnalysis

client = OpenAI()


def analyze_code(language: str, code: str) -> CodeAnalysis:

    
    instructions = """
        You are a software code analysis agent.

        Your responsibility is to analyze source code and identify potential problems.

        Focus on:
        - bugs
        - readability
        - maintainability
        - bad practices
        - security issues

        Do not refactor or rewrite the code.

        For every issue, provide:
        - a severity
        - a category
        - a clear description
        """

    
    user_input = f"""
        Language: {language}

        Code: {code}
        """

    response = client.responses.parse(
        model="gpt-5.4-mini",
        instructions= instructions,
        input= user_input,
        text_format= CodeAnalysis
    )

    return response.output_parsed