import subprocess

CLI_NAME = "repl"


def create_pipe():
    pipe = subprocess.Popen(
            [f"./{CLI_NAME}"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
            )
    return pipe

def test_one_insert():
    pipe = create_pipe()
    commands = (
            "insert 1 user2 email3\n"
            "select\n"
            ".exit\n"
            )
    output, err = pipe.communicate(input=commands)
    correct_output: str = "db > Executed.\n(1,user2,email3)"

pipe = subprocess.Popen(
        ["./repl"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
        )
commands = (
    "insert 1 user1 email1\n"
    "insert 2 user2 email2\n"
    "select\n"
    ".exit\n" # Assuming your REPL has an exit command
)

# Send them all at once
output, errors = pipe.communicate(input=commands)

print("--- REPL OUTPUT ---")
print(output)


