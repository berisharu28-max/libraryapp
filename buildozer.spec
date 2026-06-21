[app]
# (string) Title of your application
title = Library Management

# (string) Package name
package.name = libraryapp

# (string) Package domain (needed for android packaging)
package.domain = org.example

# (string) Source code directory
source.dir = .

# (list) Source files to include (Mene isme last me db jod diya hai)
source.include_exts = py, png, jpg, kv, atlas, db

# (string) Application version
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# =============================================================================
# Android specific configurations
# =============================================================================

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK directory (blank to use default)
# android.ndk = 25b

# (str) Android Build Tools version (blank to use default)
# android.build_tools_version = 33.0.0

# (bool) Use private storage for data
android.private_storage = True

# (bool) Accept SDK license without identifying manually
android.accept_sdk_license = True

# (list) The Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (list) Permissions
android.permissions = INTERNET

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
