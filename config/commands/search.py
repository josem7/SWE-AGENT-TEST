import sys
import hashlib
import os
from blar_graph.graph_construction.core.graph_builder import GraphConstructor
from blar_graph.db_managers import Neo4jManager
import subprocess
import tempfile
import sys

def format_print(code_lines, start_line):
    # Print formatted output
    print("Current node code:")
    for i, line in enumerate(code_lines, start=start_line):
        print(f"{i}: {line}")

def search_graph(query: str):
    repo_name = os.getenv("REPO_NAME")
    repo_id = hashlib.sha256(repo_name.encode()).hexdigest()
    graph_manager = Neo4jManager(repo_id)
    code, neighbours = graph_manager.get_code(query)
    if not code:
        return False
    code_text = code.get("node.text", "")
    start_line = code.get("node.start_line", 0)
    end_line = code.get("node.end_line", "")
    neighbours = neighbours
    file_path = code.get("node.file_path", "")

    if code_text is None:
        return False

    code_lines = code_text.split('\n')
    print(f"[File: {file_path}]")
    format_print(code_lines, start_line)
    print(f"\nCurrent Line {start_line} - {end_line}")
    print(f"\nCurrent node neighbours: {neighbours}")
    absolute_file_path = "/" + file_path
    with open("/temp.txt", "w") as f:
        f.write(f'export CURRENT_LINE="{start_line}"\n')
        f.write(f'export CURRENT_FILE="{absolute_file_path}"\n')
    return True

def search_graph_file_path(file_path: str, funciton_name: str):
    if funciton_name:
        result = search_graph(funciton_name)
        if result:
            sys.exit(0)
    result = search_graph(file_path)
    if not result:
        sys.exit(42)
    sys.exit(0)
    


    

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py query [function_name]")
        sys.exit(1)

    query = sys.argv[1]
    function_name = sys.argv[2] if len(sys.argv) >= 3 else None
    search_graph_file_path(query, function_name)

