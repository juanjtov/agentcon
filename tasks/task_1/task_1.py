import helpers
import flask, together, textwrap, json, os, sys, argparse
import dotenv

dotenv.load_dotenv()


def task_1():
    """
    Goal:
      Ensure the environment is set up correctly and you can run Python code.

    Instructions:
    - Install Python and dependencies
    - Run a script that generates a very cool looking hello world message
    - Save the output to outputs/task_1.txt.
    """

    # Fancy sophisticated hello world message
    fancy_hello = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║     ██╗  ██╗███████╗██╗     ██╗      ██████╗     ██╗    ██╗ ██████╗ ██████╗  ║
║     ██║  ██║██╔════╝██║     ██║     ██╔═══██╗    ██║    ██║██╔═══██╗██╔══██╗ ║
║     ███████║█████╗  ██║     ██║     ██║   ██║    ██║ █╗ ██║██║   ██║██████╔╝ ║
║     ██╔══██║██╔══╝  ██║     ██║     ██║   ██║    ██║███╗██║██║   ██║██╔══██╗ ║
║     ██║  ██║███████╗███████╗███████╗╚██████╔╝    ╚███╔███╔╝╚██████╔╝██║  ██║ ║
║     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝ ╚═════╝      ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝ ║
║                                                                              ║
║                          ██╗     ██████╗ ██╗                                 ║
║                          ██║     ██╔══██╗██║                                 ║
║                          ██║     ██║  ██║██║                                 ║
║                          ╚═╝     ██║  ██║╚═╝                                 ║
║                          ██╗     ██████╔╝██╗                                 ║
║                          ╚═╝     ╚═════╝ ╚═╝                                 ║
║                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║    ✦ ═══════════════════════════════════════════════════════════════════ ✦   ║
║                                                                              ║
║         "The beginning of wisdom is the definition of terms." - Socrates     ║
║                                                                              ║
║              ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░           ║
║              ░  Environment initialized. All systems operational.  ░           ║
║              ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░           ║
║                                                                              ║
║    ✦ ═══════════════════════════════════════════════════════════════════ ✦   ║
║                                                                              ║
║                        ┌─────────────────────────┐                           ║
║                        │   ★ Task 1 Complete ★   │                           ║
║                        └─────────────────────────┘                           ║
║                                                                              ║
║              Python: ✓   Dependencies: ✓   Ready to Build: ✓                 ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

    # Print to console
    print(fancy_hello)

    # Ensure outputs directory exists
    os.makedirs("outputs", exist_ok=True)

    # Save to file
    with open("outputs/task_1.txt", "w") as f:
        f.write(fancy_hello)

    return fancy_hello
