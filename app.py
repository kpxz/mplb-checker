from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


def get_journal_content(journal):
	if journal == "ijitdm":
		return """As a subject matter expert of International Journal of Information Technology and Decision Making (IJITDM), evaluate the submitted paper's title and abstract against the journal's aims and scope, and state if the paper is a clear reject or if it seems to fit the journal. Do NOT evaluate anything else. Give good reasoning and if unsure, state why. 

Key Areas:
    AI and Decision Making
    Bioinformatics and Medical Decision Making
    Cluster Computing and Performance
    Data and Web Mining
    Data Warehousing and Applications
    Database Performance Evaluation
    Decision Making in Distributed Systems, E-Transactions, Internet Companies, Information Security, E-commerce, Internet-based Companies
    Decision Support Systems
    Decision Technologies in Information System Design
    Digital Library Designs
    Economic Decisions and Information Systems
    Enterprise Computing and Evaluation
    Fuzzy Logic and Internet
    Group Decision Making and Software
    Habitual Domain and IT
    Human-Computer Interaction
    Information Ethics, Legal Evaluations, Overload, Policy Making
    Information Retrieval Systems
    IT and Organizational Behavior
    Intelligent Agent Technologies
    Intelligent and Fuzzy Information Processing
    Internet Service and Training
    Knowledge Representation Models
    Decision Making via the Internet
    Multimedia and Decision Making
    MCDM in IT
    Network and Decision Making
    Neural Networks and Performance
    Online Business and Decision Making
    Optimization and IT
    Organizational Information Systems
    Pattern Recognition Models
    Parallel Computing Performance
    Reasoning under Uncertainty
    Social Decisions on the Internet
    Software Performance and Evaluation
    Telecommunication Systems and Evaluation
    Visualization and Decision Making
    Web-based Language Development
    Web Search and Decision Making
    Website Design and Development
    Wireless Technology and Performance"""
	elif journal == "mplb":
		return """As a subject matter expert of the academic research journal Modern Physics Letters B (MPLB), evaluate the submitted paper's title and abstract against the journal's aims and scope, and state if the paper is a clear reject or if it seems to fit the journal. Give good reasoning and if unsure, explain why. 

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
Statistical Thermodynamics"""



@app.route("/", methods=["GET", "POST"])
def index():
	if request.method == "POST":
		journal = request.form["journal"]
		title = request.form["title"]
		abstract = request.form["abstract"]

		prompt = f"Paper title: {title}\nPaper abstract: {abstract}"

		content = get_journal_content(journal)
		completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
		                                          messages=[{
		                                           "role": "system",
		                                           "content": content
		                                          }, {
		                                           "role": "user",
		                                           "content": prompt
		                                          }])

		answer = completion.choices[0].message.content
		return render_template("result.html", answer=answer)

	return render_template("index.html")


if __name__ == "__main__":
	app.run(debug=True)
