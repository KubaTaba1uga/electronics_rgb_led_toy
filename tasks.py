###############################################
#                Imports                      #
###############################################
import os
import subprocess

from invoke import task

###############################################
#                Public API                   #
###############################################
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
KICAD_SRC_PATH = os.path.join(ROOT_PATH, "kicad_src")
OPENSCAD_SRC_PATH = os.path.join(ROOT_PATH, "openscad_src")
BUILD_PATH = os.path.join(ROOT_PATH, "build")
OPENSCAD_LIBS_PATH = os.path.join(BUILD_PATH, "openscad_libs")


@task
def clean(c, bytecode=False, extra=""):
    """
    Clean up build and temporary files.

    This task removes the specified patterns of files and directories,
    including build artifacts, temporary files, and optionally Python
    bytecode files.

    Args:
        bytecode (bool, optional): If True, also removes Python bytecode files (.pyc). Defaults to False.
        extra (str, optional): Additional pattern to remove. Defaults to "".

    Usage:
        inv clean
        inv clean --bytecode
        inv clean --extra='**/*.log'
    """
    patterns = ["build/*", "**/*~", "**/#*", "*~", "#*", "**/*.stl"]

    if bytecode:
        patterns.append("**/*.pyc")
    if extra:
        patterns.append(extra)

    for pattern in patterns:
        _pr_info("Removing pattern {}".format(pattern))
        c.run("rm -vrf {}".format(pattern))


@task
def build(c):
    """
    Build repo.

    Usage:
        inv build
    """

    raise NotImplementedError()


@task
def open_kicad(c):
    """
    Open kicad project.

    Usage:
        inv open
    """
    raise NotImplementedError()


@task
def open_openscad(
    c, file_path=os.path.join(OPENSCAD_SRC_PATH, "enclosure_part_1.scad")
):
    """
    Open openscad project.

    Usage:
        inv open-openscad
    """
    CC = "openscad"
    _write_libs_path_to_envs()

    if not os.path.isfile(file_path):
        _pr_error(f"File {file_path} does not exist!")
        return

    if _get_file_extension(file_path) != ".scad":
        _pr_error(f"File {file_path} is not an OpenSCAD file!")
        return

    if not _command_exists(CC):
        _pr_error(f"{CC} needs to be installed!")
        return

    _pr_info(f"Opening {file_path} in OpenSCAD")

    command = f"{CC} {file_path}"
    c.run(command)


@task
def download_deps(c):
    """
    Download all dependencies required to build the project.

    Usage:
        inv download-deps
    """
    _download_bosl2(c)


def _download_bosl2(c):
    _pr_info("Downloading BOSL2 library ...")
    if not _command_exists("git"):
        _pr_error("Git is not installed or not available in the PATH.")
        return

    if not os.path.exists(OPENSCAD_LIBS_PATH):
        os.makedirs(OPENSCAD_LIBS_PATH)

    repo_url = "https://github.com/BelfrySCAD/BOSL2.git"
    clone_command = f"git clone {repo_url} {os.path.join(OPENSCAD_LIBS_PATH, 'BOSL2')}"
    try:
        # Clone the repository and checkout the specified commit
        c.run(clone_command)
        _pr_info("Repository cloned successfully.")
    except Exception as e:
        _pr_error(f"Failed to download BOSL2 library: {str(e)}")


def _write_libs_path_to_envs():
    os.environ["OPENSCADPATH"] = OPENSCAD_LIBS_PATH


###############################################
#                Private API                   #
###############################################
def _get_file_extension(file_path):
    _, file_extension = os.path.splitext(file_path)
    return file_extension


def _command_exists(command):
    try:
        # Attempt to run the command with '--version' or any other flag that doesn't change system state
        subprocess.run(
            [command, "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        return True
    except FileNotFoundError:
        return False
    except subprocess.CalledProcessError:
        # The command exists but returned an error
        return True
    except Exception:
        # Catch any other exceptions
        return False


def _cut_path_to_directory(full_path, target_directory):
    """
    Cuts the path up to the specified target directory.

    :param full_path: The full path to be cut.
    :param target_directory: The directory up to which the path should be cut.
    :return: The cut path if the target directory is found, otherwise raises ValueError.
    """
    parts = full_path.split(os.sep)

    target_index = parts.index(target_directory)
    return os.sep.join(parts[: target_index + 1])


def _pr_info(message: str):
    """
    Print an informational message in blue color.

    Args:
        message (str): The message to print.

    Usage:
        pr_info("This is an info message.")
    """
    print(f"\033[94m[INFO] {message}\033[0m")


def _pr_warn(message: str):
    """
    Print a warning message in yellow color.

    Args:
        message (str): The message to print.

    Usage:
        pr_warn("This is a warning message.")
    """
    print(f"\033[93m[WARN] {message}\033[0m")


def _pr_debug(message: str):
    """
    Print a debug message in cyan color.

    Args:
        message (str): The message to print.

    Usage:
        pr_debug("This is a debug message.")
    """
    print(f"\033[96m[DEBUG] {message}\033[0m")


def _pr_error(message: str):
    """
    Print an error message in red color.

    Args:
        message (str): The message to print.

    Usage:
        pr_error("This is an error message.")
    """
    print(f"\033[91m[ERROR] {message}\033[0m")


if __name__ == "__main__":
    _write_libs_path_to_envs()
