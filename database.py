from sys import argv


# Prints the table. This function is also used in other functions
def table_printer(keys,data,table_name):
   # Creating a max length dictionary for width of each column
    max_length = {}
    for key in keys:
        max_length[key] = len(key)
    for key in keys:
        for sample in data[table_name, " elements"]:
            if len(sample[key]) > max_length[key]:
                max_length[key] = len(sample[key])

    # Creating the table line by line
    print("+", end="")
    for column in data[table_name, " columns"]:
        print("-"*(max_length[column]+2),"\b+", end="")
    print("")

    print("|", end="")
    for column in data[table_name, " columns"]:
        print(" {:<{}} |".format(column, max_length[column]), end="")
    print("")

    print("+", end="")
    for column in data[table_name, " columns"]:
        print("-" * (max_length[column]+2), "\b+", end="")
    print("")

    for sample in data[table_name, " elements"]:
        print("|", end="")
        for column in data[table_name, " columns"]:
            print(" {:<{}} |".format(sample[column],max_length[column]), end="")
        print("")

    print("+", end="")
    for column in data[table_name, " columns"]:
        print("-" * (max_length[column]+2), "\b+", end="")
    print("")

# Creates the table and columns
def create_table(data,table_name,columns):
    print("###################### CREATE #########################")
    # Define the table's columns
    data[table_name," columns"]=columns
    print("Table '{}' created with columns: {}".format(table_name, columns))
    print("#######################################################\n")


# Inserts the wanted element and prints the table
def insert(table_name,data,column_elements,columns):
    print("###################### INSERT #########################")
    # Initialize the elements list if not already present
    if (table_name, " elements") not in data:
        data[table_name, " elements"] = []
    # Add a new row by mapping column names to values
    data[table_name," elements"].append(dict(zip(columns, column_elements)))
    print("Inserted into '{}': {}\n".format(table_name, tuple(column_elements)))
    print("Table: {}".format(table_name))
    # Print the updated table
    table_printer(data[table_name," columns"],data,table_name)
    print("#######################################################\n")

# Selects the wanted columns based on conditions
def select(table_name,wanted_columns,conditions,data):
    conditions_str=str(conditions).strip("['']")
    # Use all columns if '*' is specified
    if wanted_columns == ["*"]:
        wanted_columns=data[table_name," columns"]
    selected_values = []
    conditions_dictionary = {}
    # Parse conditions into a dictionary
    for x in conditions_str.strip("{}").split(", "):
        conditions_dictionary[(x.split(": ")[0]).strip(' " ')] = (x.split(": ")[1]).strip( ' " ' )
    try:
        for sample in data[table_name, " elements"]:
            sample_data=[]
            matching_for_all_keys = True
            for key, value in conditions_dictionary.items():
                if key not in sample or sample[key] != value:
                    matching_for_all_keys = False
                    break

            if matching_for_all_keys:
                for wanted_column in wanted_columns:
                    sample_data.append(sample[wanted_column])
                selected_values.append(tuple(sample_data))

        # Raise KeyError if no rows match
        if len(selected_values) == 0:
            raise KeyError("")

    except KeyError:
        # Exception handling for missing table
        if (table_name, " columns") not in data:
            print("###################### SELECT #########################")
            print("Table {} not found".format(table_name))
            print("Condition: {}".format(conditions_str.replace('"',"'")))
            print("Select result from '{}': None".format(table_name))
            print("#######################################################\n")
            return

        # Exception handling for missing columns
        for wanted_column in wanted_columns:
            if wanted_column not in data[table_name, " columns"]:
                print("###################### SELECT #########################")
                print("Column {} does not exist".format(wanted_column))
                print("Condition: {}".format(conditions_str.replace('"',"'")))
                print("Select result from '{}': None".format(table_name))
                print("#######################################################\n")
                return

        # Handle mismatched condition keys
        mismatch_columns = []
        for key in conditions_dictionary:
            if key not in data[table_name, " columns"]:
                mismatch_columns.append(key)
        if mismatch_columns:
            print("###################### SELECT #########################")
            print("Column {} does not exist".format(", ".join(mismatch_columns)))
            print("Condition: {}".format(conditions_str.replace('"',"'")))
            print("Select result from '{}': None".format(table_name))
            print("#######################################################\n")
            return

    print("###################### SELECT #########################")
    print("Condition: {}".format(conditions_str.replace('"',"'")))
    print("Select result from '{}': {}".format(table_name,selected_values))
    print("#######################################################\n")

# Function to update rows in a table based on given conditions
def update(data,conditions,table_name,updates):
    # Creates the conditions and updates dictionary from string type input
    conditions_str = str(conditions).strip("['']")
    conditions_dictionary = {}
    for x in conditions_str.strip("{}").split(", "):
        conditions_dictionary[(x.split(": ")[0]).strip(' " ')] = (x.split(": ")[1]).strip(' " ')
    updates_str = str(updates).strip("['']")
    updates_dictionary = {}
    for x in updates_str.strip("{}").split(", "):
        updates_dictionary[(x.split(": ")[0]).strip(' " ')] = (x.split(": ")[1]).strip(' " ')


    updated_rows=0 # Counter for updated rows
    try:
        # Iterate through each element in the specified table
        for sample in data[table_name, " elements"]:
            matching_for_all_keys = True

            # Check if all conditions are satisfied
            for key, value in conditions_dictionary.items():
                if key not in sample or sample[key] != value:
                    matching_for_all_keys = False
                    break
            # Apply updates if conditions are satisfied
            if matching_for_all_keys:
                for update_key in updates_dictionary:
                    sample[update_key]= updates_dictionary[update_key]
                    updated_rows+=1

        # Check if all update keys exist in the table columns
        for key in updates_dictionary:
            if key not in data[table_name, " columns"]:
                raise KeyError

        # Check if all condition keys exist in the table columns
        for key in conditions_dictionary:
            if key not in data[table_name, " columns"]:
                raise KeyError


    except KeyError:
        # Handle cases where table or columns do not exist
        if (table_name, " columns") not in data:
            print("###################### UPDATE #########################")
            print("Updated '{}' with {} where {}".format(table_name, updates_str.replace('"',"'"), conditions_str.replace('"',"'")))
            print("Table {} not found".format(table_name))
            print("0 rows updated.")
            print("#######################################################\n")
            return


        mismatch_columns = []

        # Identify update keys not in table columns
        for key in updates_dictionary:
            if key not in data[table_name, " columns"]:
                mismatch_columns.append(key)

        if mismatch_columns:
            print("###################### UPDATE #########################")
            print("Updated '{}' with {} where {}".format(table_name, updates_str.replace('"',"'"), conditions_str.replace('"',"'")))
            print("Column {} does not exist".format(", ".join(mismatch_columns)))
            print("0 rows updated.\n")
            print("Table: {}".format(table_name))
            table_printer(data[table_name, " columns"], data, table_name)
            print("#######################################################\n")
            return

        mismatch_columns = []

        # Identify condition keys not in table columns
        for key in conditions_dictionary:
            if key not in data[table_name, " columns"]:
                mismatch_columns.append(key)

        if mismatch_columns:
            print("###################### UPDATE #########################")
            print("Updated '{}' with {} where {}".format(table_name, updates_str.replace('"',"'"), conditions_str.replace('"',"'")))
            print("Column {} does not exist".format(", ".join(mismatch_columns)))
            print("0 rows updated.\n")
            print("Table: {}".format(table_name))
            table_printer(data[table_name, " columns"], data, table_name)
            print("#######################################################\n")
            return

    # Print the result of the update operation
    print("###################### UPDATE #########################")
    print("Updated '{}' with {} where {}".format(table_name,updates_str.replace('"',"'"),conditions_str.replace('"',"'")))
    print("{} rows updated.\n".format(updated_rows))
    print("Table: {}".format(table_name))
    table_printer(data[table_name, " columns"],data,table_name)
    print("#######################################################\n")

# Function to delete rows based on conditions
def delete(table_name,conditions,data):
    # Creates the conditions dictionary from string type input
    conditions_str = str(conditions).strip("['']")
    conditions_dictionary = {}
    # Create a dictionary from conditions string
    for x in conditions_str.strip("{}").split(", "):
        conditions_dictionary[(x.split(": ")[0]).strip(' " ')] = (x.split(": ")[1]).strip(' " ')

    deleted_rows=0 # Counter for deleted rows

    try:
        # Iterate through each element in the specified table
        for sample in data[table_name, " elements"]:
            matching_for_all_keys = True

            # Check if all conditions are satisfied
            for key, value in conditions_dictionary.items():
                if key not in sample or sample[key] != value:
                    matching_for_all_keys = False
                    break

            # Remove the row if conditions are satisfied
            if matching_for_all_keys:
                data[table_name, " elements"].remove(sample)
                deleted_rows+=1

        # Check if all condition keys exist in the table columns
        for key in conditions_dictionary:
            if key not in data[table_name, " columns"]:
                raise KeyError

    except KeyError:
        # Handle cases where table or columns do not exist
        if (table_name, " columns") not in data:
            print("###################### DELETE #########################")
            print("Deleted from '{}' where {}".format(table_name, conditions_str.replace('"', "'")))
            print("Table {} not found".format(table_name))
            print("0 rows deleted.".format(deleted_rows))
            print("#######################################################\n")
            return

        mismatch_columns = []

        # Identify condition keys not in table columns
        for key in conditions_dictionary:
            if key not in data[table_name, " columns"]:
                mismatch_columns.append(key)

        if mismatch_columns:
            print("###################### DELETE #########################")
            print("Deleted from '{}' where {}".format(table_name, conditions_str.replace('"', "'")))
            print("Column {} does not exist".format(", ".join(mismatch_columns)))
            print("0 rows deleted.\n")
            print("Table: {}".format(table_name))
            table_printer(data[table_name, " columns"], data, table_name)
            print("#######################################################\n")
            return

    # Print the result of the delete operation
    print("###################### DELETE #########################")
    print("Deleted from '{}' where {}".format(table_name,conditions_str.replace('"',"'")))
    print("{} rows deleted.\n".format(deleted_rows))
    print("Table: {}".format(table_name))
    table_printer(data[table_name, " columns"], data, table_name)
    print("#######################################################\n")

# Joins two tables based on a common column and prints the result
def join(table1,table2,common_column,data):

    try:
        keys = data[table1, " columns"] + data[table2, " columns"] # Combine column names from both tables
        joined_tables= data[table1, " elements"] # Fetch elements from the first table
        joined_list=[]

        # Iterate through both tables to find matching rows based on the common column
        for sample in joined_tables:
            for element in data[table2, " elements"]:
                if sample[common_column]==element[common_column]:
                    listing_list=[]

                    for key1 in sample:
                        listing_list.append(sample[key1])
                    for key2 in element:
                        listing_list.append(element[key2])
                    joined_list.append(listing_list)


        # Calculate max column widths for pretty printing
        max_length = []
        for key in keys:
            max_length.append(len(key))

        for row in joined_list:
            for i, value in enumerate(row):
                if len(value) > max_length[i]:
                    max_length[i] = len(value)

        # Print the joined table in a formatted way
        print("####################### JOIN ##########################")
        print("Join tables {} and {}".format(table1,table2))
        print("Join result ({} rows):\n".format(len(joined_list)))
        print("Table: Joined Table")

        # Print column headers with borders
        column_index = 0
        print("+", end="")
        for i in range(len(keys)):
            print("-" * (max_length[column_index] + 2), "\b+", end="")
            column_index += 1
        print("")

        column_index = 0
        print("|", end="")
        for column in keys:
            print(" {:<{}} |".format(column, max_length[column_index]), end="")
            column_index += 1
        print("")

        column_index = 0
        print("+", end="")
        for i in range(len(keys)):
            print("-" * (max_length[column_index] + 2), "\b+", end="")
            column_index+=1
        print("")

        for sample in joined_list:
            print("|", end="")
            word_index=0
            for i in range(len(keys)):
                print(" {:<{}} |".format(sample[word_index], max_length[word_index]), end="")
                word_index+=1
            print("")

        # Print each row of the joined table
        column_index = 0
        print("+", end="")
        for i in range(len(keys)):
            print("-" * (max_length[column_index] + 2), "\b+", end="")
            column_index += 1
        print("")
        print("#######################################################\n")

        # If the common column does not exist, raise an error
        if common_column not in keys:
            raise KeyError

    except KeyError:
        # Handle missing tables or columns
        table_checker = []
        if (table1, " columns") not in data:
            table_checker.append(table1)
        if (table2, " columns") not in data:
            table_checker.append(table2)

        if table_checker:
            print("###################### JOIN ##########################")
            print("Join tables {} and {}".format(table1, table2))
            print("Table {} does not exist".format(", ".join(table_checker)))
            print("#######################################################\n")
            return

        if common_column not in data[table1, " columns"] + data[table2, " columns"]:
            print("###################### JOIN ##########################")
            print("Join tables {} and {}".format(table1, table2))
            print("Column {} does not exist".format(common_column))
            print("#######################################################\n")
            return

# Deletes all rows from a given table
def delete_all_rows(data,table_name):
    try:
        deleted_rows = len(data[table_name, " elements"])
        data[table_name, " elements"] = [] # Clear all elements from the table
        print("###################### DELETE #########################")
        print("Deleted from '{}'".format(table_name))
        print("{} rows deleted.\n".format(deleted_rows))
        print("Table: {}".format(table_name))
        table_printer(data[table_name, " columns"], data, table_name)
        print("#######################################################\n")
    except KeyError:
        # Handle case where the table does not exist
        print("###################### DELETE #########################")
        print("Deleted from '{}'".format(table_name))
        print("Table {} not found".format(table_name))
        print("0 rows deleted.")
        print("#######################################################\n")

def count_all(data,table_name):
    # Counts all rows in a table
    try:
        all_rows = len(data[table_name, " elements"])
        print("###################### COUNT #########################")
        print("Count: {}".format(all_rows))
        print("Total number of entries in '{}' is {}".format(table_name, all_rows))
        print("#######################################################\n")

    except KeyError:
        # Handle case where the table does not exist
        print("###################### COUNT #########################")
        print("Table {} not found".format(table_name))
        print("Total number of entries in '{}' is 0".format(table_name))
        print("#######################################################\n")
        return


def count(conditions,table_name,data):
    # Counts rows in a table that match given conditions
    conditions_str = str(conditions).strip("['']")
    counter = 0
    conditions_dictionary = {}
    for x in conditions_str.strip("{}").split(", "):
        conditions_dictionary[(x.split(": ")[0]).strip(' " ')] = (x.split(": ")[1]).strip(' " ')

    try:
        for sample in data[table_name, " elements"]:
            matching_for_all_keys = True
            for key, value in conditions_dictionary.items():
                if key not in sample or sample[key] != value:
                    matching_for_all_keys = False
                    break
            if matching_for_all_keys:
                counter+=1

            for key in conditions_dictionary:
                if key not in data[table_name, " columns"]:
                    raise KeyError

    except KeyError:
        # Handle missing table or columns
        if (table_name, " columns") not in data:
            print("###################### COUNT #########################")
            print("Table {} not found".format(table_name))
            print("Total number of entries in '{}' is 0".format(table_name))
            print("#######################################################\n")
            return

        mismatch_columns = []
        for key in conditions_dictionary:
            if key not in data[table_name, " columns"]:
                mismatch_columns.append(key)

        if mismatch_columns:
            print("###################### COUNT #########################")
            print("Column {} does not exist".format(", ".join(mismatch_columns)))
            print("Total number of entries in '{}' is 0".format(table_name))
            print("#######################################################\n")
            return

    # Print the count result
    print("###################### COUNT #########################")
    print("Count: {}".format(counter))
    print("Total number of entries in '{}' is {}".format(table_name,counter))
    print("#######################################################\n")


# Main function to process commands from input file
def main():
    data={}
    input_file= argv[1]
    with open(input_file, "r") as inputs:
        for line in inputs:
            # Extract the command keyword (e.g., CREATE_TABLE, INSERT, etc.)
            command=line.split(" ")[0]
            if command in {"CREATE_TABLE","INSERT","SELECT","UPDATE","DELETE","JOIN","COUNT"}:
                table_name=line.split(" ")[1]
                if command == "CREATE_TABLE":
                    # Parse the column definitions and call create_table function
                    create_table(data,table_name,line.split(" ",2)[2].strip("\n").split(","))
                if command == "INSERT":
                    try:
                        # Parse the values to insert and call the insert function
                        insert(table_name, data, line.split(" ", 2)[2].strip("\n").split(","),data[table_name, " columns"])
                    except KeyError:
                        # Handle cases where the table does not exist
                        if (table_name, " columns") not in data:
                            print("###################### INSERT #########################")
                            print("Table {} not found".format(table_name))
                            print("Inserted into '{}': {}".format(table_name,tuple(line.split(" ",2)[2].strip("\n").split(","))))
                            print("#######################################################\n")

                if command == "SELECT":
                    # Parse columns and conditions for the SELECT command
                    select(table_name,line.split(" ",4)[2].strip("\n").split(","),line.split(" ",4)[4].strip("\n"),data)

                if command == "UPDATE":
                    # Parse update values and conditions and call update function
                    update(data,line.split(" WHERE ")[1].strip("\n"),table_name,str(line.split(" WHERE ")[0]).split(" ",2)[2].strip("\n"))

                if command == "DELETE":
                    # Handle DELETE commands, either deleting all rows or based on conditions
                    if len(line.split(" "))==2:
                        delete_all_rows(data,table_name.strip("\n"))
                    else:
                        delete(table_name,line.split(" ",3)[3].strip("\n"),data)

                if command == "JOIN":
                    # Parse table names and the common column for JOIN operation
                    join(line.split(" ",3)[1].split(",")[0],line.split(" ",3)[1].split(",")[1],line.split(" ")[3].strip("\n"),data)

                if command == "COUNT":
                    # Handle COUNT command to get row counts for a table
                    if len(line.split(" "))==2:
                        count_all(data, table_name.strip("\n"))
                    else:
                        count(line.split(" ",3)[3].strip("\n"),table_name,data)


if __name__=="__main__":
    main()

