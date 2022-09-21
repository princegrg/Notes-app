
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer

# Create your views here.

# //notes GET
# //note POST
# //notes/<id> GET
# //notes/<id> PUT
# //notes/<id> DELETE

@api_view(['GET', 'POST'])
def getNotes(request):
    if request.method == 'GET':
        notes = Note.objects.all().order_by('-updated')
        serializer = NoteSerializer(notes, many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        data = request.data
        note = Note.objects.create(
            body = data['body'])
        serializer = NoteSerializer(note, many = False)
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def getNote(request, pk):

    if request.method == 'GET':
        notes = Note.objects.get(id = pk)
        serializer = NoteSerializer(notes, many = False)
        return Response(serializer.data)
    
    if request.method == 'PUT':   
        data = request.data
        note = Note.objects.get(id=pk)
        serializer = NoteSerializer(instance = note, data=data, many = False)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data) 
    
    if request.method == 'DELETE':
        note = Note.objects.get(id=pk)
        note.delete()
        return Response("Note was deleted")



# @api_view(['PUT'])
# def updateNote(request, pk):
#     data = request.data
#     note = Note.objects.get(id=pk)
#     serializer = NoteSerializer(instance = note, data=data, many = False)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)

# @api_view(['DELETE'])
# def deleteNote(request, pk):
#     note = Note.objects.get(id=pk)
#         note.delete()
#         return Response("Note was deleted")
    

# @api_view(['POST'])
# def createNote(request):
#     data = request.data
#     note = Note.objects.create(body = data['body'])
#     serializer = NoteSerializer(note, many = False)
#     return Response(serializer.data)
