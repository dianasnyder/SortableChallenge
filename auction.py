import json
import sys

class UnitAuction:
    highestAdjustedBid = 0
    highestBid = None

# load config
with open("config.json") as config:
    configData = json.load(config)

# read in input
auctionList = json.load(sys.stdin)

# dict keyed on site name
sitesConfig = {site["name"]:site for site in configData["sites"]}
# dict keyed on bidder name
bidderAdjustments = {bidder["name"]:bidder for bidder in configData["bidders"]}


# run auction
auctionResults = []
for auction in auctionList:
    auctionResult = []
    siteData = sitesConfig.get(auction["site"])
    # only hold auction if valid site
    if not siteData:
        auctionResults.append(auctionResult)
        continue

    unitAuctions = {unit: UnitAuction() for unit in auction["units"]}

    for bid in auction["bids"]:
        print("\n", bid, "\n")
        unitAuction = unitAuctions.get(bid["unit"])
        bidderAdjustment = bidderAdjustments[bid["bidder"]]

        adjustedBid = bid["bid"] 
        # can only win auction if valid bidder for site, for a valid unit, bidder is in biddersList
        # and adjusted value >= bid floor
        # linear search through bidders - could make constant by transforming bidders lists to dict
        if bid["bidder"] in siteData["bidders"] and unitAuction and bidderAdjustment:
            adjustedBid = bid["bid"] * (1 + bidderAdjustment["adjustment"])
            if (adjustedBid > siteData["floor"] and adjustedBid > unitAuction.highestAdjustedBid):
                unitAuction.highestAdjustedBid = adjustedBid
                unitAuction.highestBid = bid
                print("\nbid winner found")
                print(unitAuction.highestAdjustedBid)
                print(unitAuction.highestBid)

    # verify output proper if auction invalid or no one wins
    auctionResults.append([unitAuction.highestBid for unitName, unitAuction in unitAuctions.items()])

print(auctionResults)

with open("output.json", 'w') as output:
    json.dump(auctionResults, output, indent=4, sort_keys=True)




