def convert_table_string_to_markdown(table_string):
    # Split the input string into rows and remove leading/trailing white spaces
    rows = [row.strip() for row in table_string.split('\n')]

    # Initialize variables to store Markdown and determine the depth
    markdown = []
    depth = 0
    markdown.append("# Head\n")
    for row in rows:
        # Skip empty rows
        if not row:
            continue
        col = 0
        # Split the row into cells
        cells = [cell.strip() for cell in row.split('|')]

        # Determine the depth based on the number of cells
        depth = row.count('|') - 1

        # Create Markdown headers or cell content based on depth
        for col in range(depth):
            # if col == 0 and row == 0:
            #     # Header row
            #     markdown.append(f"# {cells[col]}\n")
            if col == 0 :
                # Header row
                markdown.append(f"## {cells[col+1]}\n")
            else:
                # Cell row
                indentation = "\t" * (col-1)
                markdown.append(f"{indentation}- {cells[col+1]}\n")


    return "".join(markdown)

# Input file path and output file path
# input_file_path = input("请输入包含表格的Markdown文件的完整路径: ")
# output_file_path = input("请输入要保存Markdown内容的文件的完整路径: ")

input_file_path = "input_table.md"
output_file_path = "output_table.md"

with open(input_file_path, 'r', encoding='utf-8') as input_file:
    table_string = input_file.read()

# Convert the table string to Markdown
markdown_content = convert_table_string_to_markdown(table_string)

# Print the Markdown content to the terminal
print(markdown_content)

# Save the Markdown content to the output file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(markdown_content)

print(f"Markdown内容已保存到文件: {output_file_path}")
