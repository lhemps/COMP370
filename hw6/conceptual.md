Q1: What is refactoring? Give three examples of refactoring techniques.
    - refactoring is rewriting parts of your code so that it has the same functionality, but is easier to understand and use
    - examples of refactoring techniques:
        - renaming variables
        - putting sections of a larger function into smaller helper functions
        - changing the contract of a function

Q2: In a data science project, why does code naturally go through "phases" of messiness?
    - when you have an idea, you want to get it working as fast as possible without taking the time to make sure all your code is legible. Later, you can come back to it to tidy it up when you aren't focused on implementing something new. As you add more functionality to your project, you go back and forth from developing new tools to cleaning up the code.

Q3: What are three techniques for creating more modular code?
    - break long functions down into smaller helper functions
    - if you are writing the same thing over and over, make it into a function to reduce redundancy
    - organize your modules so that things that work together and do similar things are grouped together