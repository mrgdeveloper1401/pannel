from panel.settings import *
import os
from datetime import datetime

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": config("POSTDB_HOST", cast=str),
        "PASSWORD": config("POSTDB_PASSWORD", cast=str),
        "PORT": config("POSTDB_PORT", cast=int),
        "USER": config("POSTDB_USER", cast=str),
        "NAME": config("POSTDB_NAME", cast=str)
    }
}

ALLOWED_HOSTS = [
    "vpn-rayanhjt.kubarcloud.net"
]

INSTALLED_APPS += [
    "corsheaders"
]

MIDDLEWARE.insert(0, "corsheaders.middleware.CorsMiddleware")
MIDDLEWARE += [
    # 'csp.middleware.CSPMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

CORS_ALLOWED_ORIGINS = [
    "https://vpn-rayanhjt.kubarcloud.net"
]

MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/app/media/'

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
        "OPTIONS": {
            "location": MEDIA_ROOT,
            "base_url": MEDIA_URL,
        },
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

SECRET_KEY = config('SECRET_KEY', cast=str)

SIMPLE_JWT['SIGNING_KEY'] = SECRET_KEY

# CSP_DEFAULT_SRC = ["'self'"]  # فقط منابع از دامنه خودتان
# CSP_SCRIPT_SRC = ["'self'"]    # اسکریپت ها فقط از دامنه خودتان
# CSP_STYLE_SRC = ["'self'"]     # استایل ها فقط از دامنه خودتان
# CSP_IMG_SRC = ["'self'"]       # تصاویر فقط از دامنه خودتان
# CSP_FONT_SRC = ["'self'"]      # فونت ها فقط از دامنه خودتان

SESSION_COOKIE_SECURE = True  # ارسال کوکی‌های Session فقط از طریق HTTPS
CSRF_COOKIE_SECURE = True  # ارسال کوکی‌های CSRF فقط از طریق HTTPS
SECURE_SSL_REDIRECT = True  # ریدایرکت خودکار HTTP به HTTPS
SECURE_HSTS_SECONDS = 31536001  # فعال‌سازی HSTS به مدت 1 سال (در ثانیه)
SECURE_HSTS_PRELOAD = True  # افزودن سایت به لیست پیش‌بارگذاری HSTS مرورگرها
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # اعمال HSTS برای تمام ساب‌دامین‌ها
SECURE_CONTENT_TYPE_NOSNIFF = True  # جلوگیری از MIME Sniffing
SECURE_BROWSER_XSS_FILTER = True  # فعال‌سازی فیلتر XSS در مرورگرهای قدیمی
X_FRAME_OPTIONS = "SAMEORIGIN"  # جلوگیری از Clickjacking (فقط نمایش در iframe با منبع یکسان)
SECURE_REFERRER_POLICY = "strict-origin"  # کنترل اطلاعات ارسال شده در هدر Referer
USE_X_FORWARDED_HOST = True  # استفاده از هدر X-Forwarded-Host برای تشخیص دامنه
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")  # تشخیص صحیح HTTPS هنگام استفاده از پروکسی

log_dir = os.path.join(BASE_DIR / "general_log_django", datetime.now().strftime("%Y-%m-%d"))
os.makedirs(log_dir, exist_ok=True)
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "color": {
            "()": "colorlog.ColoredFormatter",
            "format": "%(log_color)s%(levelname)s %(reset)s%(asctime)s %(module)s %(process)d %(thread)d %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "filters": {
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "handlers": {
        "info_file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "formatter": "color",
            "filename": os.path.join(BASE_DIR / log_dir / "info_file.log")
        },
        "error_file": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "formatter": "color",
            "filename": os.path.join(BASE_DIR / log_dir / "error_file.log")
        },
        "warning_file": {
            "level": "WARN",
            "class": "logging.FileHandler",
            "formatter": "color",
            "filename": os.path.join(BASE_DIR / log_dir / "warning_file.log")
        },
        "critical_file": {
            "level": "CRITICAL",
            "class": "logging.FileHandler",
            "formatter": "color",
            "filename": os.path.join(BASE_DIR / log_dir / "critical_file.log")
        },
    },
    "loggers": {
        "django": {
            "handlers": ["info_file", "warning_file", "critical_file", "error_file"],
            "propagate": True,
        }
    }
}
