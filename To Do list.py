to_do_list=[]

while True:
    to_do_list_append=input("Write down your works for today (type 'quit' to stop):")

    to_do_list.append(to_do_list_append)
    print("\nYour To-Do List:")
    for i, iş in enumerate(to_do_list, 1):
        print(f"{i}. {iş}")


