# db_main.py

import sql
import rdl
import pyttsx3
from db_log_utils import create_log_file, write_log, close_log_file
import sys
import os

# Add the root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import common variables from Server_main.py
from Server_main import Date, CLIENT_NAME, DataBase, Start_Year, Start_Month, Start_Date, server, username, password, database_sql, SQL_BASE_DIR, SQL_START_YEAR, SQL_START_MONTH, SQL_START_DATE, RDL_BASE_DIR, RDL_START_YEAR, RDL_START_MONTH, RDL_START_DATE, VS_PATH, REPORT_USER, REPORT_PASSWORD, REPORT_SERVER_URL, NEW_DATA_SOURCE, database_rdl

# Define the engine to specify which scripts to run
engine = ("sql", "rdl")  # Options: ("sql", "rdl"), ("sql"), ("rdl")

# Initialize voice engine
Spell = pyttsx3.init()

# Function to play voice alert
def play_voice_alert(client_name):
    voice_message = f"Hi sir, The Deployment of {client_name} completed Successfully"
    Spell.setProperty('volume', 1)
    Spell.setProperty('rate', 125)
    Spell.say(voice_message)
    Spell.runAndWait()

if __name__ == "__main__":
    # Create the log file
    log_file = create_log_file(CLIENT_NAME, Date)  # Pass both CLIENT_NAME and Date

    # Counter for log entries
    s_no = 1

    # Execute sql.py if "sql" is in the engine
    if "sql" in engine:
        print("Executing SQL scripts...")

        # Execute SQL scripts
        success_count, fail_count, paths_successful, paths_failed = sql.execute_sql_scripts(server, username, password, database_sql, SQL_BASE_DIR, SQL_START_YEAR, SQL_START_MONTH, SQL_START_DATE)

        # Log SQL execution results
        write_log(log_file, s_no, "SQL", CLIENT_NAME, success_count, fail_count, paths_failed)
        s_no += 1

    # Execute rdl.py if "rdl" is in the engine
    if "rdl" in engine:
        print("Executing RDL deployment...")

        # Execute RDL deployment
        success_count, fail_count, paths_successful, paths_failed = rdl.execute_rdl_deployment(
            RDL_BASE_DIR, RDL_START_YEAR, RDL_START_MONTH, RDL_START_DATE, 
            CLIENT_NAME, VS_PATH, REPORT_USER, REPORT_PASSWORD, 
            REPORT_SERVER_URL, NEW_DATA_SOURCE, database_rdl
        )

        # Log RDL execution results
        write_log(log_file, s_no, "RDL", CLIENT_NAME, success_count, fail_count, paths_failed)
        s_no += 1

    # Close the log file
    close_log_file(log_file)

    # Play voice alert after deployment
    play_voice_alert(CLIENT_NAME)