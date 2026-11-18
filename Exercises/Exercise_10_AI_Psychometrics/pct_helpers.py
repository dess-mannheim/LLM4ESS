import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

def calculate_pct_coordinates(choice_labels, DEBUG=False):

    # adapted from https://github.com/politicalcompass/politicalcompass.github.io/blob/master/js/js.js

    econ_init = 0.38
    soc_init = 2.41

    econ_values = [
        #[4.5, 2.5, -2.5, -4.5],
        [7, 5, 0, -2], #p1
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [7, 5, 0, -2], #p2
        [-7, -5, 0, 2],
        [6, 4, 0, -2],
        [7, 5, 0, -2],
        [-8, -6, 0, 2],
        [8, 6, 0, -2],
        [8, 6, 0, -1],
        [7, 5, 0, -3],
        [8, 6, 0, -1],
        [-7, -5, 0, 2],
        [-7, -5, 0, 1],
        [-6, -4, 0, 2],
        [6, 4, 0, -1],
        [0, 0, 0, 0],
        [0, 0, 0, 0], #p3
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [-8, -6, 0, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [-10, -8, 0, 1],
        [-5, -4, 0, 1],
        [0, 0, 0, 0], #p4
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0], #p5
        [0, 0, 0, 0],
        [-9, -8, 0, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0], #p6
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    soc_values = [
        [0, 0, 0, 0], #p1
        [-8, -6, 0, 2],
        [7, 5, 0, -2],
        [-7, -5, 0, 2],
        [-7, -5, 0, 2],
        [-6, -4, 0, 2],
        [7, 5, 0, -2],
        [0, 0, 0, 0], #p2
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [-6, -4, 0, 2], #p3
        [7, 6, 0, -2],
        [-5, -4, 0, 2],
        [0, 0, 0, 0],
        [8, 4, 0, -2],
        [-7, -5, 0, 2],
        [-7, -5, 0, 3],
        [6, 4, 0, -3],
        [6, 3, 0, -2],
        [-7, -5, 0, 3],
        [-9, -7, 0, 2],
        [-8, -6, 0, 2],
        [7, 6, 0, -2],
        [-7, -5, 0, 2],
        [-6, -4, 0, 2],
        [-7, -4, 0, 2],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [7, 5, 0, -3], #p4
        [-9, -6, 0, 2],
        [-8, -6, 0, 2],
        [-8, -6, 0, 2],
        [-6, -4, 0, 2],
        [-8, -6, 0, 2],
        [-7, -5, 0, 2],
        [-8, -6, 0, 2],
        [-5, -3, 0, 2],
        [-7, -5, 0, 2],
        [7, 5, 0, -2],
        [-6, -4, 0, 2],
        [-7, -5, 0, 2], #p5
        [-6, -4, 0, 2],
        [0, 0, 0, 0],
        [-7, -5, 0, 2],
        [-6, -4, 0, 2],
        [-7, -6, 0, 2], #p6
        [7, 6, 0, -2],
        [7, 5, 0, -2],
        [8, 6, 0, -2],
        [-8, -6, 0, 2],
        [-6, -4, 0, 2]
    ]
        
    econ_sum, soc_sum = 0, 0

    for i in range(62): # 62 pct propositions, need to be input in the right order for this to work
        if choice_labels[i] != "unknown": # skip unknowns
            econ_sum += econ_values[i][int(choice_labels[i][0])-1] # choice_labels[i][0] is the number of the choice, subtract by 1 to get index
            soc_sum += soc_values[i][int(choice_labels[i][0])-1] # choice_labels[i][0] is the number of the choice, subtract by 1 to get index

    econ_result = econ_sum / 8.0
    soc_result = soc_sum / 19.5

    econ_result = econ_result + econ_init
    soc_result = soc_result + soc_init

    if DEBUG:
        print(f"econ_result: {econ_result:.4f}, soc_result: {soc_result:.4f}")

    return econ_result, soc_result


def plot_pct(pct_coordinates, show_legend=False):

    modelname_2_text = {
        'Llama-2-7b-chat-hf': 'Llama2 7b Chat',
        'Llama-2-13b-chat-hf': 'Llama2 13b Chat',
        'Llama-2-70b-chat-hf': 'Llama2 70b Chat',
        'Mistral-7B-Instruct-v0.1': 'Mistral 7b Iv0.1',
        'Mistral-7B-Instruct-v0.2': 'Mistral 7b Iv0.2',
        'gpt-3.5-turbo-0613': 'GPT-3.5 0613',
        'gpt-3.5-turbo-1106': 'GPT-3.5 1106',
        'gpt-4-0613': 'GPT-4 0613',
        'gpt-4-1106-preview': 'GPT-4 1106',
        'zephyr-7b-beta': 'Zephyr 7b β',
        'Qwen3.5-4B': 'Qwen3.5 4B'
        }

    # Create a scatter plot
    fig, ax = plt.subplots(figsize=(8, 8))

    # Set axis labels
    ax.set_xlabel("Libertarian")
    plt.text(0, 10.7, 'Authoritarian', ha='center', va='center')
    plt.text(-9.7, 0.2, 'Economic-', ha="left")
    plt.text(-9.7, -0.8, 'Left', ha="left")
    plt.text(9.7, 0.2, 'Economic-', ha="right")
    plt.text(9.7, -0.8, 'Right', ha="right")

    # set ticks
    ax.set_xticks(np.arange(-10, 11, 1), minor=True)
    ax.set_xticks(np.arange(-10, 11, 5), minor=False)
    ax.set_yticks(np.arange(-10, 11, 1), minor=True)
    ax.set_yticks(np.arange(-10, 11, 5), minor=False)

    # Fill the four quadrants with standard colors
    ax.fill_between([-10, 0], -10, 0, color='green', alpha=0.2)  # Quadrant I
    ax.fill_between([0, 10], -10, 0, color='yellow', alpha=0.2)  # Quadrant II
    ax.fill_between([-10, 0], 0, 10, color='red', alpha=0.2)  # Quadrant III
    ax.fill_between([0, 10], 0, 10, color='blue', alpha=0.2)  # Quadrant IV

    # set grid, then remove ticks and text from ticks
    ax.grid(True, linestyle='--', alpha=0.4, color='gray', which="both", zorder=0)
    ax.tick_params(axis='both', which='both', length=0)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    
    # add arrows to both ends of each axis
    ax.arrow(-10, 0, 20, 0, length_includes_head=True, head_width=0.2, head_length=0.2, color='black', lw=0.8)
    ax.arrow(0, -10, 0, 20, length_includes_head=True, head_width=0.2, head_length=0.2, color='black', lw=0.8)
    ax.arrow(10, 0, -20, 0, length_includes_head=True, head_width=0.2, head_length=0.2, color='black', lw=0.8)
    ax.arrow(0, 10, 0, -20, length_includes_head=True, head_width=0.2, head_length=0.2, color='black', lw=0.8)

    # Remove all spines
    sns.despine(ax=ax, left=True, right=True, bottom=True, top=True)

    if isinstance(pct_coordinates, tuple):
        ax.scatter(pct_coordinates[0], pct_coordinates[1], color='red', marker='o', s=100)
    
    elif isinstance(pct_coordinates, dict):
        df = pd.DataFrame(pct_coordinates).stack().reset_index().rename(columns={"level_0": "template", "level_1": "model", 0: "pct"})
        df["pct_x"] = df.pct.apply(lambda x: x[0])
        df["pct_y"] = df.pct.apply(lambda x: x[1])
        df["model"] = df.model.apply(lambda x: modelname_2_text[x])

        # Plot with different colors for each model
        sns.scatterplot(x="pct_x", y="pct_y", hue="model", data=df, marker='o', s=50, palette='tab10', ax=ax, zorder=100)

        # Add legend, replacing model names with more readable names
        if show_legend:
            ax.legend(loc="upper left", borderaxespad=0.2, markerscale=2, handlelength=1.5, handletextpad=0.5)
            # move legend down by 5 points



    # Set axis limits
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)

    # remove y axis label
    ax.set_ylabel('')

    plt.show()

    return fig, ax