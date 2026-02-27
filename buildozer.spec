[app]
title = WorkLog
package.name = worklog
package.domain = com.samjinwt

source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,webp,json,txt,ini,ttf,otf,atlas
# 필요하면 제외
# source.exclude_dirs = tests,bin,build,.git,.github,__pycache__
# source.exclude_patterns = */__pycache__/*,*.pyc,*.pyo

version = 1.0
orientation = portrait
fullscreen = 0

# 네 앱에서 requests/notion-client 쓰면 여기 추가해야 함
# requirements = python3,kivy,requests,notion-client
requirements = python3,kivy

# entrypoint 기본은 main.py. 파일명이 다르면 꼭 맞춰라.
entrypoint = main.py

# 로그 레벨(0~2)
log_level = 2


[buildozer]
log_level = 2
warn_on_root = 1


[android]
# 타겟/최소 API
android.api = 34
android.minapi = 24

# ✅ Build-Tools 고정 (RC 안 잡게)
android.build_tools_version = 34.0.0

# ✅ 아키텍처
android.archs = arm64-v8a

# ✅ 권한
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# ✅ p4a가 SDK 업데이트/자동설치 못하게(가장 중요)
p4a.extra_args = --no-sdk-update

# ✅ (권장) 안드로이드X
android.enable_androidx = True

# ✅ (권장) gradle 안정화 (CI에서 자주 필요)
android.gradle_options = -Xmx4g -Dorg.gradle.daemon=false -Dorg.gradle.jvmargs="-Xmx4g -XX:MaxMetaspaceSize=1g"
android.add_gradle_repositories = mavenCentral()

# ✅ (선택) 릴리즈/디버그 설정(필요 시)
# android.debuggable = 1

# ✅ (선택) NDK를 고정하고 싶으면 (workflow에서 NDK 설치할 때랑 맞춰야 함)
# android.ndk = 25b
