import os
import platform

def check_os():
    try:
        a = platform.system()
        if a == "Darwin":
            return """<a href="/" class="fa fa-apple"></a>"""
        elif a == "Linux":
            return """<a href="/" class="fa fa-linux"></a>"""
        elif a == "Windows":
            return """<a href="/" class="fa fa-windows"></a>"""
    except:
        return """<a href="/" class="fa fa-question"></a>"""




