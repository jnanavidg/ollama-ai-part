from flask import Flask, render_template, request, jsonify
from backend.llm import generate

app = Flask(__name__)

# /-----------------API ROUTES-----------------/

@app.route('/health', methods=['GET'])
def check_health():
    return {"output": "healthy"}, 200

@app.route('/echo', methods=['POST'])
def echo_post():
    data = request.get_json(silent=True) or {}

    user_input = data.get('user')
    some_value = data.get('some_value')

    # processing it using some functions.
    output = generate(user_input)
    #  ... 
    return jsonify({
        "input": user_input,
        "output": output
    }), 200

@app.route('/summary', methods=['POST'])
def summary_post():
    data = request.get_json(silent=True) or {}
    # input 
    user_input = data.get('user')
    # processing it using some functions.
    prompt = "Summerize this entire text: " + user_input
    output = generate(prompt)
    # ouput
    return jsonify({
        "output": output
    }), 200

@app.route('/rewrite-tone', methods=['POST'])
def rewrite_tone():

    data = request.get_json(silent=True) or {}

    user_text = data.get("user")
    tone = data.get("tone")

    prompt = f"""
Rewrite the following text in a {tone} tone.

Rules:
- Keep the meaning exactly same
- Do not summarize
- Do not add new information
- Only change tone/style

Text:
{user_text}
"""

    output = generate(prompt)

    return jsonify({
        "original_text": user_text,
        "tone": tone,
        "rewritten_text": output
    }), 200


# /-----------------PAGES-----------------/

@app.route('/key-points', methods=['POST'])
def key_points():

    data = request.get_json(silent=True) or {}

    user_text = data.get("user")
    count = data.get("count", 5)

    prompt = f"""
Extract exactly {count} important key points from the text.

Rules:
- Return only key points
- Avoid repetition
- Keep each point short and independent
- Focus on extraction, not summarization

Text:
{user_text}
"""

    output = generate(prompt)

    points = [p.strip() for p in output.split("\n") if p.strip()]

    return jsonify({
        "total_points_requested": count,
        "key_points": points
    }), 200

@app.route('/learning-check', methods=['POST'])
def learning_check():

    content = request.form.get("content")
    level = request.form.get("level")

    prompt = f"""
You are a teacher.

Based on the learning material below, generate 5 {level} difficulty questions.

Rules:
- Questions only
- No answers
- Test understanding and reasoning

Material:
{content}
"""

    output = generate(prompt)

    questions = [q.strip() for q in output.split("\n") if q.strip()]

    return jsonify({
        "difficulty_level": level,
        "questions": questions
    }), 200

@app.route('/analyze-user-activity', methods=['POST'])
def analyze_user_activity():

    data = request.get_json(silent=True) or {}

    users_data = data.get("users_data", [])
    query = data.get("query", "")

    prompt = f"""
You are a data extraction assistant.

User Query:
{query}

User Records:
{users_data}

Instructions:
1. Understand the user's intent.
2. Find matching user records.
3. Extract only relevant information.
4. Return valid JSON only in this format:

{{
  "matched_role": "...",
  "total_matches": number,
  "results": [...]
}}
"""

    output = generate(prompt)

    try:
        import json
        return jsonify(json.loads(output)), 200
    except:
        return jsonify({
            "raw_output": output
        }), 200

@app.route('/')
def home():
    return {"message": "Server running successfully"}

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)