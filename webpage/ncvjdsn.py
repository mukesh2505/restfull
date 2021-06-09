# class SetMastersRegionSerializer(serializers.HyperlinkedModelSerializer):
#     region=serializers.CharField(max_length=100,required=False)
#     description = serializers.CharField(max_length=400,required=False)
#
#     class Meta:
#         model = Region
#         fields = ('id','region', 'description')
#
#     def create(self, validated_data):
#         return Region.objects.create(**validated_data)
#
#
# [5: 50
# PM, 5 / 28 / 2021] Mukesh
# Sharma:
#
#
# class SuperAdminMasterLineOfBusinessView(viewsets.ModelViewSet):
#     queryset = LineOfBusiness.objects.all()
#     serializer_class = SetMastersLineOfBusinessSerializer
#
#     def get_queryset(self):
#         return self.queryset.filter(is_active=True)
#
#     def create(self, request, **kwargs):
#
#         if isinstance(request.data, list):
#             serializer = SetMastersLineOfBusinessSerializer(data=request.data, many=True, context={'request': request})
#         else:
#             serializer = SetMastersLineOfBusinessSerializer(data=request.data, context={'request': request})
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(seriali…
#         [5: 50
#         PM, 5 / 28 / 2021] Mukesh
#         Sharma:
#
#         class SuperAdminMasterLineOfBusinessView(viewsets.ModelViewSet):
#
#     queryset = LineOfBusiness.objects.all()
#     serializer_class = SetMastersLineOfBusinessSerializer
#
#     def get_queryset(self):
#         return self.queryset.filter(is_active=True)
#
#     def create(self, request, **kwargs):
#
#         if isinstance(request.data, list):
#             serializer = SetMastersLineOfBusinessSerializer(data=request.data, many=True, context={'request': request})
#         else:
#             serializer = SetMastersLineOfBusinessSerializer(data=request.data, context={'request': request})
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, **kwargs):
#
#         data = dict.copy(request.data)
#         serializer = SetMastersLineOfBusinessSerializer(data=data)
#
#         if serializer.is_valid():
#             LineOfBusiness.objects.filter(id=data['id']).delete()
#
#             return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, **kwargs):
#
#         data = dict.copy(request.data)
#         serializer = SetMastersLineOfBusinessSerializer(data=data)
#
#         if serializer.is_valid():
#             lob_data = LineOfBusiness.objects.get(id=data['id'])
#             lob_data.line_of_business = data['line_of_business']
#             lob_data.description = data['description']
#
#             lob_data.save()
#
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
#
#
# [5: 51
# PM, 5 / 28 / 2021] Mukesh
# Sharma:
#
#
# class SetMastersServiceFundPeriod(serializers.ModelSerializer):
#     service_fund_period = serializers.DateField(format="%Y-%m-%d")
#
#     class Meta:
#         model = ServiceFundPeriod
#         fields = ['service_fund_period']
#
#     def create(self, validated_data):
#         return ServiceFundPeriod.objects.create(**validated_data)