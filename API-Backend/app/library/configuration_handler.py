
class ConfigurationHandler:
    def __init__(self):
        # define variables that you want to fetch and set from configuration service. Only use A-Z and _ in names.
        self.DATABASE_CONNECTION_STRING = 'postgresql://postgres:password123!@64.227.179.202:5432/freshersonly'
        self.AUTH_JWT_SECRET = 'ABCD'
        self.AUTH_JWT_ALGORITHM = 'HS256'

