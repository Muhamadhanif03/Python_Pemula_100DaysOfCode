from art import logo
print(logo)
bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid = bidding_record[bidder]
        if bid > highest_bid:
            highest_bid = bid
            winner = bidder
    print(f"Pemenang bid adalah {winner} dengan total bid {highest_bid}")


while not bidding_finished:
    name = input("Masukkan nama anda:\n")
    total_bid = int(input("Masukkan jumlah bid anda:"))
    bids[name] = total_bid
    should_continue = input(
        'Apakah anda ingin melanjutkan bid? Jika iya ketik "ya", jika tidak ketik "tidak".\n').lower()
    if should_continue == "ya":
        continue
    elif should_continue == "tidak":
        bidding_finished = True
        find_highest_bidder(bids)
