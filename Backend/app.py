from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/annotate', methods=['POST'])
def annotate():
    # Process the input text from the frontend
    input_text = request.form.get('input_text')
    
    # Implement your annotation logic here

    # Return the annotated text as a JSON response
    response = {'annotated_text': annotated_text}
    return jsonify(response)

@app.route('/annotate2', methods=['POST'])
def annotate2():
    # Process the input text from the frontend
    input_text = request.form.get('input_text')
    
    # Implement your annotation logic here

    # Return the annotated text as a JSON response
    response = {'annotated_text': annotated_text}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
