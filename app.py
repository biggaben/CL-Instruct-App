from typing import Dict
from flask import Flask, request, jsonify
from transformers import pipeline
app = Flask(__name__)

# Initialize the model and tokenizer
MODEL_NAME = "codellama/CodeLlama-13b-Instruct-hf"
llm_pipeline = pipeline("text-generation", model=MODEL_NAME)

@app.route('/generate-code', methods=['POST'])
def generate_code():
    """
    Generate code based on the provided prompt using the LLM model.

    This function accepts JSON input containing a 'prompt' field,
    generates a response using the specified LLM model, and returns
    the generated code as JSON.

    Returns:
        A JSON response containing the generated code.
    """
    data = request.json
    if not isinstance(data, Dict):
        return jsonify({"error": "Invalid JSON format"}), 400
    prompt = data.get('prompt', '')
    response = llm_pipeline(prompt, max_length=100)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
