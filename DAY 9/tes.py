from art import logo
print(logo)

bids = {}
should_end = False


def find_highest_bid(high_bid):
    highest_bid = 0
    winner = ""
    for bidder in high_bid:
        bid = high_bid[bidder]
        if bid > highest_bid:
            highest_bid = bid
            winner = bidder
    print(
        f"Pemenang bid adalah {winner}, dengan total bid sebanyak ${highest_bid}")


while not should_end:
    nama = input("Masukkan nama anda:\n")
    total_bid = int(input("Masukkan jumlah bid anda:\n$"))
    bids[nama] = total_bid
    should_continue = input(
        'Apakah anda ingin melanjutkan bid?\nUntuk melanjutkan ketik "ya", untuk berhenti ketik "tidak"\n')
    if should_continue == "ya":
        continue
    elif should_continue == "tidak":
        should_end = True
        find_highest_bid(bids)
