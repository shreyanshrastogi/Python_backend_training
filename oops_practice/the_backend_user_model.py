class User:
    def __init__(self, username: str, email: str):
        if not username:
            raise ValueError("no username")
        if not email:
            raise ValueError("no email")
        self.username = username
        self.email = email

    def get_profile(self) -> str:
        return f"User:{self.username} | Email: {self.email}"

    def __str__(self) -> str:
        return (
            "this class helps in storing user info and has a function get_profile too"
        )


def profile_getter() -> str:
    while True:
        username = input("username:")
        email = input("email:")
        try:
            user = User(username, email)
        except ValueError as e:
            print(e)
        else:
            return user.get_profile()


def main() -> None:
    print(profile_getter())
    ...


if __name__ == "__main__":
    main()
