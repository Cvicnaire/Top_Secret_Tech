# Top_Secret_Tech_Project: Jigsaw


![image](https://github.com/user-attachments/assets/bf426e1c-0ecd-4dce-937f-e3871836a2de)

Extremely Rough outline of what we could possibly do with a workflow manager

How it works:

This is python program that is designed to assemble workflows based on the given task files. An inputs json file is generated based on the workflow given. 

** How to use:
1. clone repo
2. run this command "python3 main.py", be sure to be in the jigsaw directory 
3. you can change what tasks you want to be used in the workflow inside the variables.txt


In theory we can feed this program several tasks listed in sequential order in  variables.txt to automatically compose the workflow wdl for us. 

This is still rough around the edges! 

Known Issues:

1. adding additional flags dynamically is not working yet
2. submitting the assembled workflows is not working yet, wil create the workflow wdls though


