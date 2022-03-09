from datetime import datetime ,timedelta
import db_operations as do
import requests
import json
import time

main_url ="https://api.pancakeswap.info/api/v2/tokens/"

contract_package = {}
contract_details = list()

def clear_token_list():
    """
    Truncate token list table
    """
    do.truncate()


def creating_contract_package(insert_list : list):
    """
    Adds new contract address to contract_package
   
    """

    contract_details = insert_list
    do.insert(contract_details)


def input_token_contracts() -> list():
    """
    Accept contract addresses as user input
    """

    contract_name = input("Enter token name : ")
    contract_address = input("Enter contract token : ")

    contract_details=(contract_name,contract_address)
  

    return contract_details
    

def calculate_coin_value(coin_quantity : float, coin_price : float) -> float: 
    """
    Calculates the coin accual price based on price * quantity
    """

    total_value = coin_quantity * coin_price

    return total_value


def list_contract_address():
    """
    List contract addreses
    """

    print("")

    data = do.select()

    for row in data:
        print(f"Coin : {row[0]} - Address : {row[1]}")


def get_token_details():
    """
    Getting token details from pancakeswap
    """
    track_start_date = datetime.now()
    track_stop_date = track_start_date + timedelta(days=1)

    print("")
    print(f"Tracking your alt coins from {track_start_date} to {track_stop_date} ")

    target_key = ["address"]
    data = do.select()

    while track_start_date < track_stop_date:

        for row in data:

            request = requests.get(main_url + row[1])
            response = request.json()

            if request.status_code == 200:
                name = response['data']['name']
                symbol = response['data']['symbol']
                coin_price = float(response['data']['price'])
                coin_price_bnb = float(response['data']['price_BNB'])
                
                print("")
                print(f"Coin: \x1b[6;30;42m {name} \x1b[0m Symbol: {symbol} \nPrice $: \x1b[6;30;42m {round(coin_price,6)} \x1b[0m Price BNB: {round(coin_price_bnb,7)}")
                time.sleep(1)
            else:
                print(f"Bad Request on {row[0]} {row[1]}")
        time.sleep(3)

       
def main_menu():
    print("-------------------------------------")
    print("-----Pancakeswap Alt Coin Tracker----")
    print("-------------------------------------")
    print("|  [1] Add new token                |")
    print("|  [2] List tokens                  |")
    print("|  [3] Delete token list            |")
    print("|  [4] Start pancakeswap tracking   |")
    print("|  [5] Init Database for Pancake    |")
    print("|  [0] Exit                         |")
    print("-------------------------------------")


def main():

    main_menu()
    option = int(input("Choose your action : "))

    while option !=0 :
        if option == 1:
            creating_contract_package(input_token_contracts())
        elif option == 2:
            list_contract_address()
        elif option == 3:
            clear_token_list()
        elif option == 4:
            get_token_details()
        elif option == 5:
            do.db_init()
        elif option == 0:
            exit()
        else:
            print("invalid option")
        
        print("")
        main_menu()
        option = int(input("Choose your action : "))

    print("See you soon , Goodbye !")


if __name__ == '__main__':
    main()
