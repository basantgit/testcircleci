import subprocess
import sys

def test_demo_script_runs_successfully():
    # Run the script as a subprocess
    result = subprocess.run(
        [sys.executable, "main.py"],
        capture_output=True,
        text=True
    )

    # Script should exit with status 0
    assert result.returncode == 0, f"Script failed. Output:\n{result.stdout}\nErrors:\n{result.stderr}"

    # Check expected printed output
    assert "Computation result: 4" in result.stdout
    assert "Test passed!" in result.stdout
