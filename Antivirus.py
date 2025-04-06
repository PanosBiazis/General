import os
import hashlib
import re

# Expanded list of potentially malicious patterns
MALICIOUS_PATTERNS = [# Malicious command execution
    # System command execution
    "os.system",
    "subprocess.Popen",
    "subprocess.run",
    "subprocess.call",
    "eval(",
    "exec(",
    "compile(",

    # Dangerous file operations
    "open(",
    "shutil.rmtree",
    "os.remove",
    "os.rmdir",

    # Network operations (possible exfiltration or remote control)
    "socket.socket",
    "requests.get",
    "requests.post",
    "urllib.request.urlopen",
    "http.client",

    # Base64 encoding/decoding (used for obfuscation)
    "base64.b64encode",
    "base64.b64decode",

    # Dynamic imports (used for hiding malicious modules)
    "importlib.import_module",
    "__import__(",

    # Suspicious threading or process creation
    "threading.Thread",
    "multiprocessing.Process",

    # Persistence mechanisms
    "os.mkdir('.hidden')",
    "os.path.exists('.hidden')",
    "winreg.OpenKey",
    "winreg.SetValueEx",

    # Potentially obfuscated code patterns
    "exec(base64.b64decode",
    "exec(zlib.decompress",
    "exec(gzip.decompress",

    # Credential stealing or keylogging
    "pynput.keyboard.Listener",
    "getpass.getpass",
    "pyautogui",

    # Encryption for data ransom
    "cryptography.fernet.Fernet",
    "Crypto.Cipher",
    "rsa.encrypt",
    "rsa.decrypt",

    # Malicious external calls
    "wget",
    "curl",
    "powershell",
    "cmd.exe",

    # Dangerous Windows-specific calls
    "ctypes.windll",
    "ctypes.WinDLL",
    "os.popen",
    "os.startfile",
    "wmic"
]

# Function to calculate file hash
def calculate_hash(file_path):
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

# Function to scan a file for malicious patterns
def scan_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            for pattern in MALICIOUS_PATTERNS:
                if re.search(re.escape(pattern), content):
                    return True, pattern
    except Exception as e:
        print(f"Could not scan file {file_path}: {e}")
    return False, None

# Main scan function for directories
def scan_directory(directory):
    print(f"Scanning directory: {directory}")
    malicious_files = []
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            is_malicious, pattern = scan_file(file_path)
            
            if is_malicious:
                malicious_files.append((file_path, pattern))
                print(f"[!] Malicious pattern found in {file_path}: {pattern}")
    
    return malicious_files

# Main execution
if __name__ == "__main__":
    scan_dir = input("Enter the directory to scan: ").strip()
    if os.path.exists(scan_dir):
        results = scan_directory(scan_dir)
        if results:
            print("\n[!] Malicious files detected:")
            for file, pattern in results:
                print(f"- {file} (Pattern: {pattern})")
        else:
            print("\nNo malicious files detected.")
    else:
        print("Directory does not exist!")
