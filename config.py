# ==========================================
# إعدادات المشروع
# Configuration du projet
# ==========================================

import os

# ✅ مسارات المشروع
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
PHOTOS_DIR = os.path.join(DATA_DIR, 'photos')
DATABASE_PATH = os.path.join(DATA_DIR, 'beneficiaires.db')

# إنشاء المجلدات إذا لم تكن موجودة
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(PHOTOS_DIR, exist_ok=True)

# ✅ إعدادات الواجهة الرسومية
WINDOW_TITLE = "إدارة المستفيدين من المساكن الريفية - Gestion des Bénéficiaires"
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
BG_COLOR = "#f0f0f0"
PRIMARY_COLOR = "#2c3e50"
SECONDARY_COLOR = "#3498db"

# ✅ ألوان الأزرار
BTN_ADD_COLOR = "#27ae60"      # أخضر
BTN_EDIT_COLOR = "#3498db"     # أزرق
BTN_DELETE_COLOR = "#e74c3c"   # أحمر
BTN_SEARCH_COLOR = "#f39c12"   # برتقالي
BTN_EXPORT_COLOR = "#9b59b6"   # بنفسجي

# ✅ إعدادات قاعدة البيانات
DB_TIMEOUT = 10

# ✅ تنسيقات التاريخ
DATE_FORMAT = "%Y-%m-%d"
DISPLAY_DATE_FORMAT = "%d/%m/%Y"
