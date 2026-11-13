def generate_fide_team_diagram(
team_a_name="TEAM A",
team_b_name="TEAM B",
    team_a_board1_color="White",
aisle_side="left",  # 'left' (near Board 1) or 'right' (near Board 4)
output_file="fide_team_setup.png",
):
@@ -83,11 +82,8 @@ def generate_fide_team_diagram(
board_num = i + 1
center_x = table_x + (i + 0.5) * board_spacing

    # Determine alternating colors
    if team_a_board1_color == "White":
      team_a_color = "White" if board_num % 2 == 1 else "Black"
    else:
      team_a_color = "Black" if board_num % 2 == 1 else "White"
    # Home team (Team A) plays White on odd-numbered boards.
    team_a_color = "White" if board_num % 2 == 1 else "Black"
team_b_color = "Black" if team_a_color == "White" else "White"

# Table divider lines
@@ -166,10 +162,10 @@ def generate_fide_team_diagram(
)
ax.add_patch(board_border)

    # Draw Clock (Always screen facing the Arbiter Aisle)
    # Place every clock on the aisle-facing side of its board.
clock_width = 0.22
clock_height = 0.55
    if aisle_side == "right":
    if aisle_side == "left":
clock_x = bx - clock_width - 0.12
else:
clock_x = bx + board_size + 0.12
@@ -195,6 +191,14 @@ def generate_fide_team_diagram(
fontweight="bold",
color="white",
)
    arrow_start_x = clock_x + clock_width if aisle_side == "right" else clock_x
    arrow_end_x = arrow_start_x + (0.18 if aisle_side == "right" else -0.18)
    ax.annotate(
        "",
        xy=(arrow_end_x, 2.8),
        xytext=(arrow_start_x, 2.8),
        arrowprops={"arrowstyle": "->", "color": "#2ecc71", "linewidth": 1.5},
    )

plt.tight_layout()
if output_file:
@@ -203,16 +207,23 @@ def generate_fide_team_diagram(


st.title("CHESS 4-Board Team Match Setup")
st.markdown(
    """
**Setup rules**
- The chessboard's bottom-right square is light.
- The home team plays White on odd-numbered boards.
- Teams face each other, with opposite colors on each board.
- All clocks are on the same side of the tables, with their screens facing the arbiter aisle.
"""
)

team_a_name = st.text_input("Team A", "Home Club (Team A)")
team_b_name = st.text_input("Team B", "Visiting Club (Team B)")
team_a_board1_color = st.selectbox("Team A's color on Board 1", ["White", "Black"])
team_a_name = st.text_input("Home team (Team A)", "Home Club (Team A)")
team_b_name = st.text_input("Visiting team (Team B)", "Visiting Club (Team B)")
aisle_side = st.selectbox("Arbiter aisle side", ["left", "right"])

fig = generate_fide_team_diagram(
team_a_name=team_a_name,
team_b_name=team_b_name,
    team_a_board1_color=team_a_board1_color,
aisle_side=aisle_side,
)
st.pyplot(fig)
