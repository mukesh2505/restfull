
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.decorators import api_view,permission_classes
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from .serializer import *
from .models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from .permission import Isowner
from rest_framework import generics
from rest_framework import mixins
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
)
from rest_framework import viewsets


class Base(View):
    def get(self, request):
        return render(request, 'page_one.html')

    def post(self,request):
        pass



# class Employee_list(APIView):

#     def get(self,request):
#         employee1=Employee.objects.all()
#         serializer=EmployeeSerializers(employee1, many=True)
#         return Response(serializer.data)

#     def POST(self):
#         pass

# class Employee_list(viewsets.ModelViewSet):

#     queryset = Employee.objects.all()
#     serializer_class =  EmployeeSerializers


class Employee_details(viewsets.ModelViewSet):
    """
    Retrieve, update or delete a snippet instance.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # import pdb
        # pdb.set_trace()
        return self.queryset.all()

    def delete(self, request, **kwargs):

        data = dict.copy(request.data)
        serializer = EmployeeSerializer(data=data)

        if serializer.is_valid():
            Employee.objects.filter(id=data['id']).delete()

            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, **kwargs):
        # import pdb
        # pdb.set_trace()

        data = dict.copy(request.data)
        serializer = EmployeeSerializer(data=data)

        if serializer.is_valid():
            lob_data = Employee.objects.get(id=data['id'])
            lob_data.name = data['name']
            lob_data.employee_id = data['employee_id']
            lob_data.desgination=data['desgination']
            lob_data.owner=data['owner']

            lob_data.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# # class Employee_Detail(mixins.RetrieveModelMixin,
# #                     mixins.UpdateModelMixin,
# #                     mixins.DestroyModelMixin,
# #                     generics.GenericAPIView):
# #     queryset = Employee.objects.all()
# #     serializer_class = EmployeeSerializers
# #
# #     def get(self, request, *args, **kwargs):
# #         return self.retrieve(request, *args, **kwargs)
# #
# #     def put(self, request, *args, **kwargs):
# #         return self.update(request, *args, **kwargs)
# #
# #     def delete(self, request, *args, **kwargs):
# #         return self.destroy(request, *args, **kwargs)

@api_view(['get'])
def api_root(request ,format='None'):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'employee': reverse('employee-list', request=request, format=format)

    })