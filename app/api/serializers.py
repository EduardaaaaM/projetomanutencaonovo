from rest_framework import serializers
from app.models import Verduras, Frutas, Entrega, Pagamento, Item

class VerdurasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verduras
        fields = ['nome_Do_Produto', 'preco_da_unidade', 'total_disponivel']

class FrutasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frutas
        fields = ['nome_Do_Produto', 'preco_da_unidade', 'total_disponivel']

class EntregaSerializer(serializers.ModelSerializer):
    itens = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all())
    pagamento = serializers.PrimaryKeyRelatedField(queryset=Pagamento.objects.all())

    class Meta:
        model = Entrega
        fields = ['nome_do_consumidor', 'localidade_de_entrega', 'data_de_entrega',  'pagamento']

class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = ['meios_de_pagamento', 'valor_total']

class ItemSerializer(serializers.ModelSerializer):
    entrega = serializers.PrimaryKeyRelatedField(queryset=Entrega.objects.all())

    class Meta:
        model = Item
        fields = ['nome_do_item', 'total_de_item', 'preco_do_item', 'entrega']