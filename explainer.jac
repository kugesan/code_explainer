import from mtllm.llm { Model}

# Initialize the LLM you want to use.
# Make sure you have the correct API key set up in your environment.
glob llm = Model(model_name="gemini/gemini-2.0-flash");

# Define the function that will explain the code.
# The "by llm" part tells Jac to use the LLM to generate the output.
def explain_code(code_snippet: str) -> str by llm();

# This is a semantic string, which acts as a prompt for the LLM.
sem explain_code = """
Explain the following Jac code snippet to a beginner.
Break down the code into its main parts and explain what each part does.
The user has provided the following code:
{code_snippet}
""";
