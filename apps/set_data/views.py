from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.set_data.models import Contact
from sqlalchemy.orm import sessionmaker

from conectivity.settings import DB_ENGINE


# Create your views here.
class SetData(APIView):
   
    # renderer_classes = [JSONRenderer]

    def put(self, request):
        data = request.data.copy()
        
        Session = sessionmaker(DB_ENGINE)
        session = Session()
        
        fullname = data['fullname']
        email = data['email']
        phone = data['phone']

        # create a new Contact object
        new_contact = Contact(fullname, email, phone)

        # save the object into the database
        session.add(new_contact)
        session.commit()


        
        return Response(f"Usuario con {new_contact.id} Creado")