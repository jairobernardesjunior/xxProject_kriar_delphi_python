SELECT 
    program_name,
    login_name,
    memory_usage,
    cpu_time,
    
    session_id,
    login_time,
    host_name,
    client_interface_name,
    status,
    last_request_start_time,
    last_request_end_time,
    transaction_isolation_level,
    lock_timeout,
    deadlock_priority
FROM 
    sys.dm_exec_sessions 
WHERE
    login_name NOT IN ('sa', 'AUTORIDADE NT\SISTEMA', 'NT AUTHORITY\SYSTEM')
--and host_name = 'KRIARWVM2021'
ORDER BY memory_usage desc, cpu_time desc