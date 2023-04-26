from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form["title"]
        abstract = request.form["abstract"]

        prompt = f"Paper title: {title}\nPaper abstract: {abstract}\n\nDoes this paper fit the journal's Aims and Scope? Please explain."

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant. Answer the given question."},
                {"role": "user", "content": prompt}
            ]
        )

        answer = completion.choices[0].message.content
        return render_template("result.html", answer=answer)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
