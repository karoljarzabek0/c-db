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
    correct_output: str = "db > Executed.\ndb > (1, user2, email3)\nExecuted.\ndb > "
    if output == correct_output:
        print("Test 1 passed")
    else:
        print("Test 1 failed")
        print(f"Output:\n{output}\nExpected:\n{correct_output}")

def test_long_insert():
    long_username = "a" * 32
    long_email = "a" * 255
    pipe = create_pipe()
    commands = (
            f"insert 1 {long_username} {long_email}\n"
            "select\n"
            ".exit\n"
            )
    output, err = pipe.communicate(input=commands)
    correct_output: str = f"db > Executed.\ndb > (1, {long_username}, {long_email})\nExecuted.\ndb > "
    if output == correct_output:
        print("Test 2 passed")
    else:
        print("Test 2 failed")
        print(f"Output:\n{output}\nExpected:\n{correct_output}")

def test_batch_insert():
    long_username = "a" * 32
    long_email = "a" * 255
    pipe = create_pipe()

    command = ""
    for i in range(150000):
        command += f"insert {i} user{i} email{i}\n"
    
    command += "select\n.exit\n"

    commands = (
            command
            )
    output, err = pipe.communicate(input=commands)
    correct_output: str = f"Lack of correct case"
    if output == correct_output:
        print("Test 3 passed")
    else:
        print("Test 3 failed")
        print(f"Stderr: {err}")
        print(f"Output:\n{output}\nExpected:\n{correct_output}")



if __name__ == "__main__":
    test_one_insert()
    test_long_insert()
    test_batch_insert()
