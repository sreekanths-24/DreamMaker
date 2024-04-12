import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO

def generate_goal_journey_report_image(user, current_dream, todos, events):
    # Create a new figure with a colorful background
    fig, ax = plt.subplots(figsize=(12, 10))
    fig.patch.set_facecolor('#F0F0F0')  # Set background color

    # Add the name of the goal at the top with a large, bold font
    goal_title_text = ax.text(0.5, 0.95, f"Goal: {current_dream.title}", horizontalalignment='center', fontsize=20, fontweight='bold', color='#333333')

    # Calculate the vertical position for the first table (todos)
    table1_y_position = 0.8 if todos else 0.95  # Position below the goal title if todos exist, otherwise same as the goal title

    # Create table for todos if data is available
    if todos:
        # Add title for the todos table
        todo_title_text = ax.text(0.5, table1_y_position, 'Todos', horizontalalignment='center', fontsize=16, fontweight='bold')

        # Create the todos table
        todo_data = [(todo.title, todo.description, todo.duedate, todo.complete, todo.priority) for todo in todos]
        todo_df = pd.DataFrame(todo_data, columns=['Title', 'Description', 'Due Date', 'Complete', 'Priority'])
        todo_table = ax.table(cellText=todo_df.values, colLabels=todo_df.columns, loc='center', colWidths=[0.15, 0.25, 0.1, 0.1, 0.1], cellLoc='center', colColours=['#EFEFEF']*5, bbox=[0.1, table1_y_position - 0.3, 0.8, 0.25])

    # Calculate the vertical position for the second table (events)
    table2_y_position = table1_y_position - 0.5  # Position below the first table

    # Create table for events if data is available
    if events:
        # Add title for the events table
        event_title_text = ax.text(0.5, table2_y_position, 'Events', horizontalalignment='center', fontsize=16, fontweight='bold')

        # Create the events table
        event_data = [(event.name, event.startdate, event.enddate, event.description) for event in events]
        event_df = pd.DataFrame(event_data, columns=['Name', 'Start Date', 'End Date', 'Description'])
        event_table = ax.table(cellText=event_df.values, colLabels=event_df.columns, loc='center', colWidths=[0.2, 0.2, 0.2, 0.4], cellLoc='center', colColours=['#EFEFEF']*4, bbox=[0.1, table2_y_position - 0.3, 0.8, 0.25])

    table3_y_position = table2_y_position - 0.5
    # Add "DreamMaker" text on the bottom right corner
    dreammaker_text = ax.text(0.99, table3_y_position, 'DreamMaker', horizontalalignment='right', verticalalignment='bottom', fontsize=12, color='#333333')

    # Remove axis
    ax.axis('off')

    # Save the plot as an image file
    buffer = BytesIO()
    plt.savefig(buffer, format='png', facecolor=fig.get_facecolor())  # Preserve background color
    buffer.seek(0)
    plt.close(fig)  # Close the figure to release memory
    return buffer.getvalue()
