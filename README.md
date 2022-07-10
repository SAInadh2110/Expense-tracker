# task

## Installation instructions

```
pip install -r requirements.txt
```

## Run

```
python app.py
```
# URL's Endpoints:

## 1. User Input for '/group' Endpoint:

```
User should initially enter the '/group' endpoint, and provide the following details in the "POST" HTTP method, in the below format(dict format in python)

Input data format example:
    {
        "name" : "Home",
        "members": ["A", "B", "C"]
    }
```
## Output:

```
success
```
## 2. User Input for '/expense' Endpoint:

### "POST" HTTP method:

```
To add an expense to a particular group, user should enter the following input in "POST" method, in the below format(dict format in python)

Input data format example:
    {
        "group_name" : "Home",      ----> Name of the group in which the expense is to be added
        "expense" :  {
                    "name": "Fruits and Milk",
                    "items": [{"name": "milk", "value": 50, "paid_by": [{"A": 40, "B": 10}], "owed_by": [{"A": 20,"B": 20, "C": 10}]},
                                {"name": "fruits", "value": 50, "paid_by": [{"A": 50}], "owed_by": [{"A": 10,"B": 30, "C": 10}]}]
                    }
    }
```
### Output:

```
success
```

### "PUT" HTTP method:

```
To update an expense to a particular group, user should enter the following input in "PUT" method, in the below format(dict format in python)

(Same as that provided in "POST" method) Input example:
{
        "group_name" : "Home",      ----> Name of the group in which the expense is to be updated
        "expense" :  {
                    "name": "Fruits and Milk",
                    "items": [{"name": "milk", "value": 50, "paid_by": [{"A": 40, "B": 10}], "owed_by": [{"A": 20,"B": 20, "C": 10}]},
                                {"name": "fruits", "value": 50, "paid_by": [{"A": 50}], "owed_by": [{"A": 10,"B": 30, "C": 10}]}]
                    }
}
```
### Output:

```
updated
```
### "DELETE" HTTP method:

```
To remove an expense of a particular group, user should enter the following input in "DELETE" method, in the below format(dict format in python)

Input example:
    {
            "group_name": "Home",
            "expense_name": "Fruits and Milk"
    }
```
### Output:

```
removed
```
### "GET" HTTP method:

```
To get the balance of a group such that the balances are simplified, user should enter the following input in "GET" method, in the below format(dict format in python)

Input example:
    {
            "group_name": "Home"
    }
```
### Output:

```
{
    "balances": {
        "A": {
            "owed_by": [
                {
                    "B": 40
                },
                {
                    "C": 20
                }
            ],
            "owes_to": [],
            "total_balance": 60
        },
        "B": {
            "owed_by": [],
            "owes_to": [
                {
                    "A": 40
                }
            ],
            "total_balance": -40
        },
        "C": {
            "owed_by": [],
            "owes_to": [
                {
                    "A": 20
                }
            ],
            "total_balance": -20
        }
    },
    "name": "Home"
}
```
## 3. User Input for 'balance' Endpoint:

```
To get the balance of a group, we need to first create the balance_sheet structure, so user should first provide the input in the "POST" HTTP method in '/balance' endpoint first, to create a balance_sheet for the group, and then the user should provide the same input in the "GET" HTTP method in '/expense' endpoint to get the balance of the group.
```
### Input in "POST" HTTP method:

```
After providing the input provided in "POST" HTTP method in '/balance' endpoint, we provide the same input in the "GET" HTTP method in '/expense' endpoint to get the balance of the group. So, we provide that input here first.

Input example:
    {
            "group_name": "Home"
    }
```
### Output:

```
success
```
