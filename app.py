import matplotlib.patches as patches
import matplotlib.pyplot as plt
import streamlit as st


st.set_page_config(
    page_title="Chess Team Match Setup",
    page_icon="♟️",
    layout="wide",
)


st.markdown(
    """
    <style>
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 1rem;
    }

    div[data-testid="stSidebar"] {
        background: #f8fafc;
        border-right: 1px solid #e2e8f0;
    }

    .stApp {
        background: linear-gradient(180deg, #f8fafc 0%, #eef4ff 100%);
    }

    .css-1d391kg {
        padding: 0.75rem 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def generate_fide_team_diagram(
    team_a_name="TEAM A",
    team_b_name="TEAM B",
    aisle_side="left",
):
    fig, ax = plt.subplots(figsize=(14, 7), dpi=140)
    fig.patch.set_facecolor("#f8fafc")
    ax.set_facecolor("#f8fafc")
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6)
    ax.set_aspect("equal")
    ax.axis("off")

    # Title and subtitle
    ax.text(
        6,
        5.75,
        "CHESS 4-BOARD TEAM MATCH SETUP",
        ha="center",
        va="center",
        fontsize=16,
        fontweight="bold",
        color="#0f172a",
    )
    ax.text(
        6,
        5.22,
        f"Aisle on the {aisle_side.capitalize()} side",
        ha="center",
        va="center",
        fontsize=10,
        color="#475569",
    )

    # Team names
    ax.text(
        6,
        0.52,
        team_a_name.upper(),
        ha="center",
        va="center",
        fontsize=13,
        fontweight="bold",
        color="#1d4ed8",
    )
    ax.text(
        6,
        5.02,
        team_b_name.upper(),
        ha="center",
        va="center",
        fontsize=13,
        fontweight="bold",
        color="#b45309",
    )

    # Arbiter aisle block
    aisle_x = 0.4 if aisle_side == "left" else 11.0
    aisle_rect = patches.Rectangle(
        (aisle_x, 1.0),
        0.6,
        3.6,
        facecolor="#dfe7ee",
        edgecolor="#64748b",
        linewidth=1.2,
    )
    ax.add_patch(aisle_rect)
    ax.text(
        aisle_x + 0.3,
        2.8,
        "ARBITER\nAISLE",
        ha="center",
        va="center",
        rotation=90,
        fontsize=8,
        fontweight="bold",
        color="#334155",
    )

    # Main table rectangle
    table_x = 1.25 if aisle_side == "left" else 1.1
    table_width = 9.6
    table_rect = patches.Rectangle(
        (table_x, 1.35),
        table_width,
        2.9,
        facecolor="#ffffff",
        edgecolor="#334155",
        linewidth=2,
    )
    ax.add_patch(table_rect)

    # Divider lines between boards
    board_spacing = table_width / 4
    for i in range(1, 4):
        div_x = table_x + i * board_spacing
        ax.plot(
            [div_x, div_x],
            [1.35, 4.25],
            color="#cbd5e1",
            linestyle="--",
            linewidth=1,
        )

    for i in range(4):
        board_num = i + 1
        center_x = table_x + (i + 0.5) * board_spacing

        team_a_color = "White" if board_num % 2 == 1 else "Black"
        team_b_color = "Black" if team_a_color == "White" else "White"

        ax.text(
            center_x,
            4.45,
            f"BOARD {board_num}",
            ha="center",
            va="center",
            fontsize=9,
            fontweight="bold",
            color="#0f172a",
        )

        # Seats for players
        ax.add_patch(
            patches.Circle((center_x, 4.72), 0.2, facecolor="#475569", edgecolor="#0f172a")
        )
        ax.add_patch(
            patches.Circle((center_x, 0.88), 0.2, facecolor="#475569", edgecolor="#0f172a")
        )

        # Color labels
        ax.text(
            center_x,
            3.96,
            team_b_color,
            ha="center",
            va="center",
            fontsize=8.5,
            fontweight="bold",
            color="#0f172a",
        )
        ax.text(
            center_x,
            1.54,
            team_a_color,
            ha="center",
            va="center",
            fontsize=8.5,
            fontweight="bold",
            color="#0f172a",
        )

        # Draw mini chessboard
        board_size = 1.4
        bx = center_x - board_size / 2
        by = 2.85 - board_size / 2
        sq_size = board_size / 8

        for row in range(8):
            for col in range(8):
                is_light = (row + col) % 2 == 1
                sq_color = "#f0d9b5" if is_light else "#b58863"
                ax.add_patch(
                    patches.Rectangle(
                        (bx + col * sq_size, by + row * sq_size),
                        sq_size,
                        sq_size,
                        facecolor=sq_color,
                        edgecolor="none",
                    )
                )

        ax.add_patch(
            patches.Rectangle(
                (bx, by),
                board_size,
                board_size,
                facecolor="none",
                edgecolor="#0f172a",
                linewidth=1.0,
            )
        )

        # Clock placement
        clock_width = 0.24
        clock_height = 0.58
        if aisle_side == "left":
            clock_x = bx - clock_width - 0.12
        else:
            clock_x = bx + board_size + 0.12
        clock_y = 2.85 - clock_height / 2

        clock_rect = patches.Rectangle(
            (clock_x, clock_y),
            clock_width,
            clock_height,
            facecolor="#22c55e",
            edgecolor="#166534",
            linewidth=1,
        )
        ax.add_patch(clock_rect)

        ax.text(
            clock_x + clock_width / 2,
            2.85,
            "CLOCK",
            ha="center",
            va="center",
            rotation=90,
            fontsize=6.2,
            fontweight="bold",
            color="white",
        )

        arrow_start_x = clock_x + clock_width if aisle_side == "right" else clock_x
        arrow_end_x = arrow_start_x + (0.18 if aisle_side == "right" else -0.18)
        ax.annotate(
            "",
            xy=(arrow_end_x, 2.85),
            xytext=(arrow_start_x, 2.85),
            arrowprops={"arrowstyle": "->", "color": "#22c55e", "linewidth": 1.5},
        )

    return fig


# App header
st.title("Chess Team Tournament Setup")
st.caption("A clean, readable board layout for tournament planning.")

with st.sidebar:
    st.header("Match settings")
    team_a_name = st.text_input("Home team (Team A)", "Home Club (Team A)")
    team_b_name = st.text_input("Visiting team (Team B)", "Visiting Club (Team B)")
    aisle_side = st.selectbox("Arbiter aisle side", ["left", "right"])

    st.markdown("### Setup rules")
    st.markdown(
        """
        - The bottom-right square is light.
        - The home team plays White on odd-numbered boards.
        - Teams face each other with opposite colors.
        - Clocks stay on the arbiter side.
        """
    )

left_col, right_col = st.columns([3.2, 1])

with left_col:
    fig = generate_fide_team_diagram(
        team_a_name=team_a_name,
        team_b_name=team_b_name,
        aisle_side=aisle_side,
    )
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)

with right_col:
    st.markdown("### Match summary")
    st.markdown(f"**Team A:** {team_a_name}")
    st.markdown(f"**Team B:** {team_b_name}")
    st.markdown(f"**Aisle side:** {aisle_side.capitalize()}")
    st.info("This layout is optimized for clean screen display and easy presentation.")
