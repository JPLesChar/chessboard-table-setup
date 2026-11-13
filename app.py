import random

import streamlit as st

import matplotlib.patches as patches
import matplotlib.pyplot as plt


def generate_fide_team_diagram(
    team_a_name="TEAM A",
    team_b_name="TEAM B",
    team_a_board1_color="White",
    aisle_side="left",  # 'left' (near Board 1) or 'right' (near Board 4)
    output_file="fide_team_setup.png",
):
  fig, ax = plt.subplots(figsize=(12, 6))
  ax.set_xlim(0, 12)
  ax.set_ylim(0, 6)
  ax.axis("off")

  # Title and Team Labels
  ax.text(
      6,
      5.6,
      f"FIDE 4-Board Team Match Setup (Aisle on {aisle_side.capitalize()})",
      ha="center",
      va="center",
      fontsize=14,
      fontweight="bold",
  )
  ax.text(
      6,
      5.1,
      team_b_name,
      ha="center",
      va="center",
      fontsize=12,
      fontweight="bold",
      color="#2c3e50",
  )
  ax.text(
      6,
      0.5,
      team_a_name,
      ha="center",
      va="center",
      fontsize=12,
      fontweight="bold",
      color="#2c3e50",
  )

  # Draw Arbiter Aisle
  aisle_x = 0.4 if aisle_side == "left" else 11.0
  aisle_rect = patches.Rectangle(
      (aisle_x, 1.0), 0.6, 3.6, facecolor="#d5dbdb", edgecolor="#7f8c8d"
  )
  ax.add_patch(aisle_rect)
  ax.text(
      aisle_x + 0.3,
      2.8,
      "ARBITER AISLE",
      ha="center",
      va="center",
      rotation=90,
      fontsize=10,
      fontweight="bold",
      color="#2c3e50",
  )

  # Draw Table
  table_x = 1.3 if aisle_side == "left" else 1.1
  table_width = 9.6
  table_rect = patches.Rectangle(
      (table_x, 1.4),
      table_width,
      2.8,
      facecolor="#f8f9f9",
      edgecolor="#34495e",
      linewidth=2,
  )
  ax.add_patch(table_rect)

  # Configure each of the 4 boards
  board_spacing = table_width / 4
  for i in range(4):
    board_num = i + 1
    center_x = table_x + (i + 0.5) * board_spacing

    # Determine alternating colors
    if team_a_board1_color == "White":
      team_a_color = "White" if board_num % 2 == 1 else "Black"
    else:
      team_a_color = "Black" if board_num % 2 == 1 else "White"
    team_b_color = "Black" if team_a_color == "White" else "White"

    # Table divider lines
    if i > 0:
      div_x = table_x + i * board_spacing
      ax.plot([div_x, div_x], [1.4, 4.2], color="#bdc3c7", linestyle="--")

    # Board Label
    ax.text(
        center_x,
        4.45,
        f"Board {board_num}",
        ha="center",
        va="center",
        fontsize=10,
        fontweight="bold",
    )

    # Draw Player Seats (Top = Team B, Bottom = Team A)
    seat_b = patches.Circle(
        (center_x, 4.75), 0.2, facecolor="#5d6d7e", edgecolor="black"
    )
    seat_a = patches.Circle(
        (center_x, 0.85), 0.2, facecolor="#5d6d7e", edgecolor="black"
    )
    ax.add_patch(seat_b)
    ax.add_patch(seat_a)

    # Color Labels on Table
    ax.text(
        center_x,
        3.95,
        team_b_color,
        ha="center",
        va="center",
        fontsize=9,
        fontweight="bold",
    )
    ax.text(
        center_x,
        1.65,
        team_a_color,
        ha="center",
        va="center",
        fontsize=9,
        fontweight="bold",
    )

    # Draw Chessboard (8x8 mini grid)
    board_size = 1.4
    bx = center_x - board_size / 2
    by = 2.8 - board_size / 2
    sq_size = board_size / 8

    for row in range(8):
      for col in range(8):
        # Bottom-right square (row=0, col=7) must always be light
        is_light = (row + col) % 2 == 1
        sq_color = "#f0d9b5" if is_light else "#b58863"
        sq = patches.Rectangle(
            (bx + col * sq_size, by + row * sq_size),
            sq_size,
            sq_size,
            facecolor=sq_color,
            edgecolor="none",
        )
        ax.add_patch(sq)

    board_border = patches.Rectangle(
        (bx, by),
        board_size,
        board_size,
        facecolor="none",
        edgecolor="black",
        linewidth=1,
    )
    ax.add_patch(board_border)

    # Draw Clock (Always on the side facing the Arbiter Aisle)
    clock_width = 0.22
    clock_height = 0.55
    if aisle_side == "left":
      clock_x = bx - clock_width - 0.12
    else:
      clock_x = bx + board_size + 0.12
    clock_y = 2.8 - clock_height / 2

    clock_rect = patches.Rectangle(
        (clock_x, clock_y),
        clock_width,
        clock_height,
        facecolor="#2ecc71",
        edgecolor="black",
        linewidth=1,
    )
    ax.add_patch(clock_rect)
    ax.text(
        clock_x + clock_width / 2,
        2.8,
        "CLOCK",
        ha="center",
        va="center",
        rotation=90,
        fontsize=6,
        fontweight="bold",
        color="white",
    )

  plt.tight_layout()
  plt.savefig(output_file, dpi=300)
  print(f"Diagram saved successfully to {output_file}")


# Example Usage:
generate_fide_team_diagram(
    team_a_name="Home Club (Team A)",
    team_b_name="Visiting Club (Team B)",
    team_a_board1_color="White",
    aisle_side="left",
)
