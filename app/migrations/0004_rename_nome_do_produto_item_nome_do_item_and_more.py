# Generated by Django 4.2.3 on 2024-04-17 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_data_de_entrega_entrega_data_de_entrega_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='nome_do_produto',
            new_name='nome_do_item',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='preco_unitario',
            new_name='preco_unitario_do_item',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='quantidade',
            new_name='quantidade_de_item',
        ),
    ]
