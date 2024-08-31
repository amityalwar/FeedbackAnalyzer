import pandas as pd
import matplotlib.pyplot as plt

def generate_reddit_histogram(input_file: str, output_file: str):
    """Generate a histogram from Reddit feedback data and save it as an SVG file."""
    # Load data
    data_sheet2 = pd.read_excel(input_file, sheet_name='Sheet2')

    # Use a dark theme style as a base
    plt.style.use('seaborn-v0_8-dark')

    # Configure plot aesthetics for a dark grey background site
    plt.rc('font', family='Arial')
    plt.rc('text', color='white')
    plt.rc('xtick', color='white', labelsize=12)
    plt.rc('ytick', color='white', labelsize=12)
    plt.rc('axes', labelcolor='white', edgecolor='lightgray')

    # Generate the histogram
    plt.figure(figsize=(10, 6))
    data_count = data_sheet2['User Feedback'].value_counts()
    bars = data_count.plot(kind='bar', color='white')

    plt.title('Distribution of User Concerns on VisionPro Subreddit (n=281)', fontsize=16, weight='normal')
    plt.xlabel('Categories', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Simplify design, adjust for transparent background
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_color('lightgray')
    plt.gca().spines['bottom'].set_color('lightgray')

    # Annotate each bar with the percentage
    for bar in bars.patches:
        plt.annotate(f'{bar.get_height() * 100 / data_count.sum():.1f}%', 
                     (bar.get_x() + bar.get_width() / 2, bar.get_height()), 
                     ha='center', va='bottom', color='white', fontsize=10)

    # Save the plot with a transparent background
    plt.savefig(output_file, format='svg', bbox_inches='tight', transparent=True)
    print(f"Graph saved as SVG with a transparent background at: {output_file}")

if __name__ == "__main__":
    print("This script is not meant to be run directly. Please use main.py to execute the Reddit histogram generator.")