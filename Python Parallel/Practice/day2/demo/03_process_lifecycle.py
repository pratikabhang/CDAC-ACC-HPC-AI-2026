"""
Demo: Process Lifecycle (Spawn, Name, Daemon, Kill, Subclass)
"""
import multiprocessing
import time
import os

# -----------------------------------------------------------------------------
# Module-level worker functions (Required for macOS 'spawn' start method)
# -----------------------------------------------------------------------------

def print_name():
    """Prints the process name and PID."""
    name = multiprocessing.current_process().name
    pid = os.getpid()
    print(f"[{name}] Running with PID {pid}")

def daemon_worker():
    """A background process that runs until main exits."""
    name = multiprocessing.current_process().name
    while True:
        print(f"[{name}] Daemon is ticking...")
        time.sleep(0.5)

def long_running_task():
    """A long-running task to demonstrate termination."""
    name = multiprocessing.current_process().name
    print(f"[{name}] Starting long running task...")
    try:
        while True:
            time.sleep(0.2)
    except KeyboardInterrupt:
        pass

class MyCustomProcess(multiprocessing.Process):
    """A custom process created by subclassing multiprocessing.Process."""
    
    def __init__(self, name):
        super().__init__(name=name)
        
    def run(self):
        # This method is executed when start() is called
        pid = os.getpid()
        print(f"[{self.name}] Custom process running with PID {pid}")

# -----------------------------------------------------------------------------
# Demo execution functions
# -----------------------------------------------------------------------------

def demo_spawn_and_name():
    print("--- Demo: Spawn and Name ---")
    processes = []
    
    # Create 3 named processes
    for i in range(1, 4):
        p = multiprocessing.Process(target=print_name, name=f"Worker-{i}")
        processes.append(p)
        p.start()
        
    # Wait for all processes to complete
    for p in processes:
        p.join()
        
    print("Done.\n")

def demo_daemon_process():
    print("--- Demo: Daemon Process ---")
    p = multiprocessing.Process(target=daemon_worker, name="Daemon-1", daemon=True)
    p.start()
    
    # Main process sleeps for a short time, then exits.
    # The daemon will be killed automatically.
    print("[Main] Sleeping for 2 seconds...")
    time.sleep(2)
    print("[Main] Exiting! Daemon will die automatically.\n")

def demo_kill_process():
    print("--- Demo: Terminate Process ---")
    p = multiprocessing.Process(target=long_running_task, name="TargetProc")
    p.start()
    
    time.sleep(1)
    
    print(f"[{p.name}] is_alive() -> {p.is_alive()}")
    print("[Main] Terminating the process...")
    p.terminate()
    p.join()
    
    print(f"[{p.name}] is_alive() -> {p.is_alive()}")
    print(f"[{p.name}] Exit code -> {p.exitcode}\n")

def demo_process_subclass():
    print("--- Demo: Subclassing Process ---")
    p = MyCustomProcess("Subclass-Worker")
    p.start()
    p.join()
    print("Done.\n")

if __name__ == '__main__':
    # Uncomment the function you want to test
    demo_spawn_and_name()
    # demo_daemon_process()
    # demo_kill_process()
    # demo_process_subclass()
