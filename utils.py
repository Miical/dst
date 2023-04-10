def print_table(table):
    """
    This function takes a 2D list of strings and prints it as a table with aligned columns.
    """
    # Find the maximum length of string in each column
    col_widths = [max(len(str(row[i])) for row in table) for i in range(len(table[0]))]

    # Print the table with aligned columns
    for row in table:
        # Join each element in the row as a string, left-justified with the maximum width of the corresponding column
        # Separate each element with two spaces
        print("  ".join(str(row[i]).ljust(col_widths[i]) for i in range(len(row))))
