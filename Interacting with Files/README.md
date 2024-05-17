# Visitors 

## Project Objective Overview: 

This project takes in a visitor’s credentials, as well as the name of the person assisting the visitor, then stores that information in a json file. Each visitor has a separate json file, which can be accessed upon request. 

## Project Description Outline: 
 
- ### This is how this project receives visitor data. 

    - The Visitor class. 

    - Explanation of each attribute and its purpose. 

- ### How this project records visitor data. 

    - The save method. How it works. 

- ### How visitor data is retrieved.  

    - The load method. How it works.  

## Project Description: 

 ### This is how this project receives visitor data: 

- The “Visitor” class takes 7 arguments. 

- Out of the 7 arguments, 6 are attributes, and 1 is a self instance which is the first argument. 

- The “full_name” attribute stores the visitor’s full name, as a string. 

- The “age” attribute stores the visitor’s age, as an integer. 

- The “visitor_date” attribute stores the date the visitor visited, as a string. 

- The “visit_time” attribute stores the time the visitor visited, as a string. 

- The “comments” attribute stores any comments regarding the visitor, as a string. 

- The “visitor_assistant” attribute stores the name of the person who assisted the visitor, as a string. 

- The “json_visitor_info” instance variable stores all the attributes and attribute values of the “Visitor” class as a dictionary. 

- In this dictionary, the attribute names are the keys, and the values of each attribute are the values in the dictionary respectively. 

 ### How this project records visitor data:  

- The “save” method accesses the “__file_generator” method through the “Visitor” class. 

- The “__file_generator” method accepts 4 arguments. 

- “__file_generator” method arguments: “full_name”, “mode”, “file_operation”, “description”. 

- It then creates a file and performs file operations according to the values of its arguments. 

- The function of the “save” method is to save individual visitor data in separate files respectively.  

- These files are then named “visitor_the visitor’s name_the visitor’s surname.json” each. 

- After which the “save” method then appends the name of each file in a text file named “visitor_record”. 

- The “save” method achieves all of this by passing the file name as the first argument to the “__file_generator” method, the mode “w” to write, as the second; a string “write”, as the third; and finally, the dictionary in the “json_visitor_info” instance variable, as the forth, which it accesses through the self instance. 

### How visitor data is retrieved: 

- The load method takes 1 argument named “full_name”. 

- It expects a recorded visitor’s name as a string, so, it checks if the input is a string. 

- If the input is a string and the visitor’s file name is recorded in the “visitor_record.txt” file: 

    - The string inside “full_name” is converted into a file name and stored in the “file_name” variable. 

    - It then attempts to open the requested visitor’s json file using the value of the “search_visitor” variable. 

    - If the file exists, then it returns the visitor’s data.  

- If the input is not a string, then it will print a message to the terminal that requests that one enters a visitor’s full name. 

- If the input is a visitor’s name as a string, but the file for that visitor does not exist, then it prints a message that lets one know that that visitor is not recorded. 

- The “search_visitor” variable stores the index number of the location of a visitor’s file name in the visitor_record.txt file. 

- Regardless of the value of the “search_visitor” variable, the load method will return the visitor’s data only if the value of the “search_visitor” variable is not –1. 

- In the “search_visitor” variable, to find the index number of the file name in the “visitor_record.txt” file, the load method uses the “__file_generator” method through the “Visitor” class. 

- After inputting the following arguments to the “__file_generator” method: 

    - file_name; “r”; “read”, None  

- The “__file_generator” method opens the “visitor_record.txt” file and reads it. 

- The find method locates the file name in the “visitor_record.txt” file and returns an index number. 

- This index number is then stored in the “search_visitor” variable. 

- This index number is compared to –1 in the if statement to decide if the visitor’s file exists or not. 

- If the index is equal to –1, then that means that the file does not exist. 

- If the index is not equal to –1, then that means that the file exists. 

 

 

 

 

 

 

 

 