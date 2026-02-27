[app]
title = WorkLog
package.name = worklog
package.domain = com.samjinwt

source.dir = .
source.include_exts = py,png,jpg,kv

version = 1.0
orientation = portrait
fullscreen = 0

requirements = python3,kivy

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.api = 34
android.minapi = 24
android.build_tools_version = 34.0.0
android.archs = arm64-v8a
android.permissions = INTERNET
p4a.extra_args = --no-sdk-update
