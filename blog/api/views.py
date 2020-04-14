from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

from blog.models import TestModel
from blog.api.serializers import BlogSerializer

@api_view(["GET",])
@permission_classes((IsAuthenticated,))
def blog_detail(request, slug):
    try:
        obj_qs = TestModel.objects.get(slug=slug)
    except TestModel.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = BlogSerializer(obj_qs)
    return Response(serializer.data)

@api_view(["PUT",])
@permission_classes((IsAuthenticated,))
def blog_update(request, slug):

    try:
        obj_qs = TestModel.objects.get(slug=slug, user=request.user)
    except TestModel.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    serializer = BlogSerializer(obj_qs, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={"success": "successfully update"})
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE",])
@permission_classes((IsAuthenticated,))
def blog_delete(request, slug):
    try:
        obj_qs = TestModel.objects.get(slug=slug, user=request.user)
    except TestModel.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    operation = obj_qs.delete()
    data = {}
    if operation:
        data['success'] = "delete successfully"
    else:
        data['success'] = "delete failed"
    return Response(data=data)

@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def blog_create(request):
    account = TestModel(user=request.user)
    serializer = BlogSerializer(account, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogListView(ListAPIView):
    queryset = TestModel.objects.all()
    serializer_class = BlogSerializer
    pagination_class = PageNumberPagination
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ["title","content","user__username"]