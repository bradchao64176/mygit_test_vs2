def format_name(f_name,l_name):
    #this is Docstring format with three double quote
    """
    Take a fist and last name and format it to return the title case version of the name
    """
    if f_name=="" or l_name=="":
        return "You don't provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

firstname = input("what is your first name?")
lastname = input("what is your last name?")
formated_string = format_name(firstname,lastname)
print(formated_string) #formated_string variable with return result by invoked format_name