from database import CreateDB
from hash import GetHash


class Submit:
    def __init__(self, *args: str) -> None:
        CreateDB.db_path(r"login_data_base.db")
        self.table: str = "login"
        self.db: CreateDB = CreateDB(
            self.table, primary_key="username", username="TEXT", password="TEXT"
        )
        self.username: str = args[0]
        self.password: str = args[1]
        self.chk: tuple = self.db.check(self.table, username=self.username)

    @classmethod
    def sign_up(cls, user_, pass_):
        page: Submit = cls(user_, pass_)
        try:
            assert len(page.chk) == 0
        except:
            page.db.log.warning(f'Try to create "{user_}" again')
            print(f"Username has taken...!")
            return 0
        else:
            password = GetHash.get_hash_256(page.password)[0]
            page.db.add_record(user_, password)
            page.db.log.debug(f'Account "{user_}" created.')
            print(f"Sign up successfully")
            return 1

    @classmethod
    def sign_in(cls, user_, pass_):
        password = GetHash.get_hash_256(pass_)[0]
        page: Submit = cls(user_, pass_)
        try:
            assert page.chk[0] == user_
        except:
            page.db.log.error(f"Account '{user_}' not found please sign up first")
            print(f"Account '{user_}' not found please sign up first")
            return 0
        else:
            if password == page.chk[1]:
                page.db.log.debug(f" '{user_}' Signed in")
                print(f" Signed in successfully")
                return 1
            else:
                page.db.log.warning(f'"{user_}" entered worng password')
                print("username or password incorrect!!!")
                return 2


if __name__ == "__main__":
    print(Submit.sign_in("ami5n", "1423"))
