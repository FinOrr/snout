# clear.py
from pyteal import *

def clear_state_program():
    return Return(Int(1))

# Compile the contract
if __name__ == "__main__":
    
    with open("clear.teal", "w") as f:
        compiled = compileTeal(clear_state_program(), mode=Mode.Application, version=5)
        f.write(compiled)
        