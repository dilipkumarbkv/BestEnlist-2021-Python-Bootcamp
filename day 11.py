# creating file and writing text into it
with open("30 days 30 hours of Operations.txt","w") as f:
    f.write("I have completed 10 days successfully\n")
    print("process completed")


# opening file and adding text to it    
f = open("30 days 30 hours of Operations.txt","a")
f.write("Dilip Kumar\n")
print("Adding Completed")
f.close()



# opening file and reading content in the file
f = open("30 days 30 hours of Operations.txt","r")
data = f.read()
print(data)
