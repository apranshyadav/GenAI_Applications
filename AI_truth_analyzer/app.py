from flask import Flask, request, render_template
from analyzer import analyze_text

app = Flask(__name__)

session_store = {}


def get_session(user_id):
    """Create or retrieve session config"""
    if user_id not in session_store:
        session_store[user_id] = {
            "history": []
        }
    return session_store[user_id]


@app.route('/')
def home():
    return render_template(
        'index.html',
        result=None,
        user_id="user1",
        history=[]
    )


@app.route('/analyze', methods=['POST'])
def analyze():
    user_id = request.form.get('user_id')
    text = request.form.get('text')

    if not text:
        return render_template(
            'index.html',
            result=None,
            user_id=user_id,
            history=[]
        )

    session_data = get_session(user_id)

    result = analyze_text(text)

    session_data["history"].append({
        "input": text,
        "output": result
    })

    return render_template(
        'index.html',
        result=result,
        user_id=user_id,
        history=session_data["history"]
    )


@app.route('/clear')
def clear():
    user_id = request.args.get("user_id", "user1")

    if user_id in session_store:
        session_store[user_id]["history"] = []

    return render_template(
        'index.html',
        result=None,
        user_id=user_id,
        history=[]
    )


if __name__ == '__main__':
    app.run(debug=True)