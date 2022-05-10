from .models import Medic,Patient

# getting some additional data from context
def extras(request):
    patients = Patient.objects.all()
    medics = Medic.objects.all()
    medics = [x.user.email for x in medics]
    patients = [x.user.email for x in patients]
    return {'medics':medics,'patients':patients}