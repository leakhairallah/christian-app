from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/annotate', methods=['POST'])
def annotate():
    # Process the input text from the frontend
    sheet = request.form.get('sheetName')
    spreadsheet = request.form.get('spreadsheetName')
    
    # Implement your annotation logic here

    # Return the annotated text as a JSON response
    response = {'sheet': sheet, 'spreadsheet': spreadsheet}
    return jsonify(response)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
