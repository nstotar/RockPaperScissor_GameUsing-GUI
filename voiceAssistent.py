import streamlit as st
import random

st.set_page_config(page_title="Rock Paper Scissors", page_icon="✂️", layout="centered")

st.title("🪨 📄 ✂️ Rock Paper Scissors - Best of Three")

if 'player_score' not in st.session_state:
    st.session_state.player_score = 0
    st.session_state.computer_score = 0
    st.session_state.rounds_played = 0
    st.session_state.result = ""
    st.session_state.last_player_choice = ""
    st.session_state.last_computer_choice = ""
    st.session_state.show_winner = False

def play(choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    st.session_state.last_player_choice = choice
    st.session_state.last_computer_choice = computer_choice

    # Decide result
    if choice == computer_choice:
        result = "It's a tie! 🤝"
    elif (
        (choice == "Rock" and computer_choice == "Scissors") or
        (choice == "Paper" and computer_choice == "Rock") or
        (choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You win this round! 🎉"
        st.session_state.player_score += 1
    else:
        result = "Computer wins this round! 🤖"
        st.session_state.computer_score += 1

    st.session_state.result = result
    st.session_state.rounds_played += 1

    if st.session_state.rounds_played >= 3:
        st.session_state.show_winner = True

def reset_game():
    st.session_state.player_score = 0
    st.session_state.computer_score = 0
    st.session_state.rounds_played = 0
    st.session_state.result = ""
    st.session_state.last_player_choice = ""
    st.session_state.last_computer_choice = ""
    st.session_state.show_winner = False

# Scores and round info
st.subheader(f"Player Score: {st.session_state.player_score}    |    Computer Score: {st.session_state.computer_score}")
st.write(f"Rounds Played: {st.session_state.rounds_played} / 3")

# Choices display
if st.session_state.last_player_choice:
    st.write(f"**Your choice:** {st.session_state.last_player_choice}")
    st.write(f"**Computer's choice:** {st.session_state.last_computer_choice}")
    st.info(st.session_state.result)

# Game buttons
if not st.session_state.show_winner:
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🪨 Rock"):
            play("Rock")
    with col2:
        if st.button("📄 Paper"):
            play("Paper")
    with col3:
        if st.button("✂️ Scissors"):
            play("Scissors")
else:
    # Show final winner
    if st.session_state.player_score > st.session_state.computer_score:
        st.success("🎉 You win the game! Congratulations!")
    elif st.session_state.player_score < st.session_state.computer_score:
        st.error("🤖 Computer wins the game. Better luck next time!")
    else:
        st.info("It's a tie game! 🤝")

if st.button("🔄 Reset Game"):
    reset_game()
