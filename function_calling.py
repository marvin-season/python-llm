import json

import ollama


def print_price(p):
    # Simulate API call to get stock price
    print(p)


funcs = {
    "print_price": print_price
}

tools = [
    {
        "type": "function",
        "function": {
            "name": "print_price",
            "description": "print price on the console log",
            "parameters": {
                "type": "object",
                "properties": {
                    "CNY": {
                        "type": "float",
                        "description": "人民币"
                    },
                    "DOLLAR": {
                        "type": "float",
                        "description": "美元"
                    }
                },
                "required": ["CNY", "DOLLAR"]
            }
        }
    }
]

response = ollama.chat(model='llama3.1', messages=[
    {
        'role': 'user',
        'content': '一部手机的平均价格',
    },
], tools=tools)

tool_calls = response['message']['tool_calls']

for tool_call in tool_calls:
    print(tool_call)
    if tool_call['function']:
        params = tool_call['function']['arguments']
        func_name = tool_call['function']['name']
        funcs[func_name](params)
