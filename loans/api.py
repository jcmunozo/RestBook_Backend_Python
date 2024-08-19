from .models import Loan
from rest_framework import viewsets, permissions
from .serializer import LoanSerializer

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LoanSerializer
