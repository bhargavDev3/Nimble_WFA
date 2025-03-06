# Server_main.py
import os
# Common variables for App_server
client_name = "Hallmark"  # Client name
date = "06/03/2025"  # Today date,    format sholud be like:  03/12/2024  day month year
app_pool_date = date.replace("/", "")
app_pool_name = f"{client_name}_{app_pool_date}"
site_name = client_name
application_name = "OCRWEBAPI"  # Application name under client site

# Paths for App_server
WINRAR_PATH = r"C:\Program Files\WinRAR\WinRAR.exe"
New_Build_Source = r"C:/ProductionRealease/NewBuild_13022025/NewBuild_13022025/NewBuild"  # Change with New Build path
base_path = r"C:\Production2"  # Change with client base path from C drive
completion_flag_file = os.path.join(base_path, "copy_paste_completed.flag")

# Common variables for DataBase_server
Date = date  # Date for log file naming
CLIENT_NAME = client_name  # Change this to the new client name
DataBase = 'RaghuDB'   # Shared between sql.py and rdl.py
Start_Year = "2024"         # Common Year for both SQL and RDL scripts
Start_Month = "09.September"  # Common Month for both SQL and RDL scripts
Start_Date = "01092024"   # Common date for both SQL and RDL scripts

# SQL Server credentials (shared with sql.py)
server = 'HALLMARK2'  # Server name or IP address
username = 'sa'
password = 'New31298@'
database_sql = DataBase  # Shared between sql.py and rdl.py

# SQL Script Directory (GitLab repo location)
SQL_BASE_DIR = r"C:\Users\bhargavhallmark\database automation\database-automation\sqls"
SQL_START_YEAR = Start_Year
SQL_START_MONTH = Start_Month
SQL_START_DATE = Start_Date

# RDL Deployment constants (shared with rdl.py)
RDL_BASE_DIR = r"C:\Users\bhargavhallmark\database automation\database-automation\rdls"
RDL_START_YEAR = Start_Year
RDL_START_MONTH = Start_Month
RDL_START_DATE = Start_Date

VS_PATH = r"C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\devenv.exe"

REPORT_USER = "bhargavhallmark"
REPORT_PASSWORD = "t,}f^:oL^^ZF5^b"
REPORT_SERVER_URL = "http://hallmark2/Reports"

# For .rds DataSource
NEW_DATA_SOURCE = "HALLMARK2"
database_rdl = DataBase  # Shared between sql.py and rdl.py