from django.shortcuts import render

# Create your views here.

from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse

import re
from .models import Person
from .utils import *

def search_term(request):
    if request.is_ajax():
	search_result = list()
	term = request.GET.get("term", None)
	term = term.lower() ##### it could be email or name of persion.
	emails = re.findall('\S+@\S+',term)
	if emails:
	    persons = list(Person.objects.filter(email__in=emails))
	    for person in persons:
	        search_result.append({"name":str(person.first_name) + str(person.last_name)}) 
	   
	else:
	    persons = list(Person.objects.filter(first_name=term,last_name=term))
	    for person in persons:
  	        search_result.append({"name":str(person.first_name)+str(person.last_name)})
   	return search_result


def new_contact(request):

    if request.method == "POST":
	ret_data = dict()
	ret_data.update({"message": "Request body is blank...Bad request.!!"})
        if request.POST:
	    first_name = request.POST.get('first_name',None)
	    last_name = request.POST.get('last_name', None)
	    phone_no = request.POST.get('phone_no', None)
	    address = request.POST.get('address', None)
	    email = request.POST.get('email',None)
	    try:
            	p = Person.objects.create(
                	first_name=first_name,
                	last_name = last_name,
                	phone_no = phone_no,
                	address = address,
			email = email
            	)
		ret_data.update({"message":"Successfully added ...!!!"})
            except:
		ret_data.update({"message":"Oop's new person not get's added...something went wrong..!!"})
		pass
     
        return JSONResponse(ret_data)

@method_decorator(authenticate_request('contact_id'))
def edit_contact(request, contact_id):
    contact = Person.objects.get(pk=contact_id)
    if request.method == "POST":
	ret_data = dict()
    	ret_data.update({"message": "Request body is blank...Bad request"})
        if request.POST:
	    try:
	    	first_name = request.POST.get('first_name',contact.first_name)
	    	last_name = request.POST.get('last_name', contact.last_name)
	    	address = request.POST.get('address', contact.address)
	    	phone_no = request.POST.get('phone_no', contact.phone_no)
		email = request.POST.get('email', contact.email)

	    	#### saving to data base#######
            	contact.first_name = first_name
            	contact.last_name = last_name
            	contact.phone_no = phone_no
            	contact.address = address
		contact.email = email
            	contact.save()
		ret_data.update({"message": "Successfully edited the record"})
	    except:
		ret_data.update({"message":"Editing for {0} is failed ".format(contact.first_name)})
		pass

            return JSONResponse(ret_data) 

               

@method_decorator(authenticate_request('contact_id'))
def delete_contact(request, contact_id):
    contact = Person.objects.get(pk=contact_id)
    
    if request.method == "POST":
        ret_data = dict()
	ret_data.update({"message": "Sucessfully deleted the record..!!"})
        try:
	    contact.delete()
        except:
	    ret_data.update({"message":"Some thing went wrong during deletion..!!!"})
	    pass
        return JSONResponse(ret_data)
