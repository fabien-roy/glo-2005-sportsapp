from app import conn
from app.practice_centers.exceptions import PracticeCenterNotFoundException
from app.practice_centers.models import PracticeCenter
from app.practice_centers.repositories import PracticeCenterRepository


class MySQLPracticeCenterRepository(PracticeCenterRepository):
    table_name = 'practice_centers'

    id_col = 'id'
    name_col = 'name'
    email_col = 'email'
    web_site_col = 'web_site'
    phone_number_col = 'phone_number'

    def get_all(self):
        all_practice_centers = []

        try:
            with conn.cursor() as cur:
                cur.execute('SELECT ' + self.id_col + ', ' + self.name_col + ', ' + self.email_col + ', ' +
                            self.web_site_col + ', ' + self.phone_number_col +
                            ' FROM ' + self.table_name +
                            ' ORDER BY ' + self.name_col + ';')

                for practice_center_cur in cur.fetchall():
                    practice_center = PracticeCenter(practice_center_cur[self.id_col],
                                                     practice_center_cur[self.name_col],
                                                     practice_center_cur[self.email_col],
                                                     practice_center_cur[self.web_site_col],
                                                     practice_center_cur[self.phone_number_col])
                    all_practice_centers.append(practice_center)
        finally:
            cur.close()

        return all_practice_centers

    def get(self, practice_center_id):
        practice_center = None

        try:
            with conn.cursor() as cur:
                sql = ('SELECT ' + self.id_col + ', ' + self.name_col + ', ' + self.email_col + ', ' +
                       self.web_site_col + ', ' + self.phone_number_col +
                       ' FROM ' + self.table_name +
                       ' WHERE ' + self.id_col + ' = %s;')
                cur.execute(sql, practice_center_id)

                # TODO : Use fetchone (causes integer error)
                for practice_center_cur in cur.fetchall():
                    practice_center = PracticeCenter(practice_center_cur[self.id_col],
                                                     practice_center_cur[self.name_col],
                                                     practice_center_cur[self.email_col],
                                                     practice_center_cur[self.web_site_col],
                                                     practice_center_cur[self.phone_number_col])
        finally:
            cur.close()

        if practice_center is None:
            raise PracticeCenterNotFoundException

        return practice_center

    def add(self, practice_center):
        try:
            with conn.cursor() as cur:
                sql = ('INSERT INTO ' + self.table_name +
                       ' (' + self.id_col + ', ' + self.name_col + ', ' + self.email_col + ', ' + self.web_site_col +
                       ', ' + self.phone_number_col + ')' +
                       ' VALUES (%s, %s, %s, %s, %s);')
                cur.execute(sql, (practice_center.id, practice_center.name, practice_center.email,
                                  practice_center.web_site, practice_center.phone_number))

                conn.commit()
        finally:
            cur.close()
