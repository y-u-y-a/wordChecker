# from django.shortcuts import get_object_or_404
# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.response import Response

# from core.models import Lesson
# from core.serializers import LessonSerializer


# class LessonListCreateAPIView(APIView):
#     """一覧取得・登録"""

#     def get(self, request, *args, **kwargs):
#         """一覧取得"""
#         lesson_list = Lesson.objects.all()
#         serialized = LessonSerialized(instance=lesson_list, many=True)
#         return Response(serialized.data, status.HTTP_200_OK)


#     def post(self, request, *args, **kwargs):
#         """登録"""
#         serialized = LessonSerializer(data=request.data)
#         #バリデーション
#         serialized.is_valid(raise_exception=True)
#         serialized.save()
#         return Response(serialized.data, status.HTTP_201_CREATED)


# class LessonRetrieveUpdateDestroyAPIView(APIView):
#     """詳細取得・更新・削除"""

#     def get(self, request, pk, *args, **kwargs):
#         """詳細取得"""
#         #モデルオブジェクトを取得
#         lesson = get_object_or_404(Lesson, pk=pk)
#         serializer = LessonSerializer(instance=lesson)
#         return Response(serializer.data, status.HTTP_200_OK)


#     def put(self, request, pk, *args, **kwargs):
#         """更新"""
#         lesson = get_object_or_404(Lesson, pk=pk)
#         serializer = LessonSerializer(instance=lesson, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)


#     def patch(self, request, pk, *args, **kwargs):
#         """一部更新"""
#         lesson = get_object_or_404(Lesson, pk=pk)
#         serializer = LessonSerializer(instance=lesson, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)


#     def delete(self, request, pk, *args, **kwargs):
#         """削除"""
#         lesson = get_object_or_404(Lesson, pk=pk)
#         lesson.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
