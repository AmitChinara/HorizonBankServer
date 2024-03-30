class Data:

    main_page_info = """<div class="option-container"> <div class="options" id="option-1" onclick="createAccount(
    )"><div class="text-container" id="text-1"><p>CREATE ACCOUNT</p></div></div> <div class="options" id="option-2" 
    onclick="createAccountLogin()"><div class="text-container" id="text-2"><p>ACCOUNT LOGIN</p></div></div> <div 
    class="options" id="option-3" onclick="createAccountDelete()"><div class="text-container" id="text-3"><p>DELETE 
    ACCOUNT</p></div></div> </div>"""

    create_account_form = """<div class="form-container">
                    <div class="form-division" id="upper">
                        <div class="sub-division upper-sub-division" id="upper-division-1"><div class="create-account-input-container"></div></div>
                        <div class="sub-division upper-sub-division" id="upper-division-2"><div class="create-account-input-container"></div></div>
                    </div>
                    <div class="form-division" id="lower">
                        <div class="sub-division lower-sub-division" id="lower-division-1">
                            <div class="buttons" id="submit-button"><p>SUBMIT</p></div>
                        </div>
                        <div class="sub-division lower-sub-division" id="lower-division-2">
                            <div class="buttons" id="clear-button" onclick="createAccountClear()"><p>CLEAR</p></div>
                        </div>
                    </div>
                </div>"""

    account_login_info = """ """

    delete_account_form = """ """

    create_account_left_input = """<div class="input-container" id="input-field-1"><input type="text" id="first-name" class="input-field" placeholder="FIRST NAME"></div>
                            <div class="input-container" id="input-field-2"><input type="text" id="last-name" class="input-field" placeholder="LAST NAME"></div>
                            <div class="input-container" id="input-field-3"><input type="email" id="email-id" class="input-field" placeholder="EMAIL ID"></div>"""

    create_account_right_input = """<div class="input-container" id="input-field-4"><input type="date" class="input-field" id="date-of-birth"></div>
                            <div class="input-container" id="input-field-5"><input type="password" id="pin" class="input-field" placeholder="PIN" oninput="checkPin(1)"></div>
                            <div class="input-container" id="input-field-6"><input type="password" id="confirm-pin" class="input-field" placeholder="CONFIRM PIN" oninput="checkPin(2)"></div>"""
