from django.utils import timezone
from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView
from .models import Event, EventDetail
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .forms import SubscribeForm
from datetime import datetime

# Create your views here.
class Data(ListView):
	model=Event
	template_name="list1.html"
	
	def get_context_data(self,**kwargs):
		context=super().get_context_data(**kwargs)
		return context
	
	def get_queryset(self):
		queryset = Event.objects.all()
		category = self.request.GET.get('category' or None)
		dept=self.request.GET.get('department' or None)

		if dept:
			queryset = Event.objects.filter(dept__iexact=dept)

		if category:
			queryset = Event.objects.filter(category__iexact=category)

		queryset = queryset.order_by("id1")
		return queryset;

class Details(DetailView):
	model=Event
	template_name="detail.html"

	def get_context_data(self,**kwargs):
		context=super().get_context_data(**kwargs)
		pk=self.kwargs['pk']
		obj = get_object_or_404(Event,pk=pk)
		print(context)
		return context

class subscribe(FormView):
	model=EventDetail
	form_class=SubscribeForm
	template_name="newsletter.html"


	def post(self,request,*args,**kwargs):
		print(kwargs['pk'])
		if request.method == 'POST': # If the form has been submitted...
			form = SubscribeForm(request.POST or None) # A form bound to the POST data
			if form.is_valid(): # All validation rules pass
				form.save()
		else:
			form= SubscribeForm() # An unbound form
		return render(self.request, 'newsletter.html', {'form': form})

from django_cron import CronJobBase, Schedule
import time
import email
import smtplib
import imaplib
import mailparser
import sqlite3
from datetime import datetime as dt

class reademail(CronJobBase):
    RUN_EVERY_MINS = 120 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'event.reademail'    # a unique code

    def do(self):
        conn=sqlite3.connect('../db.sqlite3')
        crs=conn.cursor()
        insert='insert into test values(null,?,?,?,?,?,?,?,?)'
        def read_email_from_gmail(crs):
            try:
                user='garglakshay631@gmail.com'
                password="abcd@1234"
                serverimap = imaplib.IMAP4_SSL('imap.gmail.com')
                serverimap.login(user,password)
                serverimap.select('inbox')
                serversmtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                serversmtp.login(user, password)

                typ, data = serverimap.search(None, 'UnSeen')
                print("Connection",typ)
                print(data)
                mail_ids = data[0]

                id_list = mail_ids.split()
                if len(id_list)==0:
                    print('Database is up to date')
                    return
                first_email = int(id_list[0])
                latest_email = int(id_list[-1])
                for i in range(latest_email,first_email-1,-1):
                    typ, data = serverimap.fetch(str(i), '(RFC822)' )
                    for response_part in data:
                        if isinstance(response_part, tuple):
                            mail = mailparser.parse_from_bytes(response_part[-1])
                            name=mail.subject
                            to=mail.to[-1][-1]
                            from_=mail.from_[-1][-1]
                            att=mail.attachments
                            body=mail.text_plain[-1]
                            b=body.split('\r\n')
                            contact=b[-1]
                            date=b[-3]
                            date=dt.strptime(date,'%d %B %Y, %I %p')
                            venue=b[-5]
                            reg=b[-7]
                            str1="\r\n".join(b[:-7])
                            crs.execute('insert into event values(null,?,?,?,?,?,?,?,?)',(name,from_,to,str1,date,venue,reg,contact))
                conn.commit()
                conn.close()

            except (Exception, e):
                print (str(e))    # do your thing here