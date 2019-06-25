# from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Board, ColumnList


class BoardList(ListView):
    model = Board
    template_name = 'board/index.html'
    context_object_name = 'board_list'
    queryset = Board.objects.order_by('-created_at')


class BoardDetail(DetailView):
    model = Board
    template_name = 'board/board.html'


class ColumnLists(ListView):
    model = ColumnList
    template_name = 'list/lists.html'
    context_object_name = 'lists'
