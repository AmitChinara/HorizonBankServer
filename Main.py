from flask import Flask, jsonify
from flask_cors import CORS

from Data import Data

app = Flask(__name__)
CORS(app)


@app.route('/')
def pageData():
    data = {f'main_page_info': f'{Data.main_page_info}', f'create_account_form': f'{Data.create_account_form}',
            f'account_login_info': f'{Data.account_login_info}', f'delete_account_form': f'{Data.delete_account_form}', f'create_account_left_input': f'{Data.create_account_left_input}', f'create_account_right_input': f'{Data.create_account_right_input}'}
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
