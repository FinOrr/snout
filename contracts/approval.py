from pyteal import *

def approval_program():
    # Define constants
    rfid_code = Bytes("rfid")
    vet_details = Bytes("vet")
    
    # Create a scratch variable to store the lookup result
    vet_info = ScratchVar(TealType.bytes)

    # On creation, initialize the contract
    on_creation = Seq([
        App.globalPut(rfid_code, Int(0)),
        App.globalPut(vet_details, Bytes("")),
        Return(Int(1))
    ])

    # Register an animal (only authorised authorities can call this)
    register_animal = Seq([
        Assert(Txn.sender() == Global.creator_address()),  # Only creator (multisig) can register vets
        App.globalPut(Txn.application_args[0], Txn.application_args[1]),  # Map RFID to vet details
        Return(Int(1))
    ])

    # Lookup vet details for a given RFID code
    lookup_animal = Seq([
        vet_info.store(App.globalGet(Txn.application_args[1])),  # Store the result in scratch var
        Return(Int(1))
    ])

    # Main router
    program = Cond(
        [Txn.application_id() == Int(0), on_creation],
        [Txn.on_completion() == OnComplete.NoOp, Cond(
            [Txn.application_args[0] == Bytes("register"), register_animal],
            [Txn.application_args[0] == Bytes("lookup"), lookup_animal]
        )]
    )

    return program

if __name__ == "__main__":
    with open("contracts/approval.teal", "w") as f:
        compiled = compileTeal(approval_program(), mode=Mode.Application, version=5)
        f.write(compiled)
        