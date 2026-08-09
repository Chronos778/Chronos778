import json
import os
from datetime import datetime

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]
BOX_SIZE = 10
BOX_MARGIN = 4
WEEKS = 53
DAYS_PER_WEEK = 7

def render_heatmap(data_path, output_path):
    print(f"Loading {data_path}...")
    try:
        with open(data_path, 'r') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error loading data: {e}")
        return

    # Data is a list of {'date': 'YYYY-MM-DD', 'level': int}. It might be more or fewer than exactly 53 weeks.
    # Usually GitHub gives us the last 365 days. Let's pad it to a 53x7 grid, column major.
    
    # Let's map data to a list of levels.
    levels = [d.get('level', 0) for d in data]
    total_days = len(levels)
    
    # Calculate dimensions
    width = WEEKS * (BOX_SIZE + BOX_MARGIN) + 40 # extra for padding
    height = DAYS_PER_WEEK * (BOX_SIZE + BOX_MARGIN) + 60 # extra for footer/legend
    
    with open(output_path, 'w') as f:
        f.write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">\n')
        f.write('  <style>\n')
        f.write('    .box { rx: 2; ry: 2; opacity: 0; animation: slideDown 0.8s ease forwards; }\n')
        f.write('    @keyframes slideDown { from { transform: translateY(-10px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }\n')
        f.write('    .text { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 12px; fill: #8b949e; }\n')
        f.write('  </style>\n')
        
        # Draw the grid
        for i, level in enumerate(levels):
            # GitHub calendar is arranged by column first (each column is a week)
            week = i // DAYS_PER_WEEK
            day = i % DAYS_PER_WEEK
            
            x = 20 + week * (BOX_SIZE + BOX_MARGIN)
            y = 20 + day * (BOX_SIZE + BOX_MARGIN)
            
            # constrain level to max palette index (some users have level 4, but our palette has 6 colors)
            # Actually, standard is 0-4. Our palette is length 6, so level 0->0, level 1->1..4->4.
            col_idx = min(level, len(PALETTE) - 1)
            color = PALETTE[col_idx]
            
            # Diagonal stagger delay: week + day
            delay = (week + day) * 0.035
            
            f.write(f'  <rect class="box" x="{x}" y="{y}" width="{BOX_SIZE}" height="{BOX_SIZE}" fill="{color}" style="animation-delay: {delay}s;" />\n')

        # Add a legend
        legend_x = width - (len(PALETTE) * (BOX_SIZE + BOX_MARGIN) + 80)
        legend_y = height - 20
        f.write(f'  <text x="{legend_x - 30}" y="{legend_y + 9}" class="text">Less</text>\n')
        for i, color in enumerate(PALETTE):
            f.write(f'  <rect x="{legend_x + i * (BOX_SIZE + BOX_MARGIN)}" y="{legend_y}" width="{BOX_SIZE}" height="{BOX_SIZE}" fill="{color}" rx="2" ry="2" />\n')
        f.write(f'  <text x="{legend_x + len(PALETTE) * (BOX_SIZE + BOX_MARGIN) + 10}" y="{legend_y + 9}" class="text">More</text>\n')
        
        f.write('</svg>\n')
    print(f"Saved heatmap SVG to {output_path}")

if __name__ == "__main__":
    render_heatmap("data/contributions.json", "contrib-heatmap.svg")
