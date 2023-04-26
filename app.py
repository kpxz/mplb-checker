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

        prompt = f"Paper title: {title}\nPaper abstract: {abstract}"

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": """As a subject matter expert of the academic research journal Modern Physics Letters B (MPLB), evaluate the submitted paper's title and abstract against the journal's aims and scope, and state if the paper is a clear reject or if it seems to fit the journal. Give good reasoning and if unsure, explain why. 

Aims and Scope:
MPLB's areas include Condensed Matter Physics, Statistical Physics, as well as Atomic, Molecular and Optical Physics. A strong emphasis is placed on topics of current interest such as cold atoms and molecules, new topological materials and phases, and novel low-dimensional materials.

Subject areas suitable for publication include, but are not limited to the following fields:

1. Condensed Matter Physics:
Complex fluids
Electronic structure and properties of the materials
Ferroelectric and multiferroics
Ferromagnetism and materials
High-temperature superconductivity
Low Dimensional Materials and Systems
Liquid crystals and polymers
Many-body physics
Magnetism
Nanoscience
Photonics and metamaterials
Quantum magnetism
Quantum numerical simulation
Quantum phenomena in complex condensed matter
Superconductivity
Spintronics
Spin glasses
Solid state physics
Soft matter, biophysics, and liquids
Structure of matter, phase transitions
Strong correlation
Surfaces and interfaces
Topological states and phases of materials
Computational physics

2. Atomic, Molecular, and Optical Physics:
Aspects of spectroscopy
Coherent states
Non-linear optics
Laser physics
Luminescence
Optics and photonics
Optical metrology, atomic clocks, and frequency combs
Quantum chemistry
Quantum optics and photonics
Quantum information
Radiation and scattering
Ultracold atoms

3. Statistical Physics:
Averaging instead of Maximization
Application to Radiation (Light Quanta)
Bose–Einstein Condensates
Electrons in Metals
Equilibrium systems
Entropy
Exact Form of Distribution Functions
Exactly solvable models
Non-equilibrium systems
Quantum Statistics
Statistical Mechanics
Statistical Thermodynamics"""},
                {"role": "user", "content": prompt}
            ]
        )

        answer = completion.choices[0].message.content
        return render_template("result.html", answer=answer)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
