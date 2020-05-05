print("hello world")

# load config

# dict keyed on site name
sitesConfig = {}
# dict keyed on bidder name
bidderAdjustments = {}

# load input (generator? - probably overkill without proven need)

auctionResults = []
for auction in auctionList:
    #verify site

    # make a class that contains these fields with unit name, then make a dict
    # highestAdjustedBid determines auction winner
    highestAdjustedBid = 0
    highestBid = None
    # consider refactor in case json field name changes
    for bid in auction["bids"]:
        # can only win auction if valid bidder for site, for a valid unit, bidder is in biddersList
        # and adjusted value >= bid floor
        if sitesConfig.get(bid.bidder):

    # add to list of auction results if auction was valid


print(auctionResults)