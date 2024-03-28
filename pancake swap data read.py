def find_liquidity_pool():
    from web3 import Web3
    # Connect to the BSC mainnet using a RPC endpoint
    w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed1.binance.org/'))
    # Address of the PancakeSwap Factory contract
    pancakeswap_factory_address = '0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73'
    # ABI of the PancakeSwap Factory contract
    pancakeswap_factory_abi = [  
        {
            "constant": True,
            "inputs": [  
                { 
                    "name": "token0",
                    "type": "address"
                },
                { 
                    "name": "token1",
                    "type": "address"
                }
            ],
            "name": "getPair",
            "outputs": [  
                { 
                    "name": "",
                    "type": "address"
                }
            ],
            "payable": False,
            "stateMutability": "view",
            "type": "function"
        }
    ]

    # Address of the token bnb
    tokenA_address = '0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c' # bnb
    # Address of the token B
    tokenB_address = '0xcA2095FBaad0ad51E52CDEac1E0228796B949a1e' # SITH token
    # Create a Contract object for the PancakeSwap Factory
    pancakeswap_factory_contract = w3.eth.contract(address=pancakeswap_factory_address, abi=pancakeswap_factory_abi)
    # Get the liquidity pool address for the token pair
    liquidity_pool_address = pancakeswap_factory_contract.functions.getPair(tokenA_address, tokenB_address).call()
    print(f'The liquidity pool address for the token pair is {liquidity_pool_address}')

find_liquidity_pool()
