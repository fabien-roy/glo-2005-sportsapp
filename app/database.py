class Database:
    connection = None

    def create_connection(self):
        pass

    def connect(self):
        if self.connection is None:
            self.connection = self.create_connection()

        return self.connection
