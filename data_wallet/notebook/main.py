import sqlite3

# TODO Create a notebook to keep track of the following:
# 1. Personal notes
# 2. Data wallet related
# 3. Codebase documentation
# 4. Reference from one source to another wtih subscriptions

class Notebook:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS source
                             (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, description TEXT, context_id INTEGER, FOREIGN KEY(context_id) REFERENCES context(id))''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS source_notes
                             (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, description TEXT, context_id INTEGER, FOREIGN KEY(context_id) REFERENCES context(id))''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS references
                             (id INTEGER PRIMARY KEY AUTOINCREMENT, source_id INTEGER, relation TEXT, permission TEXT, context_id INTEGER, FOREIGN KEY(source_id) REFERENCES source(id), FOREIGN KEY(context_id) REFERENCES context(id))''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS subscriptions
                             (id INTEGER PRIMARY KEY AUTOINCREMENT, source_id INTEGER, subscriber_id INTEGER, context_id INTEGER, FOREIGN KEY(source_id) REFERENCES source(id), FOREIGN KEY(context_id) REFERENCES context(id))''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS permissions
                             (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, context_id INTEGER, view_permission BOOLEAN, query_permission BOOLEAN, FOREIGN KEY(context_id) REFERENCES context(id))''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS context
                             (id INTEGER PRIMARY KEY AUTOINCREMENT, source TEXT, subject TEXT, keywords TEXT)''')
        self.conn.commit()

    def add(self, source: str, relation: str, permission: str, subject: str, keywords: str, attempt_without_being_recorded: bool = False):
        try:
            # Insert context
            self.cursor.execute("INSERT INTO context (source, subject, keywords) VALUES (?, ?, ?)", (source, subject, keywords))
            context_id = self.cursor.lastrowid

            # Insert source
            self.cursor.execute("INSERT INTO source (title, description, context_id) VALUES (?, ?, ?)", (source, '', context_id))
            source_id = self.cursor.lastrowid

            # Insert reference
            self.cursor.execute("INSERT INTO references (source_id, relation, permission, context_id) VALUES (?, ?, ?, ?)", (source_id, relation, permission, context_id))
            self.conn.commit()

            if not attempt_without_being_recorded:
                # Insert source note
                self.cursor.execute("INSERT INTO source_notes (title, description, context_id) VALUES (?, ?, ?)", (source, '', context_id))
                self.conn.commit()

            return True
        except sqlite3.Error as e:
            print(f"Error adding data: {e}")
            self.conn.rollback()
            return False

    def get(self, source: str, relation: str, permission: str, subject: str, keywords: str, user_id: int, attempt_without_being_recorded: bool = False):
        try:
            # Get context_id from context table
            self.cursor.execute("SELECT id FROM context WHERE source = ? AND subject = ? AND keywords = ?", (source, subject, keywords))
            context_id = self.cursor.fetchone()[0]

            # Check if user has view permission for the given context
            if not self.has_view_permission(user_id, context_id):
                return None

            # Get source_id from source table
            self.cursor.execute("SELECT id FROM source WHERE title = ? AND context_id = ?", (source, context_id))
            source_id = self.cursor.fetchone()[0]

            # Get reference data from references table
            self.cursor.execute("SELECT * FROM references WHERE source_id = ? AND relation = ? AND permission = ? AND context_id = ?", (source_id, relation, permission, context_id))
            reference_data = self.cursor.fetchall()

            # Get source note data from source_notes table
            if not attempt_without_being_recorded:
                self.cursor.execute("SELECT * FROM source_notes WHERE title = ? AND context_id = ?", (source, context_id))
                source_note_data = self.cursor.fetchall()
            else:
                source_note_data = []

            # Get subscription data from subscriptions table
            self.cursor.execute("SELECT subscriber_id FROM subscriptions WHERE source_id = ? AND context_id = ?", (source_id, context_id))
            subscription_data = [row[0] for row in self.cursor.fetchall()]

            return {
                "source": source,
                "relation": relation,
                "permission": permission,
                "subject": subject,
                "keywords": keywords,
                "reference_data": reference_data,
                "source_note_data": source_note_data,
                "subscription_data": subscription_data
            }
        except sqlite3.Error as e:
            print(f"Error getting data: {e}")
            return None

    def remove(self, source_id: int, context_id: int, user_id: int):
        try:
            # Check if user has permission to remove data in the given context
            if not self.has_permission(user_id, context_id, view_permission=True, query_permission=True):
                return False

            # Delete reference
            self.cursor.execute("DELETE FROM references WHERE source_id = ? AND context_id = ?", (source_id, context_id))

            # Delete source
            self.cursor.execute("DELETE FROM source WHERE id = ? AND context_id = ?", (source_id, context_id))

            # Delete source note
            self.cursor.execute("DELETE FROM source_notes WHERE title = (SELECT title FROM source WHERE id = ?) AND context_id = ?", (source_id, context_id))

            # Delete subscriptions
            self.cursor.execute("DELETE FROM subscriptions WHERE source_id = ? AND context_id = ?", (source_id, context_id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error removing data: {e}")
            self.conn.rollback()
            return False

    def subscribe(self, source_id: int, subscriber_id: int, context_id: int):
        try:
            self.cursor.execute("INSERT INTO subscriptions (source_id, subscriber_id, context_id) VALUES (?, ?, ?)", (source_id, subscriber_id, context_id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error subscribing: {e}")
            self.conn.rollback()
            return False

    def unsubscribe(self, subscription_id: int):
        try:
            self.cursor.execute("DELETE FROM subscriptions WHERE id = ?", (subscription_id,))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error unsubscribing: {e}")
            self.conn.rollback()
            return False

    def has_view_permission(self, user_id: int, context_id: int):
        try:
            self.cursor.execute("SELECT view_permission FROM permissions WHERE user_id = ? AND context_id = ?", (user_id, context_id))
            result = self.cursor.fetchone()
            return result is not None and result[0]
        except sqlite3.Error as e:
            print(f"Error checking view permission: {e}")
            return False

    def has_query_permission(self, user_id: int, context_id: int):
        try:
            self.cursor.execute("SELECT query_permission FROM permissions WHERE user_id = ? AND context_id = ?", (user_id, context_id))
            result = self.cursor.fetchone()
            return result is not None and result[0]
        except sqlite3.Error as e:
            print(f"Error checking query permission: {e}")
            return False

    def has_permission(self, user_id: int, context_id: int, view_permission: bool = True, query_permission: bool = True):
        return self.has_view_permission(user_id, context_id) if view_permission else True and \
               self.has_query_permission(user_id, context_id) if query_permission else True
