from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import AppleDevice, AppleVersion
from .forms import AppleDeviceForm, AppleVersionForm

# -------------------------
# AppleDevice Views
# -------------------------

# List all Apple devices
def device_list(request):
    devices = AppleDevice.objects.all()
    return render(request, 'AppleVersion/device_list.html', {'devices': devices})

# Add a new Apple device
def device_add(request):
    if request.method == 'POST':
        form = AppleDeviceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('device_list')
    else:
        form = AppleDeviceForm()
    return render(request, 'AppleVersion/device_form.html', {'form': form})

# -------------------------
# AppleVersion Views
# -------------------------

# List all Apple versions
def version_list(request):
    versions = AppleVersion.objects.all()
    return render(request, 'AppleVersion/version_list.html', {'versions': versions})

# Add a new Apple version
def version_add(request):
    if request.method == 'POST':
        form = AppleVersionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('version_list')
    else:
        form = AppleVersionForm()
    return render(request, 'AppleVersion/version_form.html', {'form': form})
