py-telnet-logger
================

*Telnet-logger* is a python tool that can connect via telnet protocol to specified remote address and write every line from output to a log file adding timestamps. It can reconnect on every connection lost scenario. Additionally it can periodically send specified commands creating simple watchdog activity.

2. batch_telnet_logger.py
    read hosts from telnet_target.txt
    find login password for each host from password_db.txt
    for each hosts, start an process to execute:
        python3 telnet_logger.py --host host --password _pwd --cfg ini_configuration_file --file-dir log_dir
        if there are multiple ini_configuration_files existing in current folder, repeat above command for each file

1. telnet_logger.py
   1.1 if password is not supplied by configuration file or command line,lookup password_db.txt for the host's password automtically
   1.2 explanation of the configuration items
   -------------------------------------------
           [global]

           host=192.168.1.1
           port=23
           user=root

       # if not provisioned by configuration file or command line, look it up in password_db.txt
           password=
           #password=Kn7Jq4No8Oh3
           password_prompt=Password:
           login_prompt=login

       # text phrase to be recognized as a successful login confirmation
           logged_phrase=G C T   L T E   M O D E M

       # commands to be sent to remote host after login, saprated by "|"
           #initial_cmd=ping 192.168.1.1 -c 2|pwd|cd /|ls
           initial_cmd=lted_cli|arm1log 2|sys ver
           initial_cmd_error_phrase=

       # filename of a log file
       # log file name format: "file_dir"/"host"-"timestamp"_filename
           filename=cmd.log
           file_dir=/Users/ezhou/Downloads/logger_test

       # = comment out configurations

       # 'watchdog command' text to send to remote host periodically
       #  also as "keep-alive" command
           #wd_cmd=echo QWERTYUIOP
           wd_cmd=AT

       # expected keep-alive/wd reponse
       # empty = keep-alive/wd disabled
       # response is not logged and could be blocked by output of current process
       # so current implementation is not to match the wd_response,
       # every line received will be regarded as keep-alive reponse thus reset the reconnect timer
           wd_response=.*QWERTYUIOP.*

       # interval to send keep-alive/wd command
           wd_delay=10

       # re-connect timer(reset by every line received)
           wd_max_wait=30
           sig_usr1_cmd=

       # wait time before issue a reconnection after a connection failure or failed re-connection
           reconnect_delay=5

       # max logs: # of backup log files
       # max_log_size: max size of each log file
       # The file being written to is always "xx.log" - when it gets filled up,
       # it is closed and renamed to "xx.log.1", and if files "xx.log.1", "xx.log.2" etc. exist,
       # then they are renamed to "app.log.2", "app.log.3" etc. respectively.
           max_logs=2
           max_log_size=100000000

       # quit the telnet session after sessio_timer is up
           session_timer=60
   -------------------------------------------

   1.3 command line  options:
        Usage: telnet_logger.py [options]

        Options:
          -h, --help            show this help message and exit
          -H HOST, --host=HOST  target telnet host name (defaults to localhost)
          -P PORT, --port=PORT  destination connection port. (defaults to 23)
          -u USER, --user=USER  user name (defaults to current user)
          -p PASSWORD, --password=PASSWORD
                                password
          --login-prompt=LOGIN_PROMPT
                                login prompt to wait for (defaults to 'ogin:'
          --password-prompt=PASSWORD_PROMPT
                                password prompt to wait for (defaults to 'assword:')
          --logged-phrase=LOGGED_PHRASE
                                text phrase to be recognized as a successful login
                                confirmation
          --wd-cmd=WD_CMD       'watchdog command' text to send to remote host
                                periodically
          --wd-start-after-delay=WD_START_AFTER_DELAY
                                time after logged before start watchdog (not
                                implemented yet)
          --wd-start=after-phrase=WD_START_AFTER_PHRASE
                                phrase in output after start watchdog (not implemented
                                yet)
          --wd-max-wait=WD_MAX_WAIT
                                maximum time to wait for watchdog response (not
                                implemented yet)
          --wd-response=WD_RESPONSE
                                text phrase recognized as watchdog response (not
                                implemented yet)
          --sig-usr1-cmd=SIG_USR1_CMD
                                command to be sent to remote side after receiving USR1
                                signal
          --sig-usr2-cmd=SIG_USR2_CMD
                                command to be sent to remote side after receiving USR2
                                signal
          --wd-delay=WD_DELAY   delay between successive sending watchdog commands
          --initial-cmd=INITIAL_CMD
                                command to be sent to remote host after login
          --initial-cmd-error-phrase=INITIAL_CMD_ERROR_PHRASE
                                remote response phrase to resend initial command
          --reconnect-delay=RECONNECT_DELAY
                                delay after connection lost/error and retry
          --filename=FILENAME   filename of a log file
          --file-dir=FILE_DIR   directory of a log file
          -c CFG, --cfg=CFG     configuration file (defaults to telnet_logger.ini under current dir



