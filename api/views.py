from django.shortcuts import  get_object_or_404, render, redirect

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import VCTSerializer,Prob_occurSerializer,IndividualSerializer,OrganizationSerializer

# Create your views here.
from api.models import VCT,Prob_occur,Individual,Organization


@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'VCT_list':'VCT_list',
        'VCT_add':'VCT_add',
        'VCT_update':'VCT_update',
        'VCT_delete':'VCT_delete',

        'Prob_occur_list':'Prob_occur_list',
        'Prob_occur_add':'Prob_occur_add',
        'Prob_occur_update':'Prob_occur_update',
        'Prob_occur_delete':'Prob_occur_delete',

        'Indv_list':'Indv_list',
        'Indv_add':'Indv_add',
        'Indv_update':'Indv_update',
        'Indv_delete':'Indv_delete',

        'Org_list':'Org_list',
        'Org_add':'Org_add',
        'Org_update':'Org_update',
        'Org_delete':'Org_delete',
 	}
	return Response(api_urls)

#View
@api_view(['GET'])
def VCT_list(request):
    vct = VCT.objects.all()
    serializer = VCTSerializer(vct, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Prob_occur_list(request):
    prob = Prob_occur.objects.all()
    serializer = Prob_occurSerializer(prob, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Indv_list(request):
    indv = Individual.objects.all()
    serializer = IndividualSerializer(indv, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def Org_list(request):
    org = Organization.objects.all()
    serializer = OrganizationSerializer(org, many=True)
    return Response(serializer.data)
    

#Add
@api_view(['POST'])
def VCT_add(request):
    serializer = VCTSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def Prob_occur_add(request):
    serializer = Prob_occurSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def Indv_add(request):
    serializer = IndividualSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def Org_add(request):
    serializer = OrganizationSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#Update
@api_view(['POST'])
def VCT_update(request, pk):
	vct = VCT.objects.get(id=pk)
	serializer = VCTSerializer(instance=vct, data=request.data)

	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['POST'])
def Prob_occur_update(request, pk):
	prob = Prob_occur.objects.get(id=pk)
	serializer = Prob_occurSerializer(instance=prob, data=request.data)

	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['POST'])
def Indv_update(request, pk):
	indv = Individual.objects.get(id=pk)
	serializer = IndividualSerializer(instance=indv, data=request.data)

	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)
    
@api_view(['POST'])
def Org_update(request, pk):
	org = Organization.objects.get(id=pk)
	serializer = OrganizationSerializer(instance=org, data=request.data)

	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)



#delete

@api_view(['DELETE'])
def VCT_delete(request, pk):
	vct = VCT.objects.get(id=pk)
	vct.delete()
	return Response('Item succsesfully delete!')

@api_view(['DELETE'])
def Prob_occur_delete(request, pk):
	prob = Prob_occur.objects.get(id=pk)
	prob.delete()
	return Response('Item succsesfully delete!')

@api_view(['DELETE'])
def Indv_delete(request, pk):
	indv = Individual.objects.get(id=pk)
	indv.delete()
	return Response('Item succsesfully delete!')

@api_view(['DELETE'])
def Org_delete(request, pk):
	org = Organization.objects.get(id=pk)
	org.delete()
	return Response('Item succsesfully delete!')


def deleteIndividual(request,owner_id):
    owner = get_object_or_404(Owner, pk=owner_id)
    owner.delete()
    return redirect('index')

def deleteOrganization(request,org_id):
    org = get_object_or_404(Organization, pk=org_id)
    org.delete()
    return redirect('index')