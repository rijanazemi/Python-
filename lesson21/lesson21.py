def get_fullname(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

print(get_fullname(first_name="john", last_name="doe"))
