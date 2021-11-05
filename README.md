py-telnet-logger
================

*Telnet-logger* is a python tool that can connect via telnet protocol to specified remote address and write every line from output to a log file adding timestamps. It can reconnect on every connection lost scenario. Additionally it can periodically send specified commands creating simple watchdog activity.
1. telnet_logger.py 
   1.1 if password is not supplied by configuration file or command line,lookup password_db.txt for the host's password automtically
   1.2 Explanatio of the configuration items
      # keep-alive command
      wd_cmd=echo QWERTYUIOP
      # expected keep-alive reponse
      # response is not logged and could be blocked by output of current process
      # empty = keep-alive disabled
      wd_response=.*QWERTYUIOP.*
      # interval to send keep-alive command
      wd_delay=10
      # re-connect timer(reset by every line received)
      wd_max_wait=30
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
   -c CFG, --cfg=CFG     configuration file (defaults to ~/telnet_logger.ini


