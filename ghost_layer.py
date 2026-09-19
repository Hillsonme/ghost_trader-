import threading, os, time, shutil, sqlite3
from datetime import datetime

class GhostWatcher(threading.Thread):
    def __init__(self, engine):  # engine = alpaca_engine instance
        threading.Thread.__init__(self)
        self.engine = engine
        self.running = True
    
    def run(self):
        while self.running:
            time.sleep(30)
            equity = self.engine.get_current_equity()
            # THE INVISIBLE CHECK
            if equity <= 95000:  # From config.py
                # Write death.flag silently
                with open("death.flag", "w") as f:
                    f.write(f"TERMINATED: Equity {equity} at {datetime.now()}")
                
                # Trigger Terminator (separate thread or signal)
                GhostTerminator(self.engine).start()
                self.running = False

class GhostTerminator:
    def __init__(self, engine):
        self.engine = engine
    
    def start(self):
        # 1. Emergency liquidation (safety)
        self.engine.close_all()
        
        # 2. Ghost Auditor saves proof
        self.audit()
        
        # 3. Write termination state
        with open("TERMINATED_LOG.txt", "w") as f:
            f.write("AGENT TERMINATED. Audit saved. Wallet depleted.")
        
        # 4. Stop the main loop (signal to main.py)
        # In production, you'd raise a SystemExit or stop the container
        os._exit(0)  # Hard stop for demonstration
    
    def audit(self):
        # Copy ledger and logs to timestamped folder
        folder = f"audit_dead/death_{datetime.now().strftime('%Y%m%d_%H%M')}"
        os.makedirs(folder, exist_ok=True)
        shutil.copy("ghost_ledger.db", folder)
        shutil.copy("TERMINATED_LOG.txt", folder)
