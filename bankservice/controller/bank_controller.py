from flask import Blueprint, request
from api_reponse import get_success_response, get_error_response
import pandas
from ..controller.bank_service import process_and_save_new_bank_statement

bank_bp = Blueprint('bank', __name__)


@bank_bp.route('/upload/bank/statement', methods=['POST'])
def upload_bank_statement():
    if request.method == 'POST':
        file = request.files['file']
        # save file in local directory
        file.save(file.filename)
        data = pandas.read_excel(file)

        try:
            process_and_save_new_bank_statement(data, request['statement_number'], request['account_number'])
        except Exception as e:
            return get_error_response(str(e), "")

        return get_success_response("", "")
