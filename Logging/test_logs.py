# Logging - Means capture details,which are useful while debugging
# show user details about execution of program

# Warning to the users
# Information to the users
# Errors ,critical errors user

import logging
def test_print_logs():
  LOGGER = logging.getLogger('__name__')
# Intentional logging to user
  LOGGER.info("This is information logs")
  LOGGER.warning("This is Warning logs")
  LOGGER.error("This is Error logs")
  LOGGER.critical("This is critical logs")
