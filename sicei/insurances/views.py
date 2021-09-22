from rest_framework.views import APIView
from rest_framework.response import Response

class StudentView(APIView):

    def get(self, request):
        content = {
                    'id_student': '15216358',
                    'name':'Victor Manuel Lara Lopez'
                }, {
                    'id_student': '12345678',
                    'name':'Maria Chan Palomo'
                }, {
                    'id_student': '98765432',
                    'name':'Oliver Ojeda Quezada'
                }
            
        return Response(content)

