import matplotlib.patches as patches
import matplotlib.pyplot as plt
import streamlit as st


def generate_fide_team_diagram(
    team_a_name="TEAM A",
    team_b_name="TEAM B",
    team_a_board1_color="White",
    aisle_side="left",
    output_file=None,
):
    """Create a diagram of a four-board team match setup."""
    if team_a_board1_color not in {"White", "Black"}:
        raise ValueError("team_a_board1_color must be 'White' or 'Black'.")
    if aisle_side not in {"left", "right"}:
        raise ValueError("aisle_side must be 'left' or 'right'.")

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6)
    ax.axis("off")

    ax.text(
        6,
        5.6,
        f"CHESS 4-Board Team Match Setup (Aisle on {aisle_side.capitalize()})",
        ha="center",
        va="center",
        fontsize=14,
        fontweight="bold",
    )
    ax.text(
        6, 5.1, team_b_name, ha="center", va="center", fontsize=12,
        fontweight="bold", color="#2c3e50"
    )
    ax.text(
        6, 0.5, team_a_name, ha="center", va="center", fontsize=12,
        fontweight="bold", color="#2c3e50"
    )

    aisle_x = 0.4 if aisle_side == "left" else 11.0
    ax.add_patch(
        patches.Rectangle(
            (aisle_x, 1.0), 0.6, 3.6,
            facecolor="#d5dbdb", edgecolor="#7f8c8d"
        )
    )
    ax.text(
        aisle_x + 0.3, 2.8, "ARBITER AISLE", ha="center", va="center",
        rotation=90, fontsize=10, fontweight="bold", color="#2c3e50"
    )

    table_x = 1.3 if aisle_side == "left" else 1.1
    table_width = 9.6
    ax.add_patch(
        patches.Rectangle(
            (table_x, 1.4), table_width, 2.8,
            facecolor="#f8f9f9", edgecolor="#34495e", linewidth=2
        )
    )

    board_spacing = table_width / 4
    for i in range(4):
        board_num = i + 1
        center_x = table_x + (i + 0.5) * board_spacing
        team_a_color = (
            team_a_board1_color
            if board_num % 2 == 1
            else ("Black" if team_a_board1_color == "White" else "White")
        )
        team_b_color = "Black" if team_a_color == "White" else "White"

        if i > 0:
            div_x = table_x + i * board_spacing
            ax.plot([div_x, div_x], [1.4, 4.2], color="#bdc3c7", linestyle="--")

        ax.text(
            center_x, 4.45, f"Board {board_num}", ha="center", va="center",
            fontsize=10, fontweight="bold"
        )

        ax.add_patch(
            patches.Circle(
                (center_x, 4.75), 0.2, facecolor="#5d6d7e", edgecolor="black"
            )
        )
        ax.add_patch(
            patches.Circle(
                (center_x, 0.85), 0.2, facecolor="#5d6d7e", edgecolor="black"
            )
        )

        ax.text(
            center_x, 3.95, team_b_color, ha="center", va="center",
            fontsize=9, fontweight="bold"
        )
        ax.text(
            center_x, 1.65, team_a_color, ha="center", va="center",
            fontsize=9, fontweight="bold"
        )

        board_size = 1.4
        bx = center_x - board_size / 2
        by = 2.8 - board_size / 2
        sq_size = board_size / 8
        for row in range(8):
            for col in range(8):
                is_light = (row + col) % 2 == 1
                sq_color = "#f0d9b5" if is_light else "#b58863"
                ax.add_patch(
                    patches.Rectangle(
                        (bx + col * sq_size, by + row * sq_size),
                        sq_size, sq_size, facecolor=sq_color, edgecolor="none"
                    )
                )
        ax.add_patch(
            patches.Rectangle(
                (bx, by), board_size, board_size, facecolor="none",
                edgecolor="black", linewidth=1
            )
        )

        clock_width = 0.22
        clock_height = 0.55
        if aisle_side == "left":
            clock_x = bx - clock_width - 0.12
        else:
            clock_x = bx + board_size + 0.12
        clock_y = 2.8 - clock_height / 2
        ax.add_patch(
            patches.Rectangle(
                (clock_x, clock_y), clock_width, clock_height,
                facecolor="#2ecc71", edgecolor="black", linewidth=1
            )
        )
        ax.text(
            clock_x + clock_width / 2, 2.8, "CLOCK", ha="center", va="center",
            rotation=90, fontsize=6, fontweight="bold", color="white"
        )

        arrow_start_x = clock_x + clock_width if aisle_side == "right" else clock_x
        arrow_end_x = arrow_start_x + (0.18 if aisle_side == "right" else -0.18)
        ax.annotate(
            "", xy=(arrow_end_x, 2.8), xytext=(arrow_start_x, 2.8),
            arrowprops={"arrowstyle": "->", "color": "#2ecc71", "linewidth": 1.5}
        )

    plt.tight_layout()
    if output_file:
        fig.savefig(output_file, dpi=300)
    return fig


st.title("CHESS 4-Board Team Match Setup")
st.markdown(
    """
**Setup rules**
- The chessboard's bottom-right square is light.
- Team A's Board 1 color is selected below; colors alternate on subsequent boards.
- Teams face each other, with opposite colors on each board.
- All clocks are on the same side of the tables, facing the arbiter aisle.
"""
)

# These controls define the values passed to generate_fide_team_diagram below.
team_a_name = st.text_input("Team A name", value="TEAM A")
team_b_name = st.text_input("Team B name", value="TEAM B")
team_a_board1_color = st.selectbox(
    "Team A's color on Board 1", options=("White", "Black")
)
aisle_side = st.selectbox("Arbiter aisle side", options=("left", "right"))

fig = generate_fide_team_diagram(
    team_a_name=team_a_name,
    team_b_name=team_b_name,
    team_a_board1_color=team_a_board1_color,
    aisle_side=aisle_side,
)

st.pyplot(fig)
plt.close(fig)
