from flask import Flask
from flask_cors import CORS
from flask import jsonify, Response
from flask_restful import Api, Resource
import pandas as pd
import numpy as np
from datetime import datetime
import requests
import json

# from .routes import intialize_routes

app = Flask(__name__)
CORS(app)
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)

# intialize_routes(api)

user = requests.get('https://infy-money-nodejs.herokuapp.com/api/users/mobile/9999999999')
user_json = user.json()


## ALL THE KEYS
bonds = user_json['fi_data']['BONDS'][0]
credit_card = user_json['fi_data']['CREDIT_CARD'][0]
deposit = user_json['fi_data']['DEPOSIT'][0]
recurring_deposit = user_json['fi_data']['RECURRING_DEPOSIT'][0]
term_deposit = user_json['fi_data']['TERM_DEPOSIT'][0]
mutual_funds = user_json['fi_data']['MUTUAL_FUNDS'][0]
equities = user_json['fi_data']['EQUITIES'][0]
epf = user_json['fi_data']['EPF'][0]
etf = user_json['fi_data']['ETF'][0]
nps = user_json['fi_data']['NPS'][0]
govt_securities = user_json['fi_data']['GOVT_SECURITIES'][0]
insurance_policies = user_json['fi_data']['INSURANCE_POLICIES'][0]
ulip = user_json['fi_data']['ULIP'][0]
ppf = user_json['fi_data']['PPF'][0]


## TotalAssets = Assets - Liabilities
bonds_current_value = float(bonds['summary']['currentValue'])
term_deposit_current_value = float(term_deposit['summary']['currentValue'])
credit_card_total_due = float(credit_card['summary']['totalDueAmount'])
ppf_current_balance = float(ppf['summary']['currenBalance'])
recurring_deposit_current_value = float(recurring_deposit['summary']['currentValue'])
govt_securities_current_value = float(govt_securities['summary']['currentValue'])
equities_current_value = float(equities['summary']['currentValue'])
mutual_funds_current_value = float(mutual_funds['summary']['currentValue'])
etf_current_value = float(etf['summary']['currentValue'])
nps_current_value = float(nps['summary']['currentValue'])
epf_total_balance = float(epf['summary']['totalBalance'])

##### Credit Card details ##########
Credit_debit_time = []
Credit_amount = []
Debit_amount = []

for i in range(1,30):
    time_ori_format = credit_card['transactions']['transaction'][i]['txnDate']
    d = datetime.fromisoformat(time_ori_format)
    credit_card['transactions']['transaction'][i]['txn_Date'] = d.strftime('%d-%m-%Y %H:%M:%S')
    Credit_debit_time.append(credit_card['transactions']['transaction'][i]['txn_Date'])
    credit_card['transactions']['transaction'][i]['amount'] = float(credit_card['transactions']['transaction'][i]['amount'])
    if credit_card['transactions']['transaction'][i]['txnType'] == 'DEBIT':
        Debit_amount.append(credit_card['transactions']['transaction'][i]['amount'])
        Credit_amount.append(None)
    elif credit_card['transactions']['transaction'][i]['txnType'] == 'CREDIT':
         Credit_amount.append(credit_card['transactions']['transaction'][i]['amount'])
         Debit_amount.append(None)


######## Trade Value and Invesment Value of Investments ####################
bonds_txn_date = []
equities_txn_date = []
govt_securities_txn_date = []
bonds_trade_value = []
equities_trade_value = []
govt_securities_trade_value = []
    
for i in range(0,8):
    equities_trade_value.append(float(equities['transactions']['transaction'][i]['tradeValue']))
    time_ori_format = equities['transactions']['transaction'][i]['transactionDateTime']
    d = datetime.fromisoformat(time_ori_format)
    equities['transactions']['transaction'][i]['transactionDateTime'] = d.strftime('%d-%m-%Y')
    equities_txn_date.append(equities['transactions']['transaction'][i]['transactionDateTime'])
    

    
for i in range(0,18):
    govt_securities_trade_value.append(float(govt_securities['transactions']['transaction'][i]['tradeValue']))
    time_ori_format = govt_securities['transactions']['transaction'][i]['transactionDateTime']
    d = datetime.fromisoformat(time_ori_format)
    govt_securities['transactions']['transaction'][i]['transactionDateTime'] = d.strftime('%d-%m-%Y')
    govt_securities_txn_date.append(govt_securities['transactions']['transaction'][i]['transactionDateTime'])
    

    bonds_trade_value.append(float(bonds['transactions']['transaction'][i]['tradeValue']))
    time_ori_format = bonds['transactions']['transaction'][i]['transactionDateTime']
    d = datetime.fromisoformat(time_ori_format)
    bonds['transactions']['transaction'][i]['transactionDateTime'] = d.strftime('%d-%m-%Y')
    bonds_txn_date.append(bonds['transactions']['transaction'][i]['transactionDateTime'])
    

equities_invest_value = float(equities['summary']['investmentValue'])
govt_securities_invest_value = float(govt_securities['summary']['investmentValue'])
bonds_invest_value = float(bonds['summary']['investmentValue'])
etf_invest_value = float(etf['summary']['investmentValue'])
mf_invest_value = float(mutual_funds['summary']['investmentValue'])
nps_invest_value = float(nps['summary']['holdings']['tier1Holdings']['investmentValue'])

trade_txn_date = list(set(bonds_txn_date + equities_txn_date + govt_securities_txn_date))


########## Deposit + RD + TD ###############
deposit_credit_amount = []
deposit_debit_amount = []
deposit_credit_debit_time = []

RD_credit_amount = []
RD_debit_amount = []
RD_credit_debit_time = []

TD_credit_amount = []
TD_credit_debit_time = []
TD_debit_amount = []

deposit_credit_amount_neg = []
RD_credit_amount_neg = []
TD_credit_amount_neg = []


for i in range(30):
    time_ori_format = deposit['transactions']['transaction'][i]['transactionTimestamp']
    d = datetime.fromisoformat(time_ori_format)
    deposit['transactions']['transaction'][i]['txn_Date'] = d.strftime('%d-%m-%Y %H:%M:%S')
    deposit_credit_debit_time.append(deposit['transactions']['transaction'][i]['txn_Date'])

    deposit['transactions']['transaction'][i]['amount'] = float(deposit['transactions']['transaction'][i]['amount'])
    if deposit['transactions']['transaction'][i]['type'] == 'DEBIT':
        deposit_debit_amount.append(deposit['transactions']['transaction'][i]['amount'])
        deposit_credit_amount.append(None)
        deposit_credit_amount_neg.append(None)
    elif deposit['transactions']['transaction'][i]['type'] == 'CREDIT':
         deposit_credit_amount.append(deposit['transactions']['transaction'][i]['amount'])
         deposit_credit_amount_neg.append(-(deposit['transactions']['transaction'][i]['amount']))
         deposit_debit_amount.append(None)


    time_ori_format = recurring_deposit['transactions']['transaction'][i]['transactionTimestamp']
    d = datetime.fromisoformat(time_ori_format)
    recurring_deposit['transactions']['transaction'][i]['txn_Date'] = d.strftime('%d-%m-%Y %H:%M:%S')
    RD_credit_debit_time.append(recurring_deposit['transactions']['transaction'][i]['txn_Date'])

    recurring_deposit['transactions']['transaction'][i]['amount'] = float(recurring_deposit['transactions']['transaction'][i]['amount'])
    if recurring_deposit['transactions']['transaction'][i]['type'] == 'DEBIT':
        RD_debit_amount.append(recurring_deposit['transactions']['transaction'][i]['amount'])
        RD_credit_amount.append(None)
        RD_credit_amount_neg.append(None)
    elif recurring_deposit['transactions']['transaction'][i]['type'] == 'CREDIT':
        RD_credit_amount.append(recurring_deposit['transactions']['transaction'][i]['amount'])
        RD_credit_amount_neg.append(-(recurring_deposit['transactions']['transaction'][i]['amount']))
        RD_debit_amount.append(None)


    time_ori_format = recurring_deposit['transactions']['transaction'][i]['transactionTimestamp']
    d = datetime.fromisoformat(time_ori_format)
    recurring_deposit['transactions']['transaction'][i]['txn_Date'] = d.strftime('%d-%m-%Y %H:%M:%S')
    TD_credit_debit_time.append(recurring_deposit['transactions']['transaction'][i]['txn_Date'])

    term_deposit['transactions']['transaction'][i]['amount'] = float(term_deposit['transactions']['transaction'][i]['amount'])
    if term_deposit['transactions']['transaction'][i]['type'] == 'DEBIT':
        TD_debit_amount.append(recurring_deposit['transactions']['transaction'][i]['amount'])
        TD_credit_amount.append(None)
        TD_credit_amount_neg.append(None)
    elif term_deposit['transactions']['transaction'][i]['type'] == 'CREDIT':
        TD_credit_amount.append(term_deposit['transactions']['transaction'][i]['amount'])
        TD_credit_amount_neg.append(-(term_deposit['transactions']['transaction'][i]['amount']))
        TD_debit_amount.append(None)


########## pensions ##############

ppf_amount = []
ppf_txn_date = []
ppf_balance = []

epf_txn_date = []
epf_emp_amount = []
epf_pension_amount = []


for i in range(len(ppf['transactions']['transaction'])):
    time_ori_format = ppf['transactions']['transaction'][i]['txnDate']
    d = datetime.fromisoformat(time_ori_format)
    ppf['transactions']['transaction'][i]['txn_Date'] = d.strftime('%d-%m-%Y')
    ppf_txn_date.append(ppf['transactions']['transaction'][i]['txn_Date'])
    ppf['transactions']['transaction'][i]['amount'] = float(ppf['transactions']['transaction'][i]['amount'])
    ppf['transactions']['transaction'][i]['balance'] = float(ppf['transactions']['transaction'][i]['balance'])
    ppf_amount.append(ppf['transactions']['transaction'][i]['amount'])
    ppf_balance.append(ppf['transactions']['transaction'][i]['balance'])

for i in range(len(epf['transactions']['transaction'])):
    time_ori_format = epf['transactions']['transaction'][i]['txnDate']
    d = datetime.fromisoformat(time_ori_format)
    epf['transactions']['transaction'][i]['txn_Date'] = d.strftime('%d-%m-%Y')
    epf_txn_date.append(epf['transactions']['transaction'][i]['txn_Date'])
    epf['transactions']['transaction'][i]['employeeDepositAmount'] = float(epf['transactions']['transaction'][i]['employeeDepositAmount'])
    epf['transactions']['transaction'][i]['pensionFundAmount'] = float(epf['transactions']['transaction'][i]['pensionFundAmount'])
    epf_emp_amount.append(epf['transactions']['transaction'][i]['employeeDepositAmount'])
    epf_pension_amount.append(epf['transactions']['transaction'][i]['pensionFundAmount'])








###########################################

class total_asset(Resource):
    def get(self):

        asset = term_deposit_current_value + recurring_deposit_current_value + epf_total_balance + ppf_current_balance + govt_securities_current_value + mutual_funds_current_value + bonds_current_value + equities_current_value + nps_current_value + etf_current_value
        liabilities = credit_card_total_due
        T_Asset = asset - liabilities

        asset_json = {"asset" : asset, "liabilities" : liabilities, "TA" : T_Asset}
        return asset_json

class liabilities(Resource):
    def get(self):
        CC_Month_Due = float(credit_card['summary']['currentDue'])
        CC_Financial_charges = float(credit_card['summary']['financeCharges'])
        CC_Due_Date = credit_card['summary']['dueDate']
        CC_Previous_Due = float(credit_card['summary']['previousDueAmount'])

        liabilities_json = {"Due_Date" : CC_Due_Date , "Total_Due" : credit_card_total_due, "Financial_Charges" : CC_Financial_charges, "Pre_Month_Due" : CC_Previous_Due, "Month_Due" : CC_Month_Due}

        return liabilities_json

class credit_debit(Resource):
    def get(self):

        credit_debit_json = {"Credit_debit_time" : Credit_debit_time, "credit_amount" : Credit_amount, "debit_amount" : Debit_amount}

        return credit_debit_json


class trade_value(Resource):
    def get(self):

        trade_value_json = {"trade_txn_date" : trade_txn_date, "bonds_trade_value" : bonds_trade_value, "equities_trade_value": equities_trade_value, "govt_securities_trade_value": govt_securities_trade_value, "bonds_invest_value" : bonds_invest_value, "equities_invest_value" : equities_invest_value, "govt_securities_invest_value": govt_securities_invest_value, "mf_invest_value" : mf_invest_value, "nps_invest_value" : nps_invest_value, "etf_invest_value": etf_invest_value}

        return trade_value_json


class deposits(Resource):
    def get(self):

        deposits_json = {"TD_credit_debit_time" : TD_credit_debit_time, "RD_credit_debit_time" :RD_credit_debit_time, "deposit_credit_debit_time" : deposit_credit_debit_time, "RD_debit_amount": RD_debit_amount, "TD_debit_amount" : TD_debit_amount ,"deposit_debit_amount": deposit_debit_amount, "RD_credit_amount": RD_credit_amount, "TD_credit_amount": TD_credit_amount, "deposit_credit_amount": deposit_credit_amount, "deposit_credit_amount_neg": deposit_credit_amount_neg, "RD_credit_amount_neg": RD_credit_amount_neg, "TD_credit_amount_neg": TD_credit_amount_neg}
        return deposits_json


class pension(Resource):
    def get(self):

        pensions_json = {"ppf_amount" : ppf_amount, "ppf_balance" : ppf_balance, "ppf_txn_date" : ppf_txn_date, "epf_emp_amount": epf_emp_amount, "epf_pension_amount": epf_pension_amount, "epf_txn_date": epf_txn_date}
        return pensions_json




api.add_resource(total_asset,"/total_asset")
api.add_resource(liabilities,"/liabilities")
api.add_resource(credit_debit,"/credit_debit")
api.add_resource(trade_value,"/trade_value")
api.add_resource(deposits,"/deposits")
api.add_resource(pension,"/pension")

# @app.route("/")
# def UserData():
#     return (epf)


if __name__ == "__main__":
    app.run(debug=True)
