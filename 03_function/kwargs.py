
def print_kwargs(** kwargs):
    # print("Name ",name,"Power ",power)
    for key ,value in kwargs.items():
        print(f'{key}: {value}')

print_kwargs(name="Sparsh",power="bob")
print_kwargs(name="Sparsh",power="bob",enemy="Dr Strange")
print_kwargs(name="Sparsh")