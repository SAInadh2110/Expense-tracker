
from flask import Flask, jsonify, request
import json
import sys


app = Flask(__name__)




# I defined a list of groups(groups = []), where each of the group structure is as follows:
# {
# "name" : "group_name",
# "members": ["mem1", "mem2","mem3",..]
# "expense": [expense1, expense2, expense3,...],
# balance_sheet: {}
# }
# Structure of each expense(expense'n') is:
#{
# "name": "expense_name",
# "items": []
# }
# Structure of each item in "items" is:
#{
# "name": "item_name",
# "value": item_value,
# "paid_by":[],
# "owed_by":[]
# }
#"paid_by" and "owed_by" are list of json structures of each item name mentioned in the "item_name", and the structure of each of the element in those lists are:
# paid_by:
#{
# "name1"(person1 name) : amount_paid
# "name2"(person2 name) : amount_paid
# "name3"(person3 name) : amount_paid
# .
# .
# }
# owed_by:
#{
# "name1"(person1 name) : amount_owed
# "name2"(person2 name) : amount_owed
# "name3"(person3 name) : amount_owed
# .
# .
# }

groups = []

# a sample group structure
''' 
Structure of each group in groups[] is:    
grp = {
    "name": "home",
    "memebers": ["A", "B", "C",...]
    "expenses": [
    {#expense1=>
        "name": "Fruits and Milk",
        "items": [{"name": "milk", "value": 50, "paid_by": [{"A": 40, "B": 10}], "owed_by": [{"A": 20,"B": 20, "C": 10}]},
                {"name": "fruits", "value": 50, "paid_by": [{"A": 50}], "owed_by": [{"A": 10,"B": 30, "C": 10}]}]
    },
    {#expense2=>...},
    {#expense3=>...},
    .
    .
    .]

        
    "balance_sheet": {
        "A": {
            "total_balance": -100.0
            "owes_to": [{"C": 100}],
            "owed_by": []
        },
        "B": {
            "total_balance": 0.0
            "owes_to": [],
            "owed_by": []
        },
        "C": {
            "total_balance": 100.0
            "owes_by": [{"A": 100}],
            "owed_to": []
        }
        .
        .
        .
    }
}
'''

# [A, B, C]

# new code
@app.route('/group', methods=['POST'])
def group_create():
    '''
    input data format
    {
        "name" : "SAMPLE NAME",
        "members": [A, B, C],
    }
    '''
    groups.append(request.json)
    print(groups)
    return "success",201

# @app.route('/group', methods=['POST', 'PUT'])
# def create_group():
#     if request.method == 'POST':
#         new_group_data = request.json   #The above mentioned structure for a group in groups[] is provided by the user initially here with 
#         groups.append(new_group_data)
#     else:
#         new_group_data = request.json
#         for group in groups:
#             if new_group_data['name'] == group['name']:     #If entered into the same group again that is previously in groups[]
#                 for ex in new_group_data['expense']:        #Acessing each expense entered in that group
#                     for item in ex['items']:            #Acessing each item in a particular expense
#                         for paid in item['paid_by']:    #Acessing payment of each item in 
#                             for mem in paid:
#                                 if mem not in group['members']:    #Checking for a new group member in that payments, if a particular member is not present in that group members, then we append that group member in the members of the group
#                                     group['members'].append(mem)
#                         for owed in item['owed_by']:    #Checking for a new group member in each "owed_by" structure and if a particular member is not present in that group members, then we append that group member in the members of the group
#                             for mem in owed:
#                                 if mem not in group['members']:
#                                     group['members'].append(mem)   #For adding a new member who is included in an expense but not included in the members of the group
#             else:
#                 groups.append(new_group_data)
#     return "success", 201

@app.route('/expense', methods=['POST', 'PUT', 'DELETE', 'GET'])
def create_expense():
    '''
    input data
    {
        "group_name" : "Home",
        "expense" :  {
                    "name": "Fruits and Milk",
                    "items": [{"name": "milk", "value": 50, "paid_by": [{"A": 40, "B": 10}], "owed_by": [{"A": 20,"B": 20, "C": 10}]},
                                {"name": "fruits", "value": 50, "paid_by": [{"A": 50}], "owed_by": [{"A": 10,"B": 30, "C": 10}]}]
                    }
    }
    '''
    if request.method == 'POST':
        for g in range(len(groups)):
            if groups[g]['name'] == request.json['group_name']:
                if groups[g].get('expenses') == None:
                    groups[g]['expenses'] = []
                groups[g]['expenses'].append(request.json['expense'])
                # adding a new person
                for item in request.json['expense']['items']:
                    item_paid_bys = item['paid_by']
                    for p in item_paid_bys:
                        for key in p: # p is dict
                            if key not in groups[g]['members']:
                                groups[g]['members'].append(key)
                    item_owed_bys = item['owed_by']
                    for p in item_owed_bys:
                        for key in p: # p is dict
                            if key not in groups[g]['members']:
                                groups[g]['members'].append(key)
        print(groups)
        return "success", 201 
        
    elif request.method == 'PUT':
        for g in range(len(groups)):
            if groups[g]['name'] == request.json['group_name']:
                for e in range(len(groups[g]['expenses'])):
                    if groups[g]['expneses'][e]['name'] == request.json['expense']['name']:
                        groups[g]['expenses'][e]['expense'] = request.json['expense']

                         # adding a new person
                        for item in request.json['expense']['items']:
                            item_paid_bys = item['paid_by']
                            for p in item_paid_bys:
                                for key in p: # p is dict
                                    if key not in groups[g]['members']:
                                        groups[g]['members'].append(key)
                            item_owed_bys = item['owed_by']
                            for p in item_owed_bys:
                                for key in p: # p is dict
                                    if key not in groups[g]['members']:
                                        groups[g]['members'].append(key)
        return "updated", 200

        
    elif request.method == 'DELETE':
        '''
        input data
        {
            "group_name": "SAMPLE_NAME",
            "expense_name": "expenditure_name"
        }
        '''
        for g in groups:
            if g['name'] == request.json['group_name']:
                for en in g['expenses']:
                    if en['name'] == request.json['expense_name']:
                        g['expenses'].pop(en)
        return "removed", 200
    elif request.method == 'GET':
        '''
        input data
        {
            "group_name": "name"
        }
        '''
        x = "None"
        #print(request.json)
        #print(groups)
        for g in groups:
            if g['name'] == request.json['group_name']:
                x = g.get(g['balance_sheet'], "None")
        return x, 200
        

@app.route('/balance', methods=['POST'])
def get_balance():
    '''
    request.json input=>
    {
        "group": "name"
    }
    
    '''
    #x = 0
    balance_sheet = {}
    
    print("groups is ",groups)
    for g in range(len(groups)):
        if request.json['group'] == groups[g]['name']:
            # print(g)
            # x = g
            # create a balance sheet
            dict_balance = {}
            for mem in groups[g]['members']:
                amount_paid = 0
                amount_owed = 0
                # paid - purchased = amount received (+ve : will get money, -ve: will give money)
                for ex in groups[g]['expenses']:
                    for item in ex["items"]:
                        amount_paid_by_all = item['paid_by']
                        for a in amount_paid_by_all:
                            amount_paid = amount_paid + a.get(mem,0)
        
                        if g in dict_balance:
                            dict_balance[mem]['paid_by'] =  dict_balance[mem]['paid_by'] + amount_paid
                        else:
                            dict_balance[mem] = {}
                            dict_balance[mem]['paid_by'] = amount_paid
                            dict_balance[mem]['owed_by'] = 0
        
                        amount_owed_by_all = item['owed_by']
                        for a in amount_owed_by_all:
                            amount_owed = amount_owed + a.get(mem,0)
                        dict_balance[mem]['owed_by'] = dict_balance[mem]['owed_by'] + amount_owed
    

            net_balance_dict = {}
            #print("--------------------------------------------------dict balance 00",dict_balance)
            for mem in groups[g]['members']:
                net_balance_dict[mem] = dict_balance[mem]['paid_by'] - dict_balance[mem]['owed_by']
                net_balance_dict[mem] = dict_balance[mem]['paid_by'] - dict_balance[mem]['owed_by']

            

            loan_sheet = {}
            for person,net_bal in net_balance_dict.items():
                #print(person, net_bal)
                loan_sheet[person] = {}
                loan_sheet[person]['owes_to'] = []
                loan_sheet[person]['owed_by'] = []
                loan_sheet[person]['total_balance'] = net_bal
                if net_bal > 0:
                    loan_sheet[person]['owes_to'] = []
                    for mem in groups[g]['members']:
                        if mem != person and net_balance_dict[mem] < 0:
                            print("loan_sheet ",loan_sheet)
                            print("person ",person)
                            print("net_balance_dict ",net_balance_dict)
                            print("g ",g)
                            loan_sheet[person]['owed_by'].append({mem: abs(net_balance_dict[mem])})
                elif net_bal < 0:
                    loan_sheet[person]['owed_by'] = []
                    for mem in groups[g]['members']:
                        if mem != person and net_balance_dict[mem] > 0:
                            loan_sheet[person]['owes_to'].append({mem: abs(net_balance_dict[person])})

            balance_sheet['name'] = request.json['group']
            balance_sheet['balances'] = loan_sheet
            groups[g]['balance_sheet'] = balance_sheet
    return "success",200
            

    
            
 
if __name__ == '__main__':
    app.run(debug=True)
