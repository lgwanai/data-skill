import os
import sys
import json
import threading
import http.server
import socketserver
import socket
import argparse

def find_free_port(start_port=8000, max_port=8100):
    for port in range(start_port, max_port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(('', port))
                return port
            except OSError:
                continue
    raise IOError("No free ports found")

def get_server_info_file():
    """Get the path to the server info file."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_dir, 'tmp', '.server_info')

def check_server_running():
    """Check if the server is already running."""
    info_file = get_server_info_file()
    if not os.path.exists(info_file):
        return None
        
    try:
        with open(info_file, 'r') as f:
            info = json.load(f)
            port = info.get('port')
            
            # Simple check if port is in use
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                result = s.connect_ex(('127.0.0.1', port))
                if result == 0:
                    return port
    except Exception:
        pass
        
    # If file exists but server is not running or file is corrupted, remove it
    try:
        os.remove(info_file)
    except:
        pass
    return None

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()
        
    def log_message(self, format, *args):
        # Suppress logging to keep console clean
        pass

def run_server_forever(port, base_dir):
    """Run the server synchronously."""
    os.chdir(base_dir)
    # Save server info
    os.makedirs(os.path.join(base_dir, 'tmp'), exist_ok=True)
    with open(get_server_info_file(), 'w') as f:
        json.dump({'port': port}, f)
        
    handler = CustomHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            try:
                os.remove(get_server_info_file())
            except:
                pass

def ensure_server_running():
    """
    Ensures a lightweight HTTP server is running to serve the generated charts.
    Returns the base URL.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    port = check_server_running()
    
    if not port:
        import subprocess
        port = find_free_port()
        
        # Start this very script as a background process using the --daemon flag
        cmd = [sys.executable, os.path.abspath(__file__), "--daemon", "--port", str(port)]
        
        if sys.platform == 'win32':
            subprocess.Popen(cmd, 
                             creationflags=subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.DETACHED_PROCESS,
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            subprocess.Popen(cmd, 
                             start_new_session=True,
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                             
        # Wait a moment for it to start and write the info file
        import time
        time.sleep(0.5)
        
    return f"http://127.0.0.1:{port}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Data Skill local HTTP server")
    parser.add_argument("--daemon", action="store_true", help="Run as daemon")
    parser.add_argument("--port", type=int, help="Port to run on")
    
    args = parser.parse_args()
    
    if args.daemon and args.port:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        run_server_forever(args.port, base_dir)
    else:
        url = ensure_server_running()
        print(f"Server is running at {url}")