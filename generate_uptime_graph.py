import matplotlib.pyplot as plt
import numpy as np
import json
import datetime

def generate_uptime_graph(uptime_data, status, output_file='uptime_graph.png'):
    # Parse the uptime data
    dates = [datetime.datetime.strptime(day['date'], '%Y-%m-%d') for day in uptime_data]
    uptimes = [day['uptime'] for day in uptime_data]

    # Set color based on status
    if status == "operational":
        color = "green"
    elif status == "partial":
        color = "orange"
    else:
        color = "red"

    # Create the plot
    plt.figure(figsize=(10, 5))
    plt.plot(dates, uptimes, marker='o', color=color)
    plt.fill_between(dates, uptimes, color=color, alpha=0.2)
    plt.title('Miko Radio Uptime Status')
    plt.xlabel('Date')
    plt.ylabel('Uptime (%)')
    plt.ylim(0, 100)
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Save the graph to a file
    plt.savefig(output_file)
    plt.close()

if __name__ == "__main__":
    import sys
    status = sys.argv[1] if len(sys.argv) > 1 else "operational"
    output_file = sys.argv[2] if len(sys.argv) > 2 else "uptime_graph.png"
    
    # Example uptime data, replace this with actual data fetching
    uptime_data = [
        {"date": "2024-05-25", "uptime": 100},
        {"date": "2024-05-26", "uptime": 95},
        {"date": "2024-05-27", "uptime": 90},
        {"date": "2024-05-28", "uptime": 85},
        {"date": "2024-05-29", "uptime": 80},
        {"date": "2024-05-30", "uptime": 75},
        {"date": "2024-05-31", "uptime": 70},
    ]
    
    generate_uptime_graph(uptime_data, status, output_file)
