# Modules Project

A GUI application built with Python and Tkinter that provides various utility modules.

## Quick Start

### Running with the run.sh Script

To run this project, use the provided shell script:

1. **Make the script executable** (first time only):
   ```bash
   chmod +x run.sh
   ```

2. **Run the script**:
   ```bash
   ./run.sh
   ```

Alternatively, run the script directly without making it executable:
```bash
bash run.sh
```

### What the run.sh Script Does

The `run.sh` script automates the setup and startup process:
- Creates a virtual environment (`.venv`) if it doesn't exist
- Activates the virtual environment
- Installs packages from `requirements.txt` (if available)
- Launches the application by running `run.py`

### Manual Setup (Alternative)

If you prefer to set up manually:

1. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   ```

2. Activate it:
   ```bash
   source .venv/bin/activate
   ```

3. Install dependencies (if `requirements.txt` exists):
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python3 run.py
   ```

## Project Structure

- `Main_Module.py` - Main GUI application launcher
- `run.py` - Entry point script for the application
- `run.sh` - Bash script for automated setup and execution
- Additional modules for various utilities

## Requirements

- Python 3.6+
- Tkinter (usually included with Python)
- Any packages listed in `requirements.txt`

## License

See LICENSE file for details.
