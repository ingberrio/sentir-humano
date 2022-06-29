from django.views.generic import View
from django.conf import settings
import os
from django.template.loader import get_template
import customers
from customers.models import Invoice, Customer
from xhtml2pdf import pisa
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

class InvoicePdfView(View):

    def link_callback(self, uri, rel):
        """
        Convert HTML URIs to absolute system paths so xhtml2pdf can access those
        resources
        """
        # use short variable names
        sUrl = settings.STATIC_URL  # Typically /static/
        sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL  # Typically /static/media/
        mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

        # convert URIs to absolute system paths
        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri  # handle absolute uri (ie: http://some.tld/foo.png)

        # make sure that file exists
        if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
        return path

    def get(self, request, *args, **kwargs):
        response = ''
        response = HttpResponse(content_type='application/pdf')
        #response['Content-Disposition'] = 'attachment; filename="recibo.pdf"'
        try:
            template = get_template('admin/invoice.html')
            context = {
                'invoice': Invoice.objects.get(pk=self.kwargs['pk']),
                'comp': {'name': 'SENTIR HUMANO S.A.S', 'ruc': 'NIT 9011758345', 'address': 'CARRERA 13 17 40, ARMENIA, QUINDIO'},
                'icon': '{}{}'.format(settings.MEDIA_URL, 'logo.png')
            }
            html = template.render(context)
            pisaStatus = pisa.CreatePDF(
                html, dest=response,
                link_callback=self.link_callback
            )
            if pisaStatus.err:
                return HttpResponse('Tenemos un error <pre>' + html + '</pre>')
            return response
        except:
            pass
        return HttpResponseRedirect(reverse('customer:generatePDF')) 

class CustomerPdfView(View):

    def link_callback(self, uri, rel):
        """
        Convert HTML URIs to absolute system paths so xhtml2pdf can access those
        resources
        """
        # use short variable names
        sUrl = settings.STATIC_URL  # Typically /static/
        sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL  # Typically /static/media/
        mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

        # convert URIs to absolute system paths
        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri  # handle absolute uri (ie: http://some.tld/foo.png)

        # make sure that file exists
        if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
        return path

    def get(self, request, *args, **kwargs):
        response = ''
        response = HttpResponse(content_type='application/pdf')
        #response['Content-Disposition'] = 'attachment; filename="recibo.pdf"'
        try:
            template = get_template('admin/credential.html')
            context = {
                'customer': Customer.objects.get(pk=self.kwargs['pk']),
                'comp': {'name': 'SENTIR HUMANO S.A.S', 'ruc': 'NIT 9011758345', 'address': 'CARRERA 13 17 40, ARMENIA, QUINDIO'},
                'icon': '{}{}'.format(settings.MEDIA_URL, 'logo.png')
            }
            html = template.render(context)
            pisaStatus = pisa.CreatePDF(
                html, dest=response,
                link_callback=self.link_callback
            )
            if pisaStatus.err:
                return HttpResponse('Tenemos un error <pre>' + html + '</pre>')
            return response
        except:
            pass
        return HttpResponseRedirect(reverse('customer:credentialPDF')) 



