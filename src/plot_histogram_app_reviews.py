import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = 'capcut_app_reviews.xlsx'

# Load the data from "Sheet2"
data_sheet2 = pd.read_excel(file_path, sheet_name='Sheet2')

# Generate the histogram
plt.figure(figsize=(10, 8))
data_count = data_sheet2['Summary'].value_counts()
data_percent = data_count / data_count.sum() * 100  # Calculate percentages
bars = data_count.plot(kind='bar')
plt.title('Distribution of App Store Critical Reviews (Last 12 months)')
plt.xlabel('Summary Categories')
plt.ylabel('Frequency')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Annotate each bar with the percentage
for bar in bars.patches:
    plt.annotate(f'{bar.get_height() * 100 / data_count.sum():.1f}%', 
                 (bar.get_x() + bar.get_width() / 2, bar.get_height()), 
                 ha='center', va='bottom')

# Save the plot as an SVG file
svg_file_path = 'review_summaries_histogram.svg'
plt.savefig(svg_file_path, format='svg')

# Display the plot if needed
# plt.show()

print(f"Graph saved as SVG at: {svg_file_path}")