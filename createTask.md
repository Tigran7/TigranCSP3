{% include navigation.html %}

# Create Task
<div class="row justify-content-center" style="margin: 2%;">
    <iframe height="1000px" width="700px" src="https://replit.com/@Tigran7/GPA-calculator?lite=true#index.html"></iframe>
</div>

# GPA Calculator
![Screenshot (298)](https://user-images.githubusercontent.com/89666148/155926810-3af56a9c-7560-4623-bbd9-227c9557d489.png)
# [Video](https://youtu.be/Tf1e25A46o0)
# [Final code](https://github.com/danaylevy2004/thesuperidolenthusiasts/commit/f3b1593a8e58c224398c1edebbff9bf8f0465100)
## Written Response
### 3a
1. Describes the overall purpose of the program
- The purpose of the program is for a student to determine their cumulative GPA based on how many trimesters a class was taken and how well they performed in the class.
2. Describes what functionality of the program is demonstrated in the video
- The user inputs the name of the course they took, the number of trimesters they took that course, and then the letter grade they received in that course. When the add button is clicked a new table is created that displays the inputted values and after the user has finished inputting their classes they can click calculate GPA, which returns the average GPA count. The clear button then removes the added table so the user can restart.
3. Describes the input and output of the program demonstrated in the video
- The input of the program in the video is when the user inputs the values for the grade they received, the name of the classes they took, and the number of trimesters they took that class. The overall output received is the cumulative GPA based on the inputted values as well as the table that displays the previously inputted values.
### 3b
![Screenshot (300)](https://user-images.githubusercontent.com/89666148/155936001-9f16cb86-1dac-4fa2-a8fc-caef6970865a.png)
![Screenshot (302)](https://user-images.githubusercontent.com/89666148/155933472-3472ceec-62e5-4198-920f-3375e358b58a.png)


1. The first program code segment must show how data have been stored in the list. 
- The data in the first code segment is not actively being stored in the list because it requires user input, but when the user does type in the values the array is mutated and the value is stored there, this is seen in the example of the console. 
2. The second program code segment must show the data in the same list being used, such as creating new data from the existing data or accessing multiple elements in the list, as part of fulfilling the program’s purpose. 
- In the console example, we see that after inputting our values the information is stored in an object literal with the properties being the trimester and grade and the property value being the user input.
3. Identifies the name of the list being used in this response
- The name of the list, which is an array, is gpaArry which in this case is assigned using let so that it can be reassigned in the future using functions.
4. Describes what the data contained in the list represent in your program
- The data contained in the list is a representation of the user input, more specifically the letter grade that the user selects from the drop down menu,
5. Explains how the selected list manages complexity in your program code by explaining why your program code could not be written, or how it would be written differently if you did not use the list 
- Without the array, the program could not be written because we wouldn't have a place to store the user input. The reason we store it in an array is that it can be easily accessed in the future using built-in java script methods as well as simple indexing for example.

### 3c
1. The first program code segment must be a student-developed procedure that:
• Defines the procedure’s name and return type (if necessary)
• Contains and uses one or more parameters that have an effect on the functionality of the procedure
• Implements an algorithm that includes sequencing, selection, and iteration
- ![Screenshot (305)](https://user-images.githubusercontent.com/89666148/155936859-453786a1-06d9-44df-9b8a-cd011de76c11.png)
2. The second program code segment must show where your student-developed procedure is being called in your program.
Then, provide a written response that does both of the following:
- ![Screenshot (306)](https://user-images.githubusercontent.com/89666148/155938326-e822e78b-846b-49bd-8670-ce6f5abb3ae1.png)
3. Describes in general what the identified procedure does and how it contributes to the overall functionality of the program
- This procedure is responsible for doing the actual calculating. It takes whatever we input for the trimesters, and multiplies that by the grade inputted by the user. It then finds the average number after dividing those two and displays the average grade point. This contributes to the functionally because it is what actually takes the user's input and returns the final product that we are looking for, which is the average number.
4. Explains in detailed steps how the algorithm implemented in the identified procedure works. Your explanation must be detailed enough for someone else to recreate it.
- We start off by taking our object, which is calc GPA. By using document. query selector, we were able to store the element from HTML into our javascript file as a variable. Then using the dot operator we call the addEventListener method which basically tells our program to listen for an event, which in this case is to click on the button from the user, to trigger the function. In other words that is how our function Is invoked. We then create the actual function using an arrow function expression, rather than the traditional function declaration. We don't have any parameters and therefore the parentheses are left empty. Then we declare our trimesters variable using the let keyword in the block scope, set it to 0, and reassign the other variables that we will be using to 0 as well. The next part of the function uses a built-in javascript method called forEach, which combines iteration into the procedure. Basically, the trimester variable is reassigned to whatever the user inputs into the trimester section of the calculator and then that is multiplied by the grade point in order to get the sum. Then we reassign our overall sum to that product we just got. The forEach method itself is going to go back into the array and input the user's input as an argument of the loop.

### 3d
1. Describes two calls to the procedure identified in written response 3c. Each call must pass a different argument(s) that causes a different segment of code in the algorithm to execute.
 -One call might be if we input 2 into the trimester category and A into the grade category. This is going to cause the section of the algorithm to execute which does the calculating of the GPA because it was given 2 valid inputs and is now going to calculate the overall GPA. On the other hand, if any invalid inputs are given, such as a negative number in the trimester category or nothing at all, then another segment of the code is going to activate which causes the window to display a prompt saying that the user's input was invalid and they must try again.
2. Describes what condition(s) is being tested by each call to the procedure
- In the first example given the condition being tested is whether the user actually inputted a value, and when the computer sees the inputted value it takes it through the function and in the end outputs the grade point average. In our second case, we are testing rather the other function evaluates to truthy and falsy, and since nothing was inputted into the array it will evaluate to falsy which will execute the function and display the error message.
3. Identifies the result of each call
- The second call is going to display a message that prompts the user to try again. On the other hand, the first scenario is going to input values into the array, which is going to then run through the function and output the GPA and an object literally contained inside the array the creates key pair values, which the inputs being the property values.



# Design Ideas and Usage
Tigran has decided on making a GPA calculator. This fits into the theme of our website because our website is about education and college board. The basic idea behind it is the user will input their letter grade, which will then be converted into the corresponding number, summed up, and averaged out depending on whether it's an ap class or not to calculate the grade point average. I will also create an appealing UI to go along with the calculator

User input: Class type (AP vs regular) and letter grade
Program functionality: Take user input, convert to appropriate grade point, sum it up and find the average
Output: The average of the grade points of each class inputted
List: User input will be stored in an array for easy access from the program
Program code segment: Function that takes in grade letter and converts to grade point, function that takes in all the points and finds average
Sequencing: The program will run in order from top to bottom
Iteration: Program will include a for loop that's linked with the array
Selection: Program will have if and else-if statements that convert from letter grade to grade point
Purpose: Calculating GPA for students
Parameter/Argument: Parameter will be letter grade and whether a class is normal/AP; Argument will be the user input into these parameters Drawing sketchpad
![img gpa](https://user-images.githubusercontent.com/89666148/155934504-ed27fd53-df0a-496f-b911-0da69c95cadb.jpeg)
