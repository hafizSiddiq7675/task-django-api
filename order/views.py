# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# # Create your views here.


# class CreateOrder(APIView):
#     def post(self, request):
#         services = request.data.get('services')
#         return Response(status=status.HTTP_201_CREATED)


# class UpdateOrder(APIView):
#     def put(self, request, order_id):
#         services = request.data.get('services')
        
#         # Update the order here.
        
#         return Response(status=status.HTTP_200_OK)