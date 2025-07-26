def safe_print_integer(value):
    try:
        print("{:d}".format(value))  # محاولة الطباعة كعدد صحيح
        return True
    except (ValueError, TypeError):  # إذا لم يكن value يصلح لـ :d
        return False
