_activate_env() {
    if [ -n "$1" ]; then
        conda activate "$1"
    else
        echo "Error: Environment name not provided."
    fi
}


# @yaml
# signature: search_function <search_term>
# docstring: Returns a function code given a query, the query can be a function name, a path or a node_id. returns the node text and the neighbors of the node.
# arguments:
#   query:
#     type: string
#     description: the term to search for, it can be a function name, a path or a node_id
#     required: true

search_function() {
    if [ -z "$1" ]; then
        echo "Usage: search_function <search_term>"
        return
    fi
    local search_term="$1"

    # Check if the Python script exists
    if [ ! -f "/search.py" ]; then
        echo "Error: Python script '/search.py' not found."
        return
    fi
    conda deactivate
    # Call the Python script with the search term
    python3 /search.py "$search_term"
    local exit_status=$?
    _activate_env  "$ENV_NAME"
    if [ $exit_status? -ne 0 ]; then
        echo "Error: Python script execution failed."
    fi

    source "/temp.txt"

}

# @yaml
# signature: search_file <search_term>
# docstring: Returns the content of the file of the search term. Search without the extension, if you want test.py search for test
# arguments:
#   query:
#     type: string
#     description: the term to search for, it can be a function name, a path or a node_id
#     required: true

search_file() {
    if [ -z "$1" ]; then
        echo "Usage: search_function <search_term>"
        return
    fi
    local search_term="$1"

    # Check if the Python script exists
    if [ ! -f "/search.py" ]; then
        echo "Error: Python script '/search.py' not found."
        return
    fi

    conda deactivate
    python3 /search.py "$search_term"
    local exit_status=$?
    _activate_env  "$ENV_NAME"

    if [ $exit_status? -ne 0 ]; then
        echo "Error: Python script execution failed."
    fi
    source "/temp.txt"


}