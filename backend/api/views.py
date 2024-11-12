from django.shortcuts import render
from django.http import HttpResponse  
from .serializers import *  
from rest_framework.response import Response  # Importa Response para retornar respostas JSON.
from rest_framework import viewsets, permissions 
from .models import * 

# Função de visualização simples que retorna uma resposta de texto para a home page.
def home(request):
    return HttpResponse("this is the home page")  # Responde com o texto "this is the home page".

# Criação de uma classe de visualização de API para manipular operações CRUD de um modelo chamado Project.
class ProjectViewSet(viewsets.ViewSet):
    permissions_classes = [permissions.AllowAny]  # Define a permissão para que qualquer pessoa possa acessar.
    queryset = Project.objects.all()  # Define o conjunto de consultas com todos os objetos do modelo Project.
    serializer_class = ProjectSerializer  # Define o serializer a ser usado para conversão de dados.

    # Método para listar todos os projetos.
    def list(self, request):
        queryset = self.queryset  # Pega todos os objetos Project.
        serializer = self.serializer_class(queryset, many=True)  # Serializa o queryset em JSON.
        return Response(serializer.data)  # Retorna a lista de projetos serializados.

    # Método para criar um novo projeto.
    def create(self, request):
        serializer = self.serializer_class(data=request.data)  # Serializa os dados enviados na requisição.
        if serializer.is_valid():  # Se os dados forem válidos,
            serializer.save()  # Salva o novo projeto.
            return Response(serializer.data, status=201)  # Retorna os dados do projeto criado com status 201 (Criado).
        else:
            return Response(serializer.errors, status=400)  # Retorna os erros com status 400 (Requisição inválida).

    # Método para recuperar (detalhar) um projeto específico pelo ID.
    def retrieve(self, request, pk=None):
        project = self.queryset.get(pk=pk)  # Busca o projeto pelo ID.
        serializer = self.serializer_class(project)  # Serializa o projeto específico.
        return Response(serializer.data)  # Retorna os dados do projeto serializado.

    # Método para atualizar um projeto existente.
    def update(self, request, pk=None):
        project = self.queryset.get(pk=pk)  # Busca o projeto pelo ID.
        serializer = self.serializer_class(project, data=request.data)  # Serializa os dados novos para o projeto.
        if serializer.is_valid():  # Se os dados são válidos,
            serializer.save()  # Salva as alterações no projeto.
            return Response(serializer.data)  # Retorna os dados atualizados.
        else:
            return Response(serializer.errors, status=400)  # Retorna os erros com status 400 (Requisição inválida).

    # Método para deletar um projeto.
    def destroy(self, request, pk=None):
        project = self.queryset.get(pk=pk)  # Busca o projeto pelo ID.
        project.delete()  # Deleta o projeto.
        return Response(status=204)  # Retorna uma resposta vazia com status 204 (Sem conteúdo).
