# Generated by Django 4.2.3 on 2024-04-18 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_nome_do_produto_item_nome_do_item_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entrega',
            old_name='endereco_de_entrega',
            new_name='localidade_de_entrega',
        ),
        migrations.RenameField(
            model_name='entrega',
            old_name='nome_do_cliente',
            new_name='nome_do_consumidor',
        ),
        migrations.RenameField(
            model_name='frutas',
            old_name='nome_do_produto',
            new_name='nome_Do_Produto',
        ),
        migrations.RenameField(
            model_name='frutas',
            old_name='preco_unitario',
            new_name='preco_da_unidade',
        ),
        migrations.RenameField(
            model_name='frutas',
            old_name='quantidade_disponivel',
            new_name='total_disponivel',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='preco_unitario_do_item',
            new_name='preco_do_item',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='quantidade_de_item',
            new_name='total_de_item',
        ),
        migrations.RenameField(
            model_name='pagamento',
            old_name='metodo_de_pagamento',
            new_name='meios_de_pagamento',
        ),
        migrations.RenameField(
            model_name='verduras',
            old_name='nome_do_produto',
            new_name='nome_Do_Produto',
        ),
        migrations.RenameField(
            model_name='verduras',
            old_name='preco_unitario',
            new_name='preco_da_unidade',
        ),
        migrations.RenameField(
            model_name='verduras',
            old_name='quantidade_disponivel',
            new_name='total_disponivel',
        ),
    ]
