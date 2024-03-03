
# initialize TargetTokens dictionary from a list of target tokens from "ManualTokenList" in a text file: dictionary with ticker, balance ,address, description, URL to coingecko, flag is interesting or not


# update TargetTokens dictionary from Moralis Money strategy webhook (verify that it exists): the strategy finds low-cap tokens which satisfy certain conditions (price, net volume, net buyers, buy pressure)


# receive webhook for buy and sell signals as JSON from Trading View based on price and indicators (to be set up in trading view)

# receive webhook for buy and sell signals from Moralis Money strategies (based on on-chain data)

# define risk management (allocation of tokens): have a pool of USDC or other tokens, or many pools to pair trade against the selected token

# define logic for executing the trade define an array of conditions at which a trade is interesting (i.e. if Token in the interesting token list, net buy pressure from Moralis > min value, and no negative indication from Trading view, prepare the trade) 

# prepare trade instructions as a JSON in the bancor fastlane bot

# simulate trade on Tenderly (needs an account) and return gas fees, OPTIONAL

# execute trade on carbon by setting a one off strategy (see carbon smart contract repo)

# call fastlane to perform arb with best DEX

# update a list TargetTokenTrades to log all trades

# update TargetTokens with new balance
