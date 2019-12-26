# BACKEND = 'frontera.contrib.backends.sqlalchemy.Distributed'
# MAX_REQUESTS = 2000
# MAX_NEXT_REQUESTS = 10
# DELAY_ON_EMPTY = 0.0

# following 2 settings tells frontera that crawwler is running locally
SPIDER_FEED_PARTITIONS = 4
SPIDER_LOG_PARTITIONS = 4

BACKEND = 'frontera.contrib.backends.sqlalchemy.Distributed'
SQLALCHEMYBACKEND_ENGINE = 'sqlite:///dcrawlers.db'

