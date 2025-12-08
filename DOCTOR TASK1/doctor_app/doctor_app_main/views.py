from django.shortcuts import render, redirect, get_object_or_404
from .models import Doctor, Slot, Booking

def home(request):
    doctors = Doctor.objects.all()
    return render(request, 'home.html', {'doctors': doctors})

def book_slot(request, slot_id):
    slot = get_object_or_404(Slot, id=slot_id)
    if request.method == 'POST':
        patient_name = request.POST.get('patient_name')
        Booking.objects.create(patient_name=patient_name, doctor=slot.doctor, slot=slot)
        slot.is_booked = True
        slot.save()
        return redirect('home')
    return render(request, 'book_slot.html', {'slot': slot})
