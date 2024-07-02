from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import LeadSerializer, OurWorkSerializer, SliderSerializer, ClientReviewSerializer, OurServiceSerializer, OurTechSerializer
from .models import Lead, OurWork, Slider, ClientReview, OurService, OurTech
from rpsoft_backend.customRenderer import CustomRenderer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.exceptions import APIException

# Create your views here.

@api_view(['GET','POST'])
@renderer_classes([CustomRenderer])
@authentication_classes([BasicAuthentication])
@permission_classes([AllowAny])
def lead_api(request, pk=None):
    statusCode=None
    try :        
        if request.method=="GET":
            data=request.data
            id=pk 
            if id is not None:
                lead=Lead.objects.get(id=pk)
                serializer=LeadSerializer(lead)  
                respData={"results":serializer.data,"message":"Request Successfull", "statusCode":statusCode}
                return Response(respData, status.HTTP_200_OK)
            
            lead=Lead.objects.all()
            serializer=LeadSerializer(lead, many=True) 
            results=serializer.data         
            if len(results)==0:
                statusCode=status.HTTP_204_NO_CONTENT

            respData={"results":serializer.data,"message":"Request Successfull", "statusCode":statusCode}
            return Response(respData, status.HTTP_200_OK)

        if request.method=="POST":
            data=request.data
            serializer=LeadSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                respData={"results":data,"message":"Lead Created Successfull", "statusCode":statusCode}
                return Response(respData, status.HTTP_201_CREATED)
            respData={"results":[],"message":serializer.errors, "statusCode":statusCode}
            return Response(respData, status.HTTP_400_BAD_REQUEST)
    except Exception as exc:
        respData={"results":[],"message":"Error Occured", "statusCode":statusCode}
        return Response(respData, status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@renderer_classes([CustomRenderer])
def ourWork_api(request, pk=None):
    statusCode=None
    if request.method=="GET":
        data=request.data
        id=pk 
        if id is not None:
            work=OurWork.objects.get(id=pk)
            serializer=OurWorkSerializer(work)  
            respData={"results":serializer.data,"message":"Request Successfull", "statusCode":statusCode}
            return Response(respData, status.HTTP_200_OK)
        
        work=OurWork.objects.all()
        serializer=OurWorkSerializer(work, many=True) 
        results=serializer.data 
        if len(results)==0:
            statusCode=status.HTTP_204_NO_CONTENT

        respData={"results":serializer.data,"message":"Request Successfull", "statusCode":statusCode}
        return Response(respData, status.HTTP_200_OK)
    
@api_view(['GET'])
@renderer_classes([CustomRenderer])
def slider_api(request, pk=None):
    statusCode=None
    if request.method=="GET":
        data=request.data
        id=pk 
        if id is not None:
            slider=Slider.objects.get(id=pk)
            serializer=SliderSerializer(slider)  
            respData={"results":serializer.data,"message":"Request Successfull", "statusCode":statusCode}
            return Response(respData, status.HTTP_200_OK)
        
        slider=Slider.objects.all()
        serializer=SliderSerializer(slider, many=True) 
        results=serializer.data 
        if len(results)==0:
            statusCode=status.HTTP_204_NO_CONTENT

        respData={"results":serializer.data,"message":"Request Successfull", "statusCode":statusCode}
        return Response(respData, status.HTTP_200_OK)
    
@api_view(['GET'])
@renderer_classes([CustomRenderer])
def client_review_api(request, pk=None):
    statusCode=None
    if request.method=="GET":
        data=request.data
        id=pk 
        if id is not None:
            review=ClientReview.objects.get(id=pk)
            serializer=ClientReviewSerializer(review)  
            respData={"results":serializer.data,"message":"Request Successfull", "statusCode":statusCode}
            return Response(respData, status.HTTP_200_OK)
        
        review=ClientReview.objects.all()
        serializer=ClientReviewSerializer(review, many=True) 
        results=serializer.data 
        if len(results)==0:
            statusCode=status.HTTP_204_NO_CONTENT

        respData={"results":serializer.data,"message":"Request Successfull", "statusCode":statusCode}
        return Response(respData, status.HTTP_200_OK)

@api_view(['GET'])
@renderer_classes([CustomRenderer])
def ourservice_api(request, pk=None):
    statusCode=None
    if request.method=="GET":
        data=request.data
        id=pk 
        if id is not None:
            service=OurService.objects.get(id=pk)
            serializer=OurServiceSerializer(service)  
            respData={"results":serializer.data,"message":"Request Successfull", "statusCode":statusCode}
            return Response(respData, status.HTTP_200_OK)
        
        service=OurService.objects.all()
        serializer=OurServiceSerializer(service, many=True) 
        results=serializer.data 
        if len(results)==0:
            statusCode=status.HTTP_204_NO_CONTENT

        respData={"results":serializer.data,"message":"Request Successfull", "statusCode":statusCode}
        return Response(respData, status.HTTP_200_OK)
    
    
@api_view(['GET'])
@renderer_classes([CustomRenderer])
def ourtech_api(request, pk=None):
    statusCode=None
    if request.method=="GET":
        data=request.data
        id=pk 
        if id is not None:
            tech=OurTech.objects.get(id=pk)
            serializer=OurTechSerializer(tech)  
            respData={"results":serializer.data,"message":"Request Successfull", "statusCode":statusCode}
            return Response(respData, status.HTTP_200_OK)
        
        tech=OurTech.objects.all()
        serializer=OurTechSerializer(tech, many=True) 
        results=serializer.data 
        if len(results)==0:
            statusCode=status.HTTP_204_NO_CONTENT

        respData={"results":serializer.data,"message":"Request Successfull", "statusCode":statusCode}
        return Response(respData, status.HTTP_200_OK)
