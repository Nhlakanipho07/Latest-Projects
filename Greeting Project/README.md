# Person  

 ## Project Objective Overview: 

- This project collects the user's credentials, including their interests. 

- It then generates a greetings statement in the first person. 

- This is achieved using a Person class. 


## Project Description Outline: 

- How it validates the type of each attribute. 

- How the interests statement method works. 

- How the hello method works. 

 
## Project Description: 

### How it validates the type of each attribute: 

- When an instance is created, the Person class takes 4 arguments. 

- The interests argument is optional, whilst the other 3 are mandatory. 

- This is to account for a user who has no interests. 

- It then automatically calls the init method and creates attributes using the values of the arguments it received. 

- The init method then calls the “__attribute_checker” method through the self-instance. 

- The “__attribute_checker” method checks each attribute to ensure that its values are of the correct type. 

- If not, the “__attribute_checker” method raises a type error message. 

 
### How the interests statement method works: 

- The “__interests_statement” method takes one argument, which is the self-instance. 

- It checks the value of the self.interest attribute. 

- It compares the value to an integer or the string “none”. 

- If the value is “none”, this means the user has no interest, so it assign “none” to “count_interests”. 

- If the value is not “none”, but a list of interests as a list of strings: 

    - It calculates the length of the string. 

    - It then compares the length of the string to an integer. 

    - It generates a custom statement depending on the numeric value of the integer, using the value of self.interests attribute. 

    - If the integer is 1, this means that the user has one interest. 

    - So, a customized statement is created. 

    - This statement is in the first person.  

    - It communicates the user’s interest. 

    - If the numeric value of the integer is greater than or equal to 2. 

    - This means that the user has two or more interests. 

    - So, a customized statement is created. 

    - This statement is in the first person and in the plural form. 

    - It communicates all the user’s interests. 

- It then returns the interests variable. 

 
### How the hello method works: 

- The hello method takes one argument, which is the self-instance. 

- The hello method calls the “__interests_statement” method through the self-instance. 

- It then stores the call in its own interests variable. 

- A customized statement is created in the hello variable, using self.name, self.age, self.gender and interests variables. 

- The values of the above variables create a greetings statement in the first person. 

- The hello method then returns the hello variable. 

 

 

 