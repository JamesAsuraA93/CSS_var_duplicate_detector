import re


def find_duplicate_css_variables(css_file_path):
    # Regular expression to match CSS variables (e.g., --var-name: value;)
    regex = r'(--[^:]+):\s*[^;]+;'
    variables = {}

    with open(css_file_path, 'r') as file:
        content = file.read()

    # Find all matches
    matches = re.findall(regex, content)

    # Check each variable
    for var in matches:
        if var in variables:
            variables[var] += 1
        else:
            variables[var] = 1

    # Identify duplicates
    duplicates = {var: count for var, count in variables.items() if count > 1}

    return duplicates


# Example usage

file_path = 'globals.css'
duplicates_summary = find_duplicate_css_variables(file_path)
if len(duplicates_summary) == 0:
    print("No duplicates found")
else:
    print("Duplicate CSS Variables:")
for each_var, each_count in duplicates_summary.items():
    print(f"{each_var}: {each_count} times")
