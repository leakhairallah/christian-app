import config
import json
import os

from flask import Flask, request, jsonify, render_template
import gspread

from camel_morph.sandbox.debug_lemma_paradigms import regenerate_signature_lex_rows
from camel_morph.utils import utils

CONFIG_FILE = 'config_debug_lemma_paradigms.json'
SERVICE_ACCOUNT_PATH = 'service_account.json'

config_json = utils.get_config_file(CONFIG_FILE)
config_global = config_json['global']

service_account = json.loads(config.GSPREAD_API_KEY)
with open(SERVICE_ACCOUNT_PATH, 'w') as f:
    json.dump(service_account, f)

sa = gspread.service_account(SERVICE_ACCOUNT_PATH)
os.remove(SERVICE_ACCOUNT_PATH)

def get_config_name(sheet_name):
    if 'Noun-' in sheet_name:
        config_name = 'noun_msa_lemma_paradigms'
    elif 'Adj-' in sheet_name:
        config_name = 'adj_msa_lemma_paradigms'
    else:
        raise NotImplementedError
    return config_name

app = Flask(__name__)

@app.route('/regenerateSignature', methods=['POST'])
def regenerate_signature():
    # Process the input text from the frontend
    sheet_name = request.form.get('sheetName')
    spreadsheet = request.form.get('spreadsheetName')

    config_name = get_config_name(sheet_name)

    sh = sa.open(spreadsheet)
    sheets = sh.worksheets()

    sheet = [sheet for sheet in sheets if sheet.title == sheet_name][0]

    try:
        regenerate_signature_lex_rows(sheet, sh, config_json, config_name)
        return jsonify('SUCCESS')
    except:
        return 'FAILED; ERROR:regenerate_signature_lex_rows'

@app.route('/')
def index():
    sheets = [sheet for config_local in config_json['local'].values()
              for sheet in config_local['debugging']['sheets']]
    return render_template('index.html',
                           sheets=sheets)

