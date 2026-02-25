class User:
    user_registered = 0

    def __init__(self, username: str, email: str):
        if not username:
            raise ValueError("no username")
        if not email:
            raise ValueError("no email")
        self.username = username
        self.email = email
        User.user_registered += 1
        self.user_registered = 1

    def get_profile(self) -> str:
        return f"User:{self.username} | Email: {self.email}"

    def __str__(self) -> str:
        return (
            "this class helps in storing user info and has a function get_profile too"
        )


def profile_getter() -> User:
    while True:
        username = input("username:")
        email = input("email:")
        try:
            return User(username, email)
        except ValueError as e:
            print(e)


def main() -> None:
    user_1 = profile_getter()
    user_2 = profile_getter()
    user_3 = profile_getter()
    print(
        ("total user registered: {} ,user_1 registered:{}").format(
            User.user_registered, user_1.user_registered
        )
    )


if __name__ == "__main__":
    main()
