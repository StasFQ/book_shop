# Generated by Django 4.1.5 on 2023-01-24 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='BookItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=254)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.book')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=254)),
                ('status', models.BooleanField()),
                ('delivery_adress', models.CharField(max_length=254)),
                ('order_id_in_shop', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.book')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItemBookItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.bookitem')),
                ('order_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.orderitem')),
            ],
        ),
    ]
