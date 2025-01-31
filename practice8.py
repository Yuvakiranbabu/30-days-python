template="""Hi there {name},
welcome to your first day in {store}."""

def format_msg(my_name,my_store):

    my_msg=template.format(name=my_name,store=my_store)
    return my_msg


print(format_msg("Jonah","Cloud 9"))