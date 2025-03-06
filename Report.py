import os
import glob
import time
from datetime import datetime, timedelta
# Define log paths
db_log_path = 'db_logs'
app_log_path = 'app_logs'
output_log_path = 'Nimble_LOG'
# Create output directory if it doesn't exist
os.makedirs(output_log_path, exist_ok=True)
def get_recent_files(log_path):
    """Get the most recent HTML log file in the specified path."""
    # Get all HTML files in the directory
    html_files = glob.glob(os.path.join(log_path, '*.html'))
    # Filter files modified within the last 12 hours
    recent_files = [f for f in html_files if time.time() - os.path.getmtime(f) < 12 * 3600]
    if not recent_files:
        return None
    # Return the most recently modified file
    return max(recent_files, key=os.path.getmtime)
def merge_logs(db_file, app_file):
    """Merge the contents of the DB and App log files into one HTML file."""
    with open(db_file, 'r', encoding='utf-8') as db_f:
        db_content = db_f.readlines()
    with open(app_file, 'r', encoding='utf-8') as app_f:
        app_content = app_f.readlines()
    # Extract header and body content
    db_header = db_content[:len(db_content) // 2]
    db_body = db_content[len(db_content) // 2:]
    app_header = app_content[:len(app_content) // 2]
    app_body = app_content[len(app_content) // 2:]
    # Create a new HTML structure
    combined_html = f"""
            {''.join(db_header)}
            {''.join(db_body)}
            {''.join(app_header)}
            {''.join(app_body)}
    """
    return combined_html
def main():
    db_file = get_recent_files(db_log_path)
    app_file = get_recent_files(app_log_path)
    if not db_file or not app_file:
        print("No recent log files found in one or both directories.")
        return
    db_filename = os.path.basename(db_file)
    app_filename = os.path.basename(app_file)
    # Check if filenames match or start with the same characters
    if db_filename[:3] != app_filename[:3]:
        print("The log files do not match based on their names.")
        return
    # Merge logs
    merged_content = merge_logs(db_file, app_file)
    # Extract the common base name for output
    common_base_name = db_filename.split('.')[0]  # Use the DB filename as the base
    output_filename = f"{common_base_name}.html"  # Only include the base name
    output_file_path = os.path.join(output_log_path, output_filename)
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(merged_content)
    print(f"Merged log file created: {output_file_path}")
if __name__ == "__main__":
    main()