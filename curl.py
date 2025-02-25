class Url:
    MAIN_SITE_URL = 'https://stellarburgers.nomoreparties.site'
    LOGIN_URL = f'{MAIN_SITE_URL}/login'
    PERSONAL_ACCOUNT_URL = f'{MAIN_SITE_URL}/account/profile'
    PASSWORD_RECOVERY_URL = f'{MAIN_SITE_URL}/forgot-password'
    RESET_PASSWORD_URL = f'{MAIN_SITE_URL}/reset-password'
    ORDER_FEED_URL = f'{MAIN_SITE_URL}/feed'
    ORDER_HISTORY_URL = f'{MAIN_SITE_URL}/account/order-history'

    CREATE_USER = '/api/auth/register'
    LOGIN_USER = '/api/auth/login'
    DELETE_USER = '/api/auth/user'




