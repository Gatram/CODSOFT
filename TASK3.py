import tkinter as tk
import random

# Main window
r = tk.Tk()
r.title("Password Generator")
r.geometry("500x300")
r.config(bg="black")

# Function to delay messages
def update():                                   
    t1.config(text="")
    complexmsg.config(text="")

# Function to generate a weak password (uppercase and lowercase letters)
def weakpassword(l):
    p = ""
    for i in range(l):
        ran = random.randrange(1, 3)
        if ran == 1:  # Random uppercase
            p += chr(random.randrange(65, 91))
        else:  # Random lowercase
            p += chr(random.randrange(97, 123))
    return p

# Function to generate a moderate password (uppercase, lowercase letters, and numbers)
def moderatepassword(l):
    p = ""
    for i in range(l):
        ran = random.randrange(1, 4)
        if ran == 1:  # Random uppercase
            p += chr(random.randrange(65, 91))
        elif ran == 2:  # Random lowercase
            p += chr(random.randrange(97, 123))
        else:  # Random number
            p += chr(random.randrange(48, 58))
    return p

# Function to generate a strong password (letters, numbers, and special characters)
def strongpassword(l):
    p = ""
    for i in range(l):
        p += chr(random.choice(range(33, 127)))  # ASCII characters from 33 to 126
    return p

# Main function to generate and display the password
def click():
    if length.get() == "":  # If no length is provided
        t1.config(text="# Empty bar")
        r.after(2000, update)
        return
    
    if length.get().isdigit():  # Check if the input length is a digit
        l = int(length.get())
        if l >= 5 and l <= 50:  # Check if the length is in the valid range
            if complexity.get() != "None":  # Ensure a complexity level is selected
                if complexity.get() == "weak":
                    password = weakpassword(l)
                elif complexity.get() == "moderate":
                    password = moderatepassword(l)
                else:
                    password = strongpassword(l)
                
                # Display the password in a new window
                rr = tk.Toplevel(r)
                rr.geometry("500x100")
                rr.config(bg="black")
                label = tk.Label(rr, text=password, bg="black", fg="orange", font=("Cascadia Code ExtraLight", 15, "bold", "italic"))
                label.pack(pady=20)
            else:  # If no complexity is selected
                complexmsg.config(text="# Specify the complexity of the password")
                r.after(2000, update)
        else:  # If the length is out of range
            t1.config(text="# Length should be between 5 and 50")
            r.after(2000, update)
    else:  # If the length is not a digit
        t1.config(text="# Length should be digits only")
        r.after(2000, update)

# Heading
heading = tk.Label(text="Password\nGenerator", bg="black", fg="orange", font=("Cascadia Code ExtraLight", 15, "bold", "italic"), padx=10)
heading.pack(anchor="nw", padx=10, pady=10)

# Frame for length input
f1 = tk.Frame(r, bg="black")
length = tk.StringVar()  # Tkinter string variable

t = tk.Label(f1, text="Password Length", fg="orange", bg="black", font=("Cascadia Code ExtraLight", 12, "bold"))
t.grid(row=0, column=0, padx=5)

lengthentry = tk.Entry(f1, textvariable=length, bg="orange", fg="black", font=("Cascadia Code ExtraLight", 10, "bold"), justify="center")
lengthentry.grid(row=0, column=1, padx=5)

t1 = tk.Label(f1, text="", font=("Ariel", 7), bg="black", fg="orange")  # Label for error messages related to length
t1.grid(row=1, column=1)

f1.pack(pady=20)

# Frame for complexity selection
f2 = tk.Frame(r, bg="black")
complexity = tk.StringVar()  # Tkinter string variable
complexity.set(None)

radio1 = tk.Radiobutton(f2, text="Weak", fg="orange", bg="black", font=("Cascadia Code ExtraLight", 10, "bold"), variable=complexity, value="weak")
radio1.grid(row=0, column=1)

radio2 = tk.Radiobutton(f2, text="Moderate", fg="orange", bg="black", font=("Cascadia Code ExtraLight", 10, "bold"), variable=complexity, value="moderate")
radio2.grid(row=0, column=2)

radio3 = tk.Radiobutton(f2, text="Strong", fg="orange", bg="black", font=("Cascadia Code ExtraLight", 10, "bold"), variable=complexity, value="strong")
radio3.grid(row=0, column=3)

f2.pack()

complexmsg = tk.Label(r, text="", font=("Ariel", 7), bg="black", fg="orange")  # Label for error messages related to complexity
complexmsg.pack()

# Frame for buttons
f3 = tk.Frame(r, bg="black")

b = tk.Button(f3, text="Generate", bg="orange", fg="black", font=("Cascadia Code ExtraLight", 9, "bold"), command=click)
b.grid(row=0, column=0, padx=5)

b1 = tk.Button(f3, text="Quit", bg="orange", fg="black", font=("Cascadia Code ExtraLight", 9, "bold"), command=r.quit)
b1.grid(row=0, column=1, padx=5)

f3.pack(pady=10)

r.mainloop()
