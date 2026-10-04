"""RPyC server for Remote System Inspector & Math Utility."""

import ast
import math
import operator
import os
import platform
import time

import rpyc
from rpyc.utils.server import ThreadedServer


class SystemInspectorService(rpyc.Service):
    def exposed_get_system_info(self):
        return {
            "system": platform.system(),
            "release": platform.release(),
            "hostname": platform.node(),
            "cpu_count": os.cpu_count(),
            "server_time": time.strftime("%Y-%m-%d %H:%M:%S"),
        }

    def exposed_list_files(self, directory_path="."):
        try:
            return sorted(os.listdir(directory_path))
        except (FileNotFoundError, NotADirectoryError, PermissionError) as exc:
            return [f"ERROR: {exc}"]

    def exposed_compute_powers(self, base, max_exponent):
        max_exponent = int(max_exponent)
        if max_exponent < 0 or max_exponent > 100:
            return {"error": "Exponent must be between 0 and 100."}

        return {exponent: base ** exponent for exponent in range(max_exponent + 1)}

    def exposed_execute_expression(self, expression_str):
        """
        Safely evaluates basic arithmetic.
        Supports numbers, +, -, *, /, //, %, **, parentheses,
        and math.sqrt(...), math.sin(...), math.cos(...), math.tan(...).
        """
        allowed_functions = {
            "sqrt": math.sqrt,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "log": math.log,
        }

        try:
            tree = ast.parse(expression_str, mode="eval")
            return self._safe_eval(tree.body, allowed_functions)
        except Exception as exc:
            return f"ERROR: {exc}"

    def _safe_eval(self, node, functions):
        binary_ops = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.FloorDiv: operator.floordiv,
            ast.Mod: operator.mod,
            ast.Pow: operator.pow,
        }
        unary_ops = {
            ast.UAdd: operator.pos,
            ast.USub: operator.neg,
        }

        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value

        if isinstance(node, ast.BinOp) and type(node.op) in binary_ops:
            left = self._safe_eval(node.left, functions)
            right = self._safe_eval(node.right, functions)
            return binary_ops[type(node.op)](left, right)

        if isinstance(node, ast.UnaryOp) and type(node.op) in unary_ops:
            value = self._safe_eval(node.operand, functions)
            return unary_ops[type(node.op)](value)

        if isinstance(node, ast.Call):
            if (
                isinstance(node.func, ast.Attribute)
                and isinstance(node.func.value, ast.Name)
                and node.func.value.id == "math"
                and node.func.attr in functions
            ):
                args = [self._safe_eval(arg, functions) for arg in node.args]
                return functions[node.func.attr](*args)

        raise ValueError("Only basic arithmetic and approved math functions are allowed.")


if __name__ == "__main__":
    server = ThreadedServer(SystemInspectorService, port=18861)
    print("RPyC System Inspector Server running on port 18861...")
    server.start()
