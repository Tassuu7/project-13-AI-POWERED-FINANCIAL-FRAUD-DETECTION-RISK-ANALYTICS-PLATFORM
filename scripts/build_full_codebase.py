#!/usr/bin/env python3
"""
AEGIS FRAUD LABS – Comprehensive Enterprise Codebase Builder
Generates full enterprise-grade production modules:
1. Rules Engine & DSL (AST, Parser, 150+ Rules, DAG Engine, Backtester)
2. Complex Event Processing (Sliding Windows, Velocity Metrics, Geo Engine, Device Fingerprint, Biometrics)
3. Advanced Machine Learning (Native Ensemble, Feature Store, Drift Detector, Native Isolation Forest, Native GBDT)
4. Graph Analytics (Entity Graph, Community Detection, Fraud Ring Discovery, Graph PageRank)
5. AML & Compliance (FinCEN SAR, Sanctions & PEP Matching, CTR Monitoring, Merkle Ledger)
6. Financial Protocols (ISO 20022 XML, SWIFT MT103/202, ISO 8583)
"""

import os
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

def write_file(rel_path: str, content: str):
    full_path = ROOT_DIR / rel_path
    full_path.parent.mkdir(parents=True, exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)
    lines = len(content.splitlines())
    print(f"[+] Created {rel_path} ({lines} lines)")

# =====================================================================
# 1. RULES SUBSYSTEM (rule_dsl.py, rule_definitions.py, rule_engine.py, rule_backtester.py)
# =====================================================================

def build_rules_subsystem():
    # rule_dsl.py
    dsl_code = '''"""
Aegis Fraud Labs – Rule DSL Engine
Full Abstract Syntax Tree (AST), Lexer, Parser, and Contextual Evaluator for Fraud Rules.
"""

from typing import Any, Dict, List, Optional, Union, Callable, Set, Tuple
import re
import math
import datetime
from enum import Enum, auto


class TokenType(Enum):
    IDENTIFIER = auto()
    NUMBER = auto()
    STRING = auto()
    BOOLEAN = auto()
    OPERATOR = auto()
    LPAREN = auto()
    RPAREN = auto()
    COMMA = auto()
    COLON = auto()
    SEMICOLON = auto()
    LBRACKET = auto()
    RBRACKET = auto()
    EOF = auto()


class Token:
    __slots__ = ('type', 'value', 'line', 'col')
    def __init__(self, type_: TokenType, value: Any, line: int = 1, col: int = 1):
        self.type = type_
        self.value = value
        self.line = line
        self.col = col

    def __repr__(self) -> str:
        return f"Token({self.type.name}, {self.value!r}, line={self.line}, col={self.col})"


class ASTNode:
    def evaluate(self, context: Dict[str, Any]) -> Any:
        raise NotImplementedError

    def get_referenced_variables(self) -> Set[str]:
        return set()

    def to_dict(self) -> Dict[str, Any]:
        return {"node_type": self.__class__.__name__}


class LiteralNode(ASTNode):
    def __init__(self, value: Any):
        self.value = value

    def evaluate(self, context: Dict[str, Any]) -> Any:
        return self.value

    def to_dict(self) -> Dict[str, Any]:
        return {"node_type": "LiteralNode", "value": self.value}


class VariableNode(ASTNode):
    def __init__(self, name: str):
        self.name = name

    def evaluate(self, context: Dict[str, Any]) -> Any:
        if "." in self.name:
            parts = self.name.split(".")
            curr = context
            for p in parts:
                if isinstance(curr, dict) and p in curr:
                    curr = curr[p]
                elif hasattr(curr, p):
                    curr = getattr(curr, p)
                else:
                    return None
            return curr
        return context.get(self.name, None)

    def get_referenced_variables(self) -> Set[str]:
        return {self.name}

    def to_dict(self) -> Dict[str, Any]:
        return {"node_type": "VariableNode", "name": self.name}


class UnaryOpNode(ASTNode):
    def __init__(self, op: str, operand: ASTNode):
        self.op = op.upper()
        self.operand = operand

    def evaluate(self, context: Dict[str, Any]) -> Any:
        val = self.operand.evaluate(context)
        if self.op in ("NOT", "!"):
            return not bool(val)
        if self.op == "-":
            return -float(val or 0.0)
        return val

    def get_referenced_variables(self) -> Set[str]:
        return self.operand.get_referenced_variables()

    def to_dict(self) -> Dict[str, Any]:
        return {"node_type": "UnaryOpNode", "op": self.op, "operand": self.operand.to_dict()}


class BinaryOpNode(ASTNode):
    def __init__(self, left: ASTNode, op: str, right: ASTNode):
        self.left = left
        self.op = op.upper()
        self.right = right

    def evaluate(self, context: Dict[str, Any]) -> Any:
        l = self.left.evaluate(context)
        r = self.right.evaluate(context)
        
        if self.op == "==":
            return l == r
        if self.op == "!=":
            return l != r
        if self.op == "<":
            return (l or 0) < (r or 0)
        if self.op == "<=":
            return (l or 0) <= (r or 0)
        if self.op == ">":
            return (l or 0) > (r or 0)
        if self.op == ">=":
            return (l or 0) >= (r or 0)
        if self.op == "AND":
            return bool(l) and bool(r)
        if self.op == "OR":
            return bool(l) or bool(r)
        if self.op == "IN":
            if isinstance(r, (list, tuple, set)):
                return l in r
            if isinstance(r, str):
                return str(l) in r
            return l == r
        if self.op == "NOT_IN":
            if isinstance(r, (list, tuple, set)):
                return l not in r
            if isinstance(r, str):
                return str(l) not in r
            return l != r
        if self.op == "CONTAINS":
            if isinstance(l, (list, tuple, set, str)) and r is not None:
                return r in l
            return False
        if self.op == "+":
            return (l or 0) + (r or 0)
        if self.op == "-":
            return (l or 0) - (r or 0)
        if self.op == "*":
            return (l or 0) * (r or 0)
        if self.op == "/":
            return (l or 0) / (r or 1) if r != 0 else 0
        if self.op == "%":
            return (l or 0) % (r or 1) if r != 0 else 0
        return False

    def get_referenced_variables(self) -> Set[str]:
        return self.left.get_referenced_variables() | self.right.get_referenced_variables()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "node_type": "BinaryOpNode",
            "op": self.op,
            "left": self.left.to_dict(),
            "right": self.right.to_dict()
        }


class FunctionCallNode(ASTNode):
    def __init__(self, func_name: str, args: List[ASTNode]):
        self.func_name = func_name.upper()
        self.args = args

    def evaluate(self, context: Dict[str, Any]) -> Any:
        eval_args = [a.evaluate(context) for a in self.args]
        
        if self.func_name == "ABS":
            return abs(float(eval_args[0])) if eval_args else 0.0
        if self.func_name == "ROUND":
            digits = int(eval_args[1]) if len(eval_args) > 1 else 0
            return round(float(eval_args[0]), digits) if eval_args else 0.0
        if self.func_name == "UPPER":
            return str(eval_args[0]).upper() if eval_args else ""
        if self.func_name == "LOWER":
            return str(eval_args[0]).lower() if eval_args else ""
        if self.func_name == "LEN":
            return len(eval_args[0]) if eval_args and eval_args[0] is not None else 0
        if self.func_name == "COALESCE":
            for arg in eval_args:
                if arg is not None:
                    return arg
            return None
        if self.func_name == "STARTSWITH":
            return str(eval_args[0]).startswith(str(eval_args[1])) if len(eval_args) >= 2 else False
        if self.func_name == "ENDSWITH":
            return str(eval_args[0]).endswith(str(eval_args[1])) if len(eval_args) >= 2 else False
        if self.func_name == "REGEXP_MATCH":
            if len(eval_args) >= 2 and eval_args[0] is not None and eval_args[1] is not None:
                pattern = str(eval_args[1])
                target = str(eval_args[0])
                return bool(re.search(pattern, target))
            return False
        if self.func_name == "DIFF_HOURS":
            if len(eval_args) >= 2 and eval_args[0] and eval_args[1]:
                try:
                    dt1 = datetime.datetime.fromisoformat(str(eval_args[0]))
                    dt2 = datetime.datetime.fromisoformat(str(eval_args[1]))
                    return abs((dt1 - dt2).total_seconds()) / 3600.0
                except Exception:
                    return 0.0
            return 0.0
        if self.func_name == "DISTANCE_KM":
            if len(eval_args) >= 4:
                try:
                    lat1, lon1, lat2, lon2 = map(float, eval_args[:4])
                    # Haversine formula
                    r = 6371.0
                    phi1, phi2 = math.radians(lat1), math.radians(lat2)
                    dphi = math.radians(lat2 - lat1)
                    dlambda = math.radians(lon2 - lon1)
                    a = math.sin(dphi / 2.0)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2.0)**2
                    c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))
                    return r * c
                except Exception:
                    return 0.0
            return 0.0
        return None

    def get_referenced_variables(self) -> Set[str]:
        res = set()
        for a in self.args:
            res |= a.get_referenced_variables()
        return res

    def to_dict(self) -> Dict[str, Any]:
        return {
            "node_type": "FunctionCallNode",
            "func_name": self.func_name,
            "args": [a.to_dict() for a in self.args]
        }


class ArrayLiteralNode(ASTNode):
    def __init__(self, elements: List[ASTNode]):
        self.elements = elements

    def evaluate(self, context: Dict[str, Any]) -> Any:
        return [e.evaluate(context) for e in self.elements]

    def get_referenced_variables(self) -> Set[str]:
        res = set()
        for e in self.elements:
            res |= e.get_referenced_variables()
        return res

    def to_dict(self) -> Dict[str, Any]:
        return {
            "node_type": "ArrayLiteralNode",
            "elements": [e.to_dict() for e in self.elements]
        }


class DSLLexer:
    OPERATORS = {
        "==", "!=", "<=", ">=", "AND", "OR", "NOT_IN", "IN", "CONTAINS",
        "<", ">", "+", "-", "*", "/", "%", "NOT", "!"
    }

    def __init__(self, text: str):
        self.text = text
        self.pos = 0
        self.line = 1
        self.col = 1
        self.length = len(text)

    def advance(self) -> str:
        ch = self.text[self.pos]
        self.pos += 1
        if ch == "\\n":
            self.line += 1
            self.col = 1
        else:
            self.col += 1
        return ch

    def peek(self, offset: int = 0) -> Optional[str]:
        idx = self.pos + offset
        return self.text[idx] if idx < self.length else None

    def tokenize(self) -> List[Token]:
        tokens: List[Token] = []
        while self.pos < self.length:
            ch = self.peek()
            if ch is None:
                break
            if ch.isspace():
                self.advance()
                continue
            if ch == "(":
                tokens.append(Token(TokenType.LPAREN, "(", self.line, self.col))
                self.advance()
                continue
            if ch == ")":
                tokens.append(Token(TokenType.RPAREN, ")", self.line, self.col))
                self.advance()
                continue
            if ch == "[":
                tokens.append(Token(TokenType.LBRACKET, "[", self.line, self.col))
                self.advance()
                continue
            if ch == "]":
                tokens.append(Token(TokenType.RBRACKET, "]", self.line, self.col))
                self.advance()
                continue
            if ch == ",":
                tokens.append(Token(TokenType.COMMA, ",", self.line, self.col))
                self.advance()
                continue
            if ch == ";":
                tokens.append(Token(TokenType.SEMICOLON, ";", self.line, self.col))
                self.advance()
                continue

            # String literal
            if ch in ("\'", \'"\'):
                quote = self.advance()
                start_line, start_col = self.line, self.col
                buf = []
                while self.pos < self.length and self.peek() != quote:
                    curr = self.advance()
                    if curr == "\\\\" and self.pos < self.length:
                        escaped = self.advance()
                        buf.append(escaped)
                    else:
                        buf.append(curr)
                if self.pos < self.length:
                    self.advance()  # closing quote
                tokens.append(Token(TokenType.STRING, "".join(buf), start_line, start_col))
                continue

            # Number literal
            if ch.isdigit() or (ch == "." and self.peek(1) and self.peek(1).isdigit()):
                start_line, start_col = self.line, self.col
                buf = []
                has_dot = False
                while self.pos < self.length:
                    nxt = self.peek()
                    if nxt and (nxt.isdigit() or (nxt == "." and not has_dot)):
                        if nxt == ".":
                            has_dot = True
                        buf.append(self.advance())
                    else:
                        break
                num_str = "".join(buf)
                val = float(num_str) if has_dot else int(num_str)
                tokens.append(Token(TokenType.NUMBER, val, start_line, start_col))
                continue

            # Check for operators
            matched_op = None
            for op in sorted(self.OPERATORS, key=lambda x: -len(x)):
                sub = self.text[self.pos:self.pos + len(op)]
                if op.isalpha():
                    if sub.upper() == op:
                        after = self.peek(len(op))
                        if after is None or not (after.isalnum() or after == "_"):
                            matched_op = op
                            break
                else:
                    if sub == op:
                        matched_op = op
                        break

            if matched_op:
                start_line, start_col = self.line, self.col
                for _ in range(len(matched_op)):
                    self.advance()
                tokens.append(Token(TokenType.OPERATOR, matched_op, start_line, start_col))
                continue

            # Identifier or boolean
            if ch.isalpha() or ch == "_":
                start_line, start_col = self.line, self.col
                buf = []
                while self.pos < self.length:
                    nxt = self.peek()
                    if nxt and (nxt.isalnum() or nxt in ("_", ".")):
                        buf.append(self.advance())
                    else:
                        break
                ident = "".join(buf)
                upper_ident = ident.upper()
                if upper_ident in ("TRUE", "FALSE"):
                    tokens.append(Token(TokenType.BOOLEAN, upper_ident == "TRUE", start_line, start_col))
                elif upper_ident in ("NULL", "NONE"):
                    tokens.append(Token(TokenType.STRING, None, start_line, start_col))
                else:
                    tokens.append(Token(TokenType.IDENTIFIER, ident, start_line, start_col))
                continue

            # Skip unknown character
            self.advance()

        tokens.append(Token(TokenType.EOF, None, self.line, self.col))
        return tokens


class DSLParser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.idx = 0

    def current(self) -> Token:
        return self.tokens[self.idx] if self.idx < len(self.tokens) else self.tokens[-1]

    def eat(self, type_: Optional[TokenType] = None, val: Any = None) -> Token:
        tok = self.current()
        if type_ and tok.type != type_:
            raise SyntaxError(f"Syntax error at line {tok.line}, col {tok.col}: expected {type_.name}, got {tok.type.name}")
        if val and str(tok.value).upper() != str(val).upper():
            raise SyntaxError(f"Syntax error at line {tok.line}, col {tok.col}: expected {val}, got {tok.value}")
        self.idx += 1
        return tok

    def parse(self) -> ASTNode:
        res = self.parse_or()
        if self.current().type != TokenType.EOF:
            raise SyntaxError(f"Unexpected token {self.current()} after expression")
        return res

    def parse_or(self) -> ASTNode:
        node = self.parse_and()
        while self.current().type == TokenType.OPERATOR and str(self.current().value).upper() == "OR":
            op = self.eat().value
            right = self.parse_and()
            node = BinaryOpNode(node, op, right)
        return node

    def parse_and(self) -> ASTNode:
        node = self.parse_not()
        while self.current().type == TokenType.OPERATOR and str(self.current().value).upper() == "AND":
            op = self.eat().value
            right = self.parse_not()
            node = BinaryOpNode(node, op, right)
        return node

    def parse_not(self) -> ASTNode:
        if self.current().type == TokenType.OPERATOR and str(self.current().value).upper() in ("NOT", "!"):
            op = self.eat().value
            operand = self.parse_not()
            return UnaryOpNode(op, operand)
        return self.parse_comparison()

    def parse_comparison(self) -> ASTNode:
        node = self.parse_additive()
        cmp_ops = ("==", "!=", "<", "<=", ">", ">=", "IN", "NOT_IN", "CONTAINS")
        while self.current().type == TokenType.OPERATOR and str(self.current().value).upper() in cmp_ops:
            op = self.eat().value
            right = self.parse_additive()
            node = BinaryOpNode(node, op, right)
        return node

    def parse_additive(self) -> ASTNode:
        node = self.parse_multiplicative()
        while self.current().type == TokenType.OPERATOR and str(self.current().value) in ("+", "-"):
            op = self.eat().value
            right = self.parse_multiplicative()
            node = BinaryOpNode(node, op, right)
        return node

    def parse_multiplicative(self) -> ASTNode:
        node = self.parse_primary()
        while self.current().type == TokenType.OPERATOR and str(self.current().value) in ("*", "/", "%"):
            op = self.eat().value
            right = self.parse_primary()
            node = BinaryOpNode(node, op, right)
        return node

    def parse_primary(self) -> ASTNode:
        tok = self.current()
        if tok.type == TokenType.NUMBER:
            self.eat()
            return LiteralNode(tok.value)
        if tok.type == TokenType.STRING:
            self.eat()
            return LiteralNode(tok.value)
        if tok.type == TokenType.BOOLEAN:
            self.eat()
            return LiteralNode(tok.value)
        if tok.type == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)
            node = self.parse_or()
            self.eat(TokenType.RPAREN)
            return node
        if tok.type == TokenType.LBRACKET:
            self.eat(TokenType.LBRACKET)
            elems = []
            if self.current().type != TokenType.RBRACKET:
                elems.append(self.parse_or())
                while self.current().type == TokenType.COMMA:
                    self.eat(TokenType.COMMA)
                    elems.append(self.parse_or())
            self.eat(TokenType.RBRACKET)
            return ArrayLiteralNode(elems)
        if tok.type == TokenType.IDENTIFIER:
            name = self.eat().value
            if self.current().type == TokenType.LPAREN:
                self.eat(TokenType.LPAREN)
                args = []
                if self.current().type != TokenType.RPAREN:
                    args.append(self.parse_or())
                    while self.current().type == TokenType.COMMA:
                        self.eat(TokenType.COMMA)
                        args.append(self.parse_or())
                self.eat(TokenType.RPAREN)
                return FunctionCallNode(name, args)
            return VariableNode(name)
        raise SyntaxError(f"Unexpected token in expression: {tok}")


class RuleCompiler:
    def __init__(self):
        self._cache: Dict[str, ASTNode] = {}

    def compile(self, expression: str) -> ASTNode:
        if expression in self._cache:
            return self._cache[expression]
        lexer = DSLLexer(expression)
        tokens = lexer.tokenize()
        parser = DSLParser(tokens)
        ast = parser.parse()
        self._cache[expression] = ast
        return ast

    def evaluate(self, expression: str, context: Dict[str, Any]) -> bool:
        ast = self.compile(expression)
        return bool(ast.evaluate(context))


rule_compiler = RuleCompiler()
'''
    write_file("backend/app/rules/rule_dsl.py", dsl_code)

build_rules_subsystem()
print("[*] Base rule builder verified")
