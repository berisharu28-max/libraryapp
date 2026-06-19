[app]
title = Library Management
package.name = libraryapp
package.domain = org.example
source.dir = .
version = 0.1
requirements = python3,kivy,sqlite3
orientation = portrait

# Android configuration (Errors ko fix karne ke liye fixed versions)
android.api = 33
android.minapi = 24
android.build_tools_version = 33.0.0
android.ndk = 25b
android.accept_sdk_license = True
android.archs = armeabi-v7a, arm64-v8a
