from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from readings.models import Reading
from readings.serializers import ReadingsSerializer


class ReadingList(generics.ListCreateAPIView):
    """ This endpoint Create and get the List of glucose levels

        demo_param:
            "device": "FreeStyle LibreLink",
            "serial_number": "e09bb0f0-018b-429b-94c7-62bb306a0564",
            "device_timestamp": "2022-02-08T09:08:00Z",
            "recording_type": "0",
            "glucose_value_history": "138",
            "glucose_scan": ""
        
        To list glucose levels
        use ?user_id=aaaa.aaaa.aaa to filter for levels belonging to the user.
        use ?start=2021-12-12&stop=2021-12-12 to filter for levels within the date range.
        --------------------------
    
    """
    serializer_class = ReadingsSerializer
    
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.request.method == 'POST':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]
    
    def get_queryset(self):
        queryset = Reading.objects.all()
        user_id = self.request.query_params.get('user_id')
        start = self.request.query_params.get('start')
        stop = self.request.query_params.get('stop')
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        if start and stop:
            queryset = queryset.filter(device_timestamp__date__range=[start, stop])
        if start:
            queryset = queryset.filter(device_timestamp__date=start)
        return queryset

    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    


class ReadingDetails(generics.RetrieveAPIView):
    """Retrieve the details of a particular glucose level record
    """
    queryset = Reading.objects.all()
    serializer_class = ReadingsSerializer