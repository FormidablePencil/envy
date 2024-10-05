#!/bin/bash

# Function to search files for abstract concepts
search_files_for_concepts() {
  local directory=$1
  local concept=$2
  
  echo "Searching for '$concept' in $directory..."
  
  # Use search_files tool to find relevant files
  local results=$(antml_function_calls
<antml_invoke name="search_files">
<antml_parameter name="path">$directory</antml_parameter>
<antml_parameter name="regex">$concept</antml_parameter>
</antml_invoke>
</antml_function_calls)
  
  if [ -z "$results" ]; then
    echo "No results found for '$concept' in $directory."
  else
    echo "$results"
  fi
}

# Example usage
search_files_for_concepts "/Downloads" "abstract concepts and ideas"