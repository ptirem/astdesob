import json
import sys

def parse_expression(expr):
    t = expr["type"]
    if t == "Literal":
        return repr(expr["value"])
    elif t == "Identifier":
        return expr["name"]
    elif t == "ArrayExpression":
        return "[" + ", ".join(parse_expression(e) for e in expr["elements"] if e) + "]"
    elif t in ["BinaryExpression", "AssignmentExpression"]:
        left = parse_expression(expr["left"])
        right = parse_expression(expr["right"])
        return f"({left} {expr['operator']} {right})"
    elif t == "CallExpression":
        callee_expr = expr["callee"]
        # Vérifie si le callee est une fonction (fléchée ou non) pour parenthéser explicitement
        if callee_expr["type"] in ["ArrowFunctionExpression", "FunctionExpression"]:
            callee = f"({parse_expression(callee_expr)})"
        else:
            callee = parse_expression(callee_expr)
        args = ", ".join(parse_expression(arg) for arg in expr["arguments"])
        return f"{callee}({args})"

    elif t == "MemberExpression":
        obj = parse_expression(expr["object"])
        prop = parse_expression(expr["property"])
        return f"{obj}.{prop}"
    elif t in ["ArrowFunctionExpression", "FunctionExpression"]:
        params = ", ".join(p["name"] for p in expr["params"])
        body = parse_block(expr["body"]) if not expr["expression"] else parse_expression(expr["body"])

        # Détecter si la fonction est immédiatement invoquée
        is_iife = expr.get('is_iife', False)
        if is_iife:
            return f"({params}) => {body}"
        else:
            return f"({params}) => {body}"

    elif t == "UnaryExpression":
        arg = parse_expression(expr["argument"])
        return f"{expr['operator']}{arg}"
    elif t == "ObjectExpression":
        return "{ /* object */ }"
    else:
        return f"/* Unsupported expression: {t} */"

def parse_statement(stmt):
    t = stmt["type"]
    if t == "VariableDeclaration":
        kind = stmt["kind"]
        return "\n".join(f"{kind} {decl['id']['name']} = {parse_expression(decl['init'])};"
                         for decl in stmt["declarations"])
    elif t == "ExpressionStatement":
        expr = parse_expression(stmt["expression"])
        if expr.startswith("(() =>") or expr.startswith("(function"):
            return f"{expr};"
        return expr + ";"
    elif t == "ReturnStatement":
        return "return " + parse_expression(stmt["argument"]) + ";"
    elif t == "FunctionDeclaration":
        return parse_function(stmt)
    elif t == "IfStatement":
        test = parse_expression(stmt["test"])
        cons = parse_block(stmt["consequent"])
        return f"if ({test}) {cons}"
    elif t == "BlockStatement":
        return parse_block(stmt)
    else:
        return f"// Unsupported statement: {t}"

def parse_block(block):
    return "{\n" + "\n".join(parse_statement(stmt) for stmt in block["body"] if stmt["type"] != "EmptyStatement") + "\n}"

def parse_function(func):
    name = func["id"]["name"]
    params = ", ".join(p["name"] for p in func["params"])
    body = parse_block(func["body"])
    return f"function {name}({params}) {body}"

def parse_program(ast):
    lines = []
    for stmt in ast["body"]:
        if stmt["type"] == "jaajajajajajajajajajajajaj":
            continue
        lines.append(parse_statement(stmt))
    return "\n\n".join(lines)

def main(filepath):
    
    try:
        with open(filepath, 'r') as f:
            ast = json.load(f)
    except FileNotFoundError:
        print("Le fichier n'existe pas.")
    
    js_code = parse_program(ast)
    
    
    print(js_code)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script.py <path_to_ast.json>")
        sys.exit(1)
    main(sys.argv[1])