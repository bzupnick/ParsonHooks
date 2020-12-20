from json import loads
from src.models import Webhook
from django.http import JsonResponse, HttpResponseBadRequest


def router(req, **kwargs):
    if req.method == "POST":
        return create(req)
    else:
        return HttpResponseBadRequest()


def create(req):
    body = loads(req.body)
    name = body.get('name')
    if name:
        new_webhook = Webhook(name=name, user=req.user)
        new_webhook.save()
        return JsonResponse({'id': new_webhook.id})
    else:
        return HttpResponseBadRequest()
