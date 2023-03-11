# 30-Days-of-Python
30 Days of Python Study
Lesson 1: Printing Text

In this lesson, you'll learn how to print text to the console using the print() function.

    Open Visual Studio Code and create a new file by clicking "File" > "New File".
    Save the file as helloworld.py in a directory of your choice.
    In the file, add the following code:

python

print("Hello, world!")

    Save the file.
    Open a terminal or command prompt and navigate to the directory where helloworld.py is located.
    Run the following command to execute the script:

bash

python helloworld.py

You should see the text "Hello, world!" printed to the console.

    Next, initialize a Git repository in the directory where your helloworld.py file is located. You can do this by opening the terminal in VS Code and running the following command:

bash

git init

This will create a new Git repository in the current directory.

    Add helloworld.py to the Git repository by running the following command in the terminal:

bash

git add helloworld.py

This will stage your file for commit.

    Commit your changes to Git by running the following command in the terminal:

bash

git commit -m "Add 'Hello, world!' message"

This will commit your changes to Git with a commit message explaining what changes you made.

    Finally, push your changes to a remote Git repository. If you don't have a remote repository set up yet, you can create a new repository on a hosting platform like GitHub or GitLab, and then follow their instructions for pushing your changes. Here's an example command for pushing your changes to a remote repository:

bash

git push origin master

This will push your changes to a remote repository on the master branch.
The error "bash: !': event not found" occurs because the exclamation mark (!) is a special character in bash and is used for history expansion. If you use an exclamation mark in a command without escaping it properly, bash will try to interpret it as a history expansion command and may produce errors like the one you saw.

To fix this error, you can either escape the exclamation mark with a backslash (\!) or use single quotes (') around the string containing the exclamation mark.

For example, instead of writing:

bash

git commit -m "Add 'Hello, world!' message"

You can write:

bash

git commit -m 'Add '\''Hello, world!'\'' message'

The backslashes and single quotes tell bash to treat the exclamation mark as a literal character rather than a special character.

Alternatively, you can use double quotes (") and escape the exclamation mark with a backslash:

bash

git commit -m "Add \!Hello, world\! message"

This will also prevent bash from interpreting the exclamation mark as a history expansion command.
    Open VS Code and navigate to your Python30D folder.
    In the Explorer panel on the left-hand side, click on the Python30D folder to open it.
    Right-click on the Python30D folder and select "New File" from the context menu.
    In the "Name your file" dialog box, type hello.py and press Enter to create a new Python file named hello.py in the Python30D folder.
    In the hello.py file, type the following code:

python

print("Hello, world!")

    Save the hello.py file by pressing Ctrl+S (Windows/Linux) or Cmd+S (macOS).
    Open the VS Code terminal by clicking on "Terminal" in the top menu and selecting "New Terminal".
    In the terminal, navigate to your Python30D folder by running the command cd Python30D.
    Stage the changes to the hello.py file by running the command git add hello.py.
    Commit the changes to Git by running the command git commit -m "Add hello.py file with 'Hello, world!' message".
    Push the changes to GitHub by running the command git push origin main.
    
    In lesson 3, we'll learn how to add user input to our Python program and use it to manipulate strings.

    Open the hello.py file that we created in lesson 2 in VS Code.
    Modify the code to prompt the user for their name and print a personalized message that includes their name. Replace the print statement in hello.py with the following code:

python

name = input("What is your name? ")
print("Hello, " + name + "!")

This code will prompt the user to enter their name and store the input in the variable name. It will then print a personalized message that includes the user's name.

    Save the hello.py file by pressing Ctrl+S (Windows/Linux) or Cmd+S (macOS).
    Open the VS Code terminal by clicking on "Terminal" in the top menu and selecting "New Terminal".
    In the terminal, navigate to your Python30D folder by running the command cd Python30D.
    Stage the changes to the hello.py file by running the command git add hello.py.
    Commit the changes to Git by running the command git commit -m "Add user input to hello.py".
    Push the changes to GitHub by running the command git push origin main.
