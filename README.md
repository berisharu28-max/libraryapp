# LibraryApp

This is a Kivy-based library management app meant for desktop and Android.

## Android build steps

1. Install WSL or use a Linux environment.
2. Install Python 3 and dependencies.
3. Install Buildozer:
   ```bash
   pip install buildozer
   sudo apt update
   sudo apt install -y build-essential git python3-pip python3-venv
   ```
4. In the project folder, run:
   ```bash
   buildozer init
   ```
   (If you already have `buildozer.spec`, skip this.)
5. Build the APK:
   ```bash
   buildozer android debug
   ```
6. Deploy to a connected Android device:
   ```bash
   buildozer android debug deploy run
   ```

## Notes

- The app stores its SQLite database in `App.user_data_dir`, so it works on Android storage.
- Keep `main.py` and `library.kv` together in the project root.
