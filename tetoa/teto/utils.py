points = [
        {"title":"Главная страница","url_name" : "Home"},
       # {"title":"Продукты в наличие","url_name" : "info"},
        {"title":"Добавление продукта","url_name" : "add_prod"},
        {"title":"Связь с нами","url_name" : "contact"},
        #{"title":"Авторизация","url_name" : "login"},
        #{"title":"Регистрация","url_name" : "register"},
        #{"title":"Пользователи","url_name" : "userrs"},
          ]

class DataMixin:
    def get_user_context(self,**kwargs):
        context = kwargs
        context["points"] = points
        return context