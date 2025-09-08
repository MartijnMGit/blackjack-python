from art import logo
import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" * 30)

def adjust_for_ace(hand):
    while sum(hand) > 21 and 11 in hand:
        hand[hand.index(11)] = 1
    return hand

def compare_scores(player_score, pc_score):
    if player_score > 21:
        return "You went over. You lose 😭"
    elif pc_score > 21:
        return "Opponent went over. You win 😁"
    elif player_score > pc_score:
        return "You win! 🎉"
    elif player_score < pc_score:
        return "You lose 😞"
    else:
        return "It's a draw 😐"

def game():
    clear_screen()
    print(logo)

    player_cards = random.choices(cards, k=2)
    pc_cards = random.choices(cards, k=2)

    game_over = False

    while not game_over:
        player_cards = adjust_for_ace(player_cards)
        player_score = sum(player_cards)

        print(f"\nYour cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {pc_cards[0]}")

        if player_score > 21:
            game_over = True
            break

        draw = input("Type 'y' to get another card, 'n' to pass: ")
        if draw == "y":
            player_cards.append(random.choice(cards))
        else:
            game_over = True

    while sum(pc_cards) < 17:
        pc_cards.append(random.choice(cards))
        pc_cards = adjust_for_ace(pc_cards)

    player_score = sum(player_cards)
    pc_score = sum(pc_cards)

    print(f"\nYour final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {pc_cards}, final score: {pc_score}")
    print(compare_scores(player_score, pc_score))

# Main game loop
while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ") == "y":
    game()
