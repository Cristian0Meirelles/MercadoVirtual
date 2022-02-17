from django.urls import path
from . import views 
urlpatterns = [path('home/', views.index, name='home'),
               ]

urlpatterns = [
    path('home/', views.index, name='home'),
    path('user/', views.listaUser.as_view(), name='User'),
    path('user/add', views.cadastroUsers, name='UserCadastro'),
    path('user/<int:pk>', views.detalhesUsers.as_view(), name='UserDetalhes'),
    path('user/edit/<int:pk>', views.editarUsers, name='UserEditar'),
    path('user/delete<int:pk>', views.excluirUsers, name='UserExcluir'),
    
    
    path('pagamento/', views.listaPagamento.as_view(), name='Pagamento'),
    path('pagamento/add', views.buscaUser, name='PagamentoUser'),
    path('pagamento/add/<int:pk>', views.cadastroPagamento, name='PagamentoCadastro'),
    path('pagamento/<int:pk>', views.detalhesPagamento, name='PagamentoDetalhes'),
    path('pagamento/delete<int:pk>', views.excluirPagamento, name='PagamentoExcluir'),
    
    path('item/', views.listaItem.as_view(), name='Item'),
    path('item/add', views.cadastroItem, name='ItemCadastro'),
    path('item/edit/<int:pk>', views.editarItem, name='ItemEditar'),
    path('item/delete<int:pk>', views.excluirItem, name='ItemExcluir'),

]