#!/usr/bin/env python

import logging
import logging.config
from os import path

log_file_path = path.join(path.dirname(path.abspath(__file__)), 'log.config')
logging.config.fileConfig(log_file_path, disable_existing_loggers=False)
logger = logging.getLogger()
logger.debug('often makes a very good meal of %s', 'visiting tourists')