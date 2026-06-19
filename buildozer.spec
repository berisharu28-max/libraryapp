[app]
# (str) Title of your application
title = Library Management

# (str) Package name
package.name = libraryapp

# (str) Package domain (unique identifier prefix)
package.domain = org.example

# (str) Source code where the main.py is located
source.dir = .

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy,sqlite3

# (str) Supported orientation (landscape, portrait)
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 0

# (str) Supported source file extensions
source.include_exts = py,kv

# (str) Presplash and icon can be omitted for now

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.archs = armeabi-v7a
android.api = 33
android.minapi = 21
android.enable_androidx = True

# Uncomment if you need Android permissions
# android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
