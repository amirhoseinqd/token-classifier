def is_identifier(token):
    return token.isidentifier() and not token.isdigit()

def is_number(token):
    try:
        float(token)
        return True
    except ValueError:
        return False

def is_symbol(token):
    symbols = ['(', ')', ';', '+', '*', '=', '>', '>=', '<', '<=', '!=', '==']
    return token in symbols

def is_keyword(token):
    keywords = ['int', 'char', 'if', 'then', 'else']
    return token in keywords

def classify_token(token):
    if is_identifier(token):
        return 'Identifier'
    elif is_number(token):
        return 'Number'
    elif is_symbol(token):
        return 'Symbol'
    elif is_keyword(token):
        return 'Keyword'
    else:
        return 'Unknown'
