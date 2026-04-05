# python-mini-database
Mini SQL python



Sure! Here are the English versions for both projects, written in a clean, human-like style suitable for GitHub.

---

### **Simple SQL-Like Table Manager**

This project is a file-based table management system written in Python that mimics basic SQL commands (CREATE, INSERT, SELECT, UPDATE, DELETE, JOIN, COUNT). It processes commands from an input file and displays the results in a formatted, easy-to-read table structure.

#### **Features**
* **Dynamic Table Creation:** Define new tables with custom column names.
* **Data Operations:** Full support for inserting, updating, and deleting rows.
* **Conditional Queries:** Filter and count data based on specific criteria.
* **Table Joining:** Perform joins between two tables using a common column.
* **Visual Output:** Automatically calculates column widths and prints data using ASCII-style borders.

#### **Usage**
Run the program from the command line by providing an input file as an argument:
```bash
python main.py input.txt
```

#### **Data Structure**
The project uses a dictionary (`data`) as its core, where table names serve as keys. Columns and elements are stored as nested lists and dictionaries. The `table_printer` function ensures the output is always aligned and professional.

#### **Supported Commands**
* `CREATE_TABLE [Table_Name] [Col1,Col2,...]`
* `INSERT [Table_Name] [Val1,Val2,...]`
* `SELECT [Table_Name] [Columns/*] WHERE {Conditions}`
* `UPDATE [Table_Name] {New_Values} WHERE {Conditions}`
* `DELETE [Table_Name] WHERE {Conditions}`
* `JOIN [Table1,Table2] WHERE [Common_Column]`
* `COUNT [Table_Name] WHERE {Conditions}`

---

