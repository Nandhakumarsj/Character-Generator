import os
import google.generativeai as genai
from flask import Flask, request, render_template, render_template_string
from markupsafe import Markup
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])

    generation_config = {
        "temperature": 1.75,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash-exp",
        generation_config=generation_config,
    )

    theme = request.form.get('theme')
    name = request.form.get('name')
    age = request.form.get('age')
    gender = request.form.get('gender')
    height = request.form.get('height')
    weight = request.form.get('weight')
    build = request.form.get('build')
    hair = request.form.get('hair')
    eye = request.form.get('eye')
    clothing = request.form.get('clothing')
    accessories = request.form.get('accessories')
    personality = request.form.get('personality')
    skills = request.form.get('skills')
    character_background = request.form.get('character_background')

    height_and_weights = (f"* **Height:** {height}ft \"\n" if height else "")+ f"* **Weight:** {weight} lbs\n" if weight else ""
    clothings = ''.join([f"* {text}" for text in clothing.split('.')])
    all_accessories = ''.join([f"* {text}" for text in accessories.split(',')])
    characteristics = ''.join([f"* **{text}" for text in personality.split(',')])
    all_skills = ''.join([f"\n* **{text}" for text in personality.split(',')])
    prompt = [f"Write a character design in a {theme} theme.",
  f"input: Main Character ({gender})",
  f"output: **Name:** {name}\n\n**Appearance:**\n\n* **Age:** {age}\n{height_and_weights}* **Build:** {build}\n* **Hair:** {hair}\n* **Eyes:** {eye}\n* **Clothing:**\n{clothings}\n* **Accessories:**\n{all_accessories}\n\n**Personality:**\n\n{characteristics}\n\n**Skills:**\n\n{all_skills}\n\n**Background:**\n\n{'* '.join(character_background.splitlines())}",
  f"input: Main Character ({'Male' if (gender.lower() == 'female' or 'girl' or 'woman' or 'lady') else 'Female'})",
  "output: ",]

    response = model.generate_content(prompt)
    output = []
    for chunk in response:
        if chunk:
            output.append(chunk.text)

    output = "".join(output)
    rendered_html = Markup(output)

    return render_template_string("""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recipe Result</title>
</head>

<body>
    <h1>Generated Story</h1>
    {{rendered_html}}
    <a href="/">Create another Story</a>

</body>
</html>""", rendered_html=rendered_html)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
