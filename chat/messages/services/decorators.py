from django.shortcuts import redirect

from typing import Callable

from .exceptions import ChatExistsException


def except_bad_requests(func: Callable) -> Callable:
    def wrapper(request, *args, **kwargs) -> (redirect, Callable):
        try:
            result = func(request, *args, **kwargs)
        except ChatExistsException:
            return redirect('messages:chats')
        return result
    return wrapper