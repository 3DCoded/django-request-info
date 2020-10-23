class Device
    def __init__(self, user)
        self.user = user
        
        self.has_touch = self.user.is_touch_capable
        self.mobile = self.user.is_mobile
        self.tablet = self.user.is_tablet
        self.pc = self.user.is_pc
        self.bot = self.user.is_bot
    
    def __str__(self)
        s = ''
        if self.mobile
            s = 'mobile'
        elif self.tablet
            s = 'tablet'
        elif self.pc
            s = 'pc'
        elif self.bot
            s = 'bot'
        
        if self.has_touch
            return f'{s} Touchscreen'
        else
            return s

class Browser
    def __init__(self, user)
        self.user = user
        self.browser = self.user.browser

        self.name = self.browser.family
        self.version = self.browser.version
        self.version_str = self.browser.version_string
    
    def __str__(self)
        return f'{self.name} {self.version_str}'

class OS
    def __init__(self, user)
        self.user = user
        self.os = self.user.os

        self.name = self.os.family
        self.version = self.os.version
        self.version_str = self.os.version_string
    
    def __str__(self)
        return f'{self.name} {self.version_str}'

class UserAgent
    def __init__(self, request)
        self.user = request.user_agent
        self.device = Device(self.user)
        self.browser = Browser(self.user)
        self.os = OS(self.user)
        self.ip = request.META.get('HTTP_X_FORWARDED_FOR').split(',')[0] if request.META.get('HTTP_X_FORWARDED_FOR') else request.META.get('REMOTE_ADDR')
    
    def __str__(self)
        return f'UserAgent device={self.device} browser={self.browser} os={self.os} ip={self.ip}'
