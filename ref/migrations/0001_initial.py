# Generated by Django 3.1.4 on 2022-02-22 19:33

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=25)),
                ('street', models.CharField(max_length=50)),
                ('street_no', models.CharField(max_length=10)),
                ('postal_code', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Medic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('doc_number', models.IntegerField(validators=[django.core.validators.MaxValueValidator(99999999999)])),
                ('clinic_info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ref.clinic')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30, null=True)),
                ('pesel', models.IntegerField(validators=[django.core.validators.MaxValueValidator(99999999999)])),
                ('date_of_birth', models.DateField()),
                ('city', models.CharField(max_length=25)),
                ('street', models.CharField(max_length=50)),
                ('street_no', models.CharField(max_length=10)),
                ('flat_no', models.CharField(max_length=10)),
                ('postal_code', models.CharField(max_length=6)),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_issue', models.DateField()),
                ('fk_medic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ref.medic')),
                ('fk_patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ref.patient')),
            ],
        ),
        migrations.CreateModel(
            name='TestType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_type', models.CharField(blank=True, choices=[('ANALITYKA OG??LNA - Badanie og??lne moczu', 'ANALITYKA OG??LNA - Badanie og??lne moczu'), ('ANALITYKA OG??LNA - Ka?? badanie og??lne', 'ANALITYKA OG??LNA - Ka?? badanie og??lne'), ('HEMATOLOGIA - Morfologia krwi', 'HEMATOLOGIA - Morfologia krwi'), ('HEMATOLOGIA - OB', 'HEMATOLOGIA - OB'), ('KOAGULOGIA - Fibrogen', 'KOAGULOGIA - Fibrogen'), ('KOAGULOGIA - TT', 'KOAGULOGIA - TT'), ('CHEMIA KLINICZNA - Glukoza', 'CHEMIA KLINICZNA - Glukoza'), ('CHEMIA KLINICZNA - S??d', 'CHEMIA KLINICZNA - S??d'), ('CHEMIA KLINICZNA - Potas', 'CHEMIA KLINICZNA - Potas'), ('CHEMIA KLINICZNA - Wap??', 'CHEMIA KLINICZNA - Wap??'), ('CHEMIA KLINICZNA - Kreatynina', 'CHEMIA KLINICZNA - Kreatynina'), ('CHEMIA KLINICZNA - Billirubina ca??kowita', 'CHEMIA KLINICZNA - Billirubina ca??kowita'), ('CHEMIA KLINICZNA - ALP', 'CHEMIA KLINICZNA - ALP'), ('CHEMIA KLINICZNA - Amylaza', 'CHEMIA KLINICZNA - Amylaza'), ('CHEMIA KLINICZNA - Lipaza', 'CHEMIA KLINICZNA - Lipaza'), ('CHEMIA KLINICZNA - Profil lipidowy', 'CHEMIA KLINICZNA - Profil lipidowy'), ('CHEMIA KLINICZNA - Triglierydy', 'CHEMIA KLINICZNA - Triglierydy'), ('CHEMIA KLINICZNA - ??elazo', 'CHEMIA KLINICZNA - ??elazo'), ('CHEMIA KLINICZNA - Ferrytyna', 'CHEMIA KLINICZNA - Ferrytyna'), ('CHEMIA KLINICZNA - Hemocysteina', 'CHEMIA KLINICZNA - Hemocysteina'), ('CHEMIA KLINICZNA - Albumina', 'CHEMIA KLINICZNA - Albumina'), ('CHEMIA KLINICZNA - Bia??ko ca??kowite', 'CHEMIA KLINICZNA - Bia??ko ca??kowite'), ('MARKERY KARDIOLOGICZNE - CKMB aktywno????', 'MARKERY KARDIOLOGICZNE - CKMB aktywno????'), ('MARKERY NOWOTWOROWE - AFP', 'MARKERY NOWOTWOROWE - AFP'), ('MARKERY NOWOTWOROWE - PSA ca??kowity', 'MARKERY NOWOTWOROWE - PSA ca??kowity'), ('ENDOKRYNOLOGIA - Progesteron', 'ENDOKRYNOLOGIA - Progesteron'), ('ENDOKRYNOLOGIA - Kortyzol', 'ENDOKRYNOLOGIA - Kortyzol'), ('ENDOKRYNOLOGIA - Insulina', 'ENDOKRYNOLOGIA - Insulina'), ('ENDOKRYNOLOGIA - Prolaktyna', 'ENDOKRYNOLOGIA - Prolaktyna'), ('DIAGNOSTYKA INFEKCJI - Anty HCV', 'DIAGNOSTYKA INFEKCJI - Anty HCV'), ('DIAGNOSTYKA INFEKCJI - Odra IgG', 'DIAGNOSTYKA INFEKCJI - Odra IgG'), ('DIAGNOSTYKA INFEKCJI - Ospa IgG', 'DIAGNOSTYKA INFEKCJI - Ospa IgG'), ('DIAGNOSTYKA INFEKCJI - Glista ludzka IgG', 'DIAGNOSTYKA INFEKCJI - Glista ludzka IgG'), ('AUTOIMMUNOLOGIA - ANA ELISA', 'AUTOIMMUNOLOGIA - ANA ELISA'), ('AUTOIMMUNOLOGIA - dsDNA', 'AUTOIMMUNOLOGIA - dsDNA'), ('ALERGOLOGIA - Zestaw pokarmowy 20', 'ALERGOLOGIA - Zestaw pokarmowy 20'), ('ALERGOLOGIA - Zestaw wziewny 20', 'ALERGOLOGIA - Zestaw wziewny 20'), ('BADANIE MOCZU - Bia??ko w moczu', 'BADANIE MOCZU - Bia??ko w moczu'), ('BADANIE MOCZU - Kreatynina w moczu', 'BADANIE MOCZU - Kreatynina w moczu')], max_length=50, null=True)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ref.test')),
            ],
        ),
    ]
