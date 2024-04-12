#!/usr/bin/env python3
import sys
import hashlib
from blar_graph.graph_construction.core.graph_builder import GraphConstructor
from blar_graph.db_managers import Neo4jManager

def build_graph(repo_name: str):
    repo_id = hashlib.sha256(repo_name.encode()).hexdigest()
    graph_manager = Neo4jManager(repo_id)
    graph_manager.query(f"MATCH (n {{repo_id: '{repo_id}'}}) DETACH DELETE n")
    graph_constructor = GraphConstructor(graph_manager, "python")
    graph_constructor.build_graph(repo_name)

if __name__ == "__main__":
    repo_name = sys.argv[1]
    build_graph(repo_name)
