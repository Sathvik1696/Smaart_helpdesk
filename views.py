from django.shortcuts import render
from urllib import request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Complaint
from .serializer import ComplaintSerializer
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render
from .models import Complaint   # import your model
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
def home(request):
    complaints = Complaint.objects.all()   # get data from DB
    return render(request, 'complaint/home.html', {'complaints': complaints})
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated]) 
@cache_page(120) 
def complaint_list(request):
    if request.method == 'GET':
        ordering = request.query_params.get('ordering')
        search = request.query_params.get('search')
        complaints = Complaint.objects.all()
        title = request.query_params.get('title')
        category = request.query_params.get('category')
        if search:
            complaints = complaints.filter(title__icontains=search)
        if category:
            complaints = complaints.filter(category=category)
        if ordering:
            complaints = complaints.order_by(ordering)
        paginator = PageNumberPagination()
        paginator.page_size = 2
        paginated_complaints = paginator.paginate_queryset(complaints, request)
        serializer = ComplaintSerializer(paginated_complaints, many=True)
        return paginator.get_paginated_response(serializer.data)
    if request.method == 'POST':
        serializer = ComplaintSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
@permission_classes([IsAuthenticated])
@cache_page(120) 
def complaint_detail(request, id):
    try:
        complaint = Complaint.objects.get(id=id)
    except Complaint.DoesNotExist:
        return Response(status=404)
    if request.method == 'GET':
        serializer = ComplaintSerializer(complaint)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = ComplaintSerializer(complaint, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    if request.method == 'DELETE':
        complaint.delete()
        return Response(status=204)
    if request.method == 'PATCH':
        serializer = ComplaintSerializer(complaint, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


# CREATE PAGE
def create_complaint_page(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        Complaint.objects.create(title=title, description=description)
        return redirect('/')

    return render(request, 'complaint/create.html')


# UPDATE PAGE
def update_complaint_page(request, id):
    complaint = get_object_or_404(Complaint, id=id)

    if request.method == 'POST':
        complaint.title = request.POST.get('title')
        complaint.description = request.POST.get('description')
        complaint.status = request.POST.get('status')
        complaint.save()
        return redirect('/')

    return render(request, 'complaint/update.html', {'c': complaint})


# DELETE
def delete_complaint_page(request, id):
    complaint = get_object_or_404(Complaint, id=id)
    complaint.delete()
    return redirect('/')