import json
x = {
   "name": "Fruits and Milk",
   "items": [{"name": "milk", "value": 50, "paid_by": [{"A": 40, "B": 10}], "owed_by": [{"A": 20,"B": 20, "C": 10}]},
             {"name": "fruits", "value": 50, "paid_by": [{"A": 50}], "owed_by": [{"A": 10,"B": 30, "C": 10}]}]
 }

groups = ["A", "B", "C"]
amount_a_purchased = 0
amount_a_paid = 0
# paid - purchased = amount received (+ve : will get money, -ve: will give money)
dict_balance = {}

for g in groups:
    amount_paid = 0
    amount_owed = 0
    for item in x["items"]:
        amount_paid_by_all = item['paid_by']
        for a in amount_paid_by_all:
            amount_paid = amount_paid + a.get(g,0)
        
        if g in dict_balance:
            dict_balance[g]['paid_by'] =  dict_balance[g]['paid_by'] + amount_paid
        else:
            dict_balance[g] = {}
            dict_balance[g]['paid_by'] = amount_paid
            dict_balance[g]['owed_by'] = 0
        
        amount_owed_by_all = item['owed_by']
        for a in amount_owed_by_all:
            amount_owed = amount_owed + a.get(g,0)
        dict_balance[g]['owed_by'] = dict_balance[g]['owed_by'] + amount_owed
    
    

print(dict_balance)    

net_balance_dict = {}

for g in groups:
    net_balance_dict[g] = dict_balance[g]['paid_by'] - dict_balance[g]['owed_by']
    
    
print(net_balance_dict)

final_sheet = {}

loan_sheet = {}
for person,net_bal in net_balance_dict.items():
    print(person, net_bal)
    loan_sheet[person] = {}
    loan_sheet[person]['owes_to'] = []
    loan_sheet[person]['owed_by'] = []
    loan_sheet[person]['total_balance'] = net_bal
    if net_bal > 0:
        loan_sheet[person]['owes_to'] = []
        for g in groups:
            if g != person and net_balance_dict[g] < 0:
                loan_sheet[person]['owed_by'].append({g: abs(net_balance_dict[g])})
    elif net_bal < 0:
        loan_sheet[person]['owed_by'] = []
        for g in groups:
            if g != person and net_balance_dict[g] > 0:
                loan_sheet[person]['owes_to'].append({g: abs(net_balance_dict[person])})

final_sheet['name'] = "home"
final_sheet['balances'] = loan_sheet
        
    
print(json.dumps(final_sheet,indent=4))
