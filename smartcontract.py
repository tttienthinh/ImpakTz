import smartpy as sp
import time

# https://smartpy.io/explorer?address=KT1GoCja6hoW5dEJuXWhVD94o1kKhrDvKQ69
# https://better-call.dev/ghostnet/KT1GoCja6hoW5dEJuXWhVD94o1kKhrDvKQ69/operations

@sp.module
def main():
    class StoreCarData(sp.Contract):
        def __init__(self, address): 
            # Initialisation de l'achat du véhicule
            self.data.address = address
            self.data.verified_addresses = {address}
            self.data.cars = sp.cast(
                sp.big_map(), sp.big_map[sp.address, sp.string]
            )

            
        @sp.entrypoint 
        def add_verified(self, address):
            # Créer une voiture
            if sp.sender == self.data.address:
                self.data.verified_addresses.add(address)

        
        @sp.entrypoint 
        def create_car(self, new_owner):
            # Créer une voiture
            if self.data.verified_addresses.contains(sp.sender):
                self.data.cars[new_owner] = "New car"


        @sp.entrypoint # Note the indentation
        def add_data(self, params):
            # Ajout d'information
            if self.data.verified_addresses.contains(sp.sender):
                self.data.cars[params.address] += " - " + params.text
            
        
        @sp.entrypoint 
        def change_owner(self, new_owner):
            # Changement de propriétaire
            self.data.cars[new_owner] = self.data.cars[sp.sender] + " - Transfert"
            del self.data.cars[sp.sender]

        
        @sp.offchain_view()
        def get_data(self, address):
            # Retourne les data
            return self.data.cars[address]

# Automated tests that run on simulation
@sp.add_test()
def test():
    # Initialize the test scenario
    scenario = sp.test_scenario("Test scenario", main)
    scenario.h1("StoreCarData")
    my_address = sp.address("tz1PS1Xq4pmYqzNX5nyyB9ryFGoabWK6vdXQ")
    
    # Initialize the contract and pass the starting value
    contract = main.StoreCarData(
        my_address
    )
    scenario += contract

    # On a 1 garagiste et 2 utilisateurs
    garagiste = sp.test_account(0).address
    alice = sp.test_account(1).address
    bob = sp.test_account(2).address
    
    contract.create_car(alice, _sender=my_address)
    contract.add_verified(garagiste, _sender=my_address)
    
    # RDV chez le garagiste
    contract.add_data(address=alice, text="Changement de pneu", _sender=garagiste)

    # Vente d'Alice à Bob
    contract.change_owner(bob, _sender=alice)
    
    

