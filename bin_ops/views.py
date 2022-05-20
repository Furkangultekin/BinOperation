from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .serializers import BinSerializer, OperationSerializer, BinOperationSerializer
from .models import Bin, BinOperation, Operation
from django.db.models import F

class AddBinView(APIView):
    def post(self, request):
        """
        :request: POST /bin_ops/add_bin
        :body: {
                    "bin_id":3,
                    "latitude":44.44,
                    "longitude":55.55
                }
        """
        serializer = BinSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class GetBinView(APIView):
    def get(self, request):
        """
        :request: GET /bin_ops/get_bin
        :response:
        {
            "bin_id":3,
            "latitude":44.44,
            "longitude":55.55
        },
        {
            "bin_id": 1,
            "latitude": "23.23",
            "longitude": "44.55"
        },
        ...
        """
        bins = Bin.objects.all()
        if not bins:
            raise NotFound('Bin not found')
        serializer = BinSerializer(bins, many=True)
        return Response(serializer.data)


class AddOperationView(APIView):
    def post(self, request):
        """
        :request: POST /bin_ops/add_operation
        :body:{
                    "operation_id":1,
                    "name":"first_operation"
                }
        """
        serializer = OperationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class GetOperationView(APIView):
    def get(self, request):
        """
        :request: GET /bin_ops/get_operation
        :response: [
                        {
                            "operation_id": 1,
                            "name": "first_operation"
                        },
                        {
                            "operation_id": 2,
                            "name": "second_operation"
                        },
                        ...
                    ]
        """
        operations = Operation.objects.all()
        if not operations:
            raise NotFound('Operation not found')
        serializer = OperationSerializer(operations, many=True)
        return Response(serializer.data)


class AddBinOperationView(APIView):
    def post(self, request):
        """
        :request: POST /bin_ops/add_bin_ops
        :body: {
                    "bin":1,
                    "operation":2,
                    "collection_frequency":3
                }
        :response: {
                        "bin": 1,
                        "operation": 2,
                        "collection_frequency": 3,
                        "last_collection": "2022-05-20T00:05:33.723524Z"
                    }
        """
        serializer = BinOperationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class GetBinOperationView(APIView):
    def get(self, request):
        """
        :request: GET /bin_ops/get_bin_ops
        :response: [
                        {
                            "bin": 1,
                            "operation": 2,
                            "collection_frequency": 3,
                            "last_collection": "2022-05-20T00:05:33.723524Z"
                        },
                        {
                            "bin": 2,
                            "operation": 1,
                            "collection_frequency": 5,
                            "last_collection": "2022-05-20T00:06:58.647883Z"
                        },
                        ...
                    ]
        """
        bin_ops = BinOperation.objects.all()
        if not bin_ops:
            raise NotFound('Bin-Operation pair not found')
        serializer = BinOperationSerializer(bin_ops, many=True)
        return Response(serializer.data)


class GetCollectionFreq(APIView):
    def get(self, request):
        """
        :request: GET /bin_ops/get_col_freq
        :response: [
                        {
                            "bin": 1,
                            "operation": 2,
                            "collection_frequency": 3,
                            "operation_name": "second_operation"
                        },
                        {
                            "bin": 2,
                            "operation": 1,
                            "collection_frequency": 5,
                            "operation_name": "first_operation"
                        }
                    ]
        """
        collect = BinOperation.objects.all().annotate(
                            operation_name=F('operation__name')
                            ).values('bin', 'operation', 'collection_frequency', 'operation_name')

        return Response(collect)