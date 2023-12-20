import pandas as pd
import pyodbc

#Conexão com Sql Server
#connection = pyodbc.connect("DSN=SQLServer") 

server = '.\kriarserver' 
database = 'tempdb' 
username = 'sa' 
password = 'Kriar2015' 
#cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
#cursor = cnxn.cursor()

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server='+server+';'
                      'Database='+database+';'
                      'Trusted_Connection=yes;'
                      'UID='+username+';PWD='+ password
                      )

df = pd.read_sql_query(
    'SELECT ' +
    ' program_name, ' +
    ' login_name, ' +
    ' memory_usage, ' +
    ' cpu_time, ' +
    
    ' session_id, ' +
    ' login_time, ' +
    ' host_name, ' +
    ' client_interface_name, ' +
    ' status, ' +
    ' last_request_start_time, ' +
    ' last_request_end_time ' +

    'FROM sys.dm_exec_sessions ' +

    ' Where cpu_time > 0 or memory_usage > 0 ' +

    ' ORDER BY memory_usage desc, cpu_time desc, status'    
    , conn)  

with open('UsersSqlServer.txt', 'w') as f:
    dfAsString = df.to_string(header=True, index=False)
    f.write(dfAsString)    

print(df)
print(type(df))                      

x = input('tecle enter para encerrar')