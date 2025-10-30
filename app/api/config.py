import subprocess
import sys

def install_github_package(repo_url: str, target_dir: str = None):
    """
    Instaluje pakiet z GitHub wraz z zależnościami.
    Jeśli podasz target_dir, instaluje do wskazanego folderu.
    """
    command = [sys.executable, "-m", "pip", "install", f"git+{repo_url}"]
    
    if target_dir:
        command += ["--target", target_dir]
    
    subprocess.check_call(command)